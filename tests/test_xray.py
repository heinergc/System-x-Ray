# SPDX-License-Identifier: GPL-2.0-only
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('xray', ROOT / 'skills/system-x-ray/scripts/xray.py')
xray = importlib.util.module_from_spec(spec)
spec.loader.exec_module(xray)


class XRayTests(unittest.TestCase):
    def setUp(self):
        self.graph = json.loads((ROOT / 'examples/graph.json').read_text(encoding='utf-8'))

    def test_valid_graph_and_inferred_export(self):
        self.assertEqual(xray.validate(self.graph), [])
        output = xray.dot(self.graph)
        self.assertIn('style="dashed"', output)
        self.assertIn('EVIDENCIA-001', output)

    def test_dangling_and_duplicate_ids(self):
        self.graph['nodes'].append(copy.deepcopy(self.graph['nodes'][0]))
        self.graph['edges'][0]['target'] = 'missing'
        self.assertGreaterEqual(len(xray.validate(self.graph)), 2)

    def test_missing_evidence_and_inference_reason(self):
        self.graph['edges'][0]['evidence'] = []
        del self.graph['edges'][1]['reason']
        self.assertEqual(len(xray.validate(self.graph)), 2)

    def test_pending_is_not_drawn(self):
        edge = self.graph['edges'][0]
        edge.update(status='PENDIENTE', evidence=[], question='¿Existe esta llamada?')
        self.assertEqual(xray.validate(self.graph), [])
        self.assertNotIn('"api" -> "repository"', xray.dot(self.graph))

    def test_paths_reject_escape_and_absolute(self):
        for path in ('../secret', 'src/../../secret', 'C:/secret', '/secret', r'..\secret', r'\\server\share'):
            self.graph['evidence'][0]['path'] = path
            self.assertTrue(xray.validate(self.graph), path)

    def test_inventory_excludes_dependencies_and_environment(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / 'node_modules').mkdir()
            (root / 'node_modules/dep.js').write_text('not read')
            (root / '.env').write_text('not read')
            (root / 'app.py').write_text('not read')
            result = xray.inventory(root)
            self.assertEqual([f['path'] for f in result['files']], ['app.py'])
            self.assertIn('.env', result['omitted'])

    def test_malformed_types_return_errors(self):
        for value in (None, [], {'schema_version': True}, {'schema_version': 1, 'revision': 'x', 'nodes': [], 'edges': [None], 'evidence': []}):
            self.assertTrue(xray.validate(value))

    def test_labels_are_escaped(self):
        self.graph['nodes'][0]['label'] = 'API "quote"\nnewline'
        self.assertIn(r'API \"quote\"\nnewline', xray.dot(self.graph))


if __name__ == '__main__':
    unittest.main()
