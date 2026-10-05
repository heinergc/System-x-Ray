# SPDX-License-Identifier: GPL-2.0-only
"""Portable metadata inventory, graph integrity checks and DOT export (stdlib only)."""
import argparse
import json
import os
from pathlib import Path, PurePosixPath, PureWindowsPath
import sys

EXCLUDED = {'.git', '.venv', 'venv', 'node_modules', 'vendor', '__pycache__',
            'bin', 'obj', 'dist', 'build', '.xray-work', 'graphify-out'}
STATES = {'CONFIRMADO', 'INFERIDO', 'PENDIENTE'}


def relative_path(value):
    if not isinstance(value, str) or not value.strip():
        return False
    unix, windows = PurePosixPath(value), PureWindowsPath(value)
    return not (unix.is_absolute() or windows.drive or windows.root
                or '..' in unix.parts or '..' in windows.parts)


def inventory(root):
    root = Path(root).resolve(strict=True)
    if not root.is_dir():
        raise ValueError('La raíz debe ser un directorio')
    files, omitted, errors = [], [], []

    def onerror(exc):
        # Avoid leaking absolute machine paths in portable output.
        errors.append({'error': type(exc).__name__})

    for directory, dirs, names in os.walk(root, followlinks=False, onerror=onerror):
        base = Path(directory)
        for name in list(dirs):
            path = base / name
            if name in EXCLUDED or path.is_symlink() or path.is_junction():
                dirs.remove(name)
                omitted.append(path.relative_to(root).as_posix())
        for name in sorted(names):
            path = base / name
            relative = path.relative_to(root).as_posix()
            if path.is_symlink() or name == '.env' or name.startswith('.env.'):
                omitted.append(relative)
                continue
            try:
                files.append({'path': relative, 'suffix': path.suffix.lower(),
                              'bytes': path.stat().st_size})
            except OSError as exc:
                errors.append({'path': relative, 'error': type(exc).__name__})
    return {'files': sorted(files, key=lambda item: item['path']),
            'omitted': sorted(omitted), 'errors': errors,
            'scope': 'Metadatos solamente; no detecta arquitectura ni lee contenido.'}


def validate(graph):
    errors = []
    if not isinstance(graph, dict):
        return ['El grafo debe ser un objeto JSON']
    if type(graph.get('schema_version')) is not int or graph['schema_version'] != 1:
        errors.append('schema_version debe ser 1')
    if not isinstance(graph.get('revision'), str) or not graph['revision'].strip():
        errors.append('revision es obligatoria')
    for key in ('nodes', 'edges', 'evidence'):
        if not isinstance(graph.get(key), list):
            errors.append(f'{key} debe ser una lista')
    if errors:
        return errors

    def ids(items, kind, required):
        found = set()
        for index, item in enumerate(items):
            label = f'{kind}[{index}]'
            if not isinstance(item, dict):
                errors.append(f'{label}: debe ser objeto')
                continue
            for key in required:
                if not isinstance(item.get(key), str) or not item[key].strip():
                    errors.append(f'{label}: falta {key}')
            value = item.get('id')
            if isinstance(value, str) and value.strip():
                if value in found:
                    errors.append(f'{label}: ID duplicado {value}')
                found.add(value)
        return found

    nodes = ids(graph['nodes'], 'nodes', ('id', 'label', 'kind'))
    evidence = ids(graph['evidence'], 'evidence', ('id', 'path', 'symbol'))
    for index, item in enumerate(graph['evidence']):
        if not isinstance(item, dict):
            continue
        if not relative_path(item.get('path')):
            errors.append(f'evidence[{index}]: ruta relativa inválida')
        if 'lines' in item:
            lines = item['lines']
            if not (isinstance(lines, list) and len(lines) == 2
                    and all(type(v) is int for v in lines)
                    and 1 <= lines[0] <= lines[1]):
                errors.append(f'evidence[{index}]: líneas inválidas')
    for index, edge in enumerate(graph['edges']):
        label = f'edges[{index}]'
        if not isinstance(edge, dict):
            errors.append(f'{label}: debe ser objeto')
            continue
        for key in ('source', 'target'):
            if not isinstance(edge.get(key), str) or edge[key] not in nodes:
                errors.append(f'{label}: {key} inexistente')
        if not isinstance(edge.get('relation'), str) or not edge['relation'].strip():
            errors.append(f'{label}: falta relation')
        status = edge.get('status')
        if not isinstance(status, str) or status not in STATES:
            errors.append(f'{label}: status inválido')
        refs = edge.get('evidence')
        if not isinstance(refs, list) or any(not isinstance(v, str) or v not in evidence for v in refs):
            errors.append(f'{label}: referencias de evidencia inválidas')
        elif status in ('CONFIRMADO', 'INFERIDO') and not refs:
            errors.append(f'{label}: falta evidencia')
        for state, key in (('INFERIDO', 'reason'), ('PENDIENTE', 'question')):
            if status == state and (not isinstance(edge.get(key), str) or not edge[key].strip()):
                errors.append(f'{label}: falta {key}')
    return errors


def dot(graph):
    errors = validate(graph)
    if errors:
        raise ValueError('; '.join(errors))
    quote = lambda text: json.dumps(text, ensure_ascii=False)
    result = ['digraph SystemXRay {', '  rankdir=LR;',
              '  graph [bgcolor="white", label="System X-Ray | sólido: confirmado; discontinuo: inferido", labelloc=t];',
              '  node [shape=box, style="rounded,filled", fillcolor="#EFF6FF", fontname="Arial"];',
              '  edge [fontname="Arial", fontsize=10];']
    for node in graph['nodes']:
        result.append(f'  {quote(node["id"])} [label={quote(node["label"])}];')
    for edge in graph['edges']:
        if edge['status'] == 'PENDIENTE':
            continue
        label = f'{edge["relation"]} | {edge["status"]}\n' + ', '.join(edge['evidence'])
        style = 'dashed' if edge['status'] == 'INFERIDO' else 'solid'
        result.append(f'  {quote(edge["source"])} -> {quote(edge["target"])} '
                      f'[label={quote(label)}, style={quote(style)}];')
    return '\n'.join(result + ['}', ''])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('inventory', 'validate', 'dot'))
    parser.add_argument('input', type=Path)
    parser.add_argument('--output', type=Path, help='Archivo nuevo; nunca sobrescribe existentes')
    args = parser.parse_args()
    try:
        if args.command == 'inventory':
            result = inventory(args.input)
            status = 1 if result['errors'] else 0
        else:
            graph = json.loads(args.input.read_text(encoding='utf-8-sig'))
            errors = validate(graph)
            status = 1 if errors else 0
            if args.command == 'dot':
                if errors:
                    raise ValueError('; '.join(errors))
                result = dot(graph)
            else:
                result = {'valid': not errors, 'errors': errors,
                          'scope': 'Integridad estructural; no veracidad semántica.'}
        output = result if isinstance(result, str) else json.dumps(result, ensure_ascii=False, indent=2) + '\n'
        if args.output:
            with args.output.open('x', encoding='utf-8') as handle:
                handle.write(output)
        else:
            if hasattr(sys.stdout, 'reconfigure'):
                sys.stdout.reconfigure(encoding='utf-8')
            print(output, end='')
        return status
    except (OSError, ValueError) as exc:
        print(f'Error: {exc}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
