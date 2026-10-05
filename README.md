# System X-Ray

Skill para reconstruir el funcionamiento real de sistemas existentes: arquitectura, procesos, reglas, datos, integraciones y resultados respaldados por evidencia.

Derivada del [documento original](System%20X-Ray.md), que se conserva como referencia. Las instrucciones del documento son material de diseño; no se ejecutan como una solicitud de analizar un sistema inexistente en esta carpeta.

## Uso

Entrada principal: [SKILL.md](skills/system-x-ray/SKILL.md). La lógica está escrita en Markdown y no depende de un modelo o API específicos. Su calidad depende de la capacidad del modelo y del acceso a fuentes; herramientas, MCP y descubrimiento automático dependen del cliente.

En clientes con soporte de skills, instala la carpeta `skills/system-x-ray` en su directorio de skills. Para Codex, puede copiarse a `~/.codex/skills/system-x-ray`; para otros clientes consulta su ruta de descubrimiento. No hace falta copiar todo el repositorio. La carpeta incluye referencias y un script Python sin dependencias externas.

En un chat sin soporte de skills, proporciona SKILL.md y las referencias pertinentes, junto con los archivos del sistema. Los enlaces a scripts y referencias solo funcionan si esos archivos también están accesibles.

Ejemplos de petición:

```text
Usa $system-x-ray en este repositorio. Produce un panorama y explica el flujo de aprobación con evidencia.
Usa $system-x-ray en modo completo y crea docs/analisis-sistema, incluyendo cobertura y preguntas pendientes.
Usa $system-x-ray para determinar qué componentes y tablas afecta cambiar esta regla.
```

## Herramientas incluidas

Python 3.12+; solo biblioteca estándar:

```sh
python skills/system-x-ray/scripts/xray.py inventory .
python skills/system-x-ray/scripts/xray.py validate examples/graph.json
python skills/system-x-ray/scripts/xray.py dot examples/graph.json --output arquitectura.dot
python -m unittest discover -s tests -v
```

El inventario usa metadatos, excluye generados/dependencias habituales, no sigue enlaces y omite .env. No sustituye un análisis semántico. El validador comprueba integridad y referencias del grafo; no prueba afirmaciones del código. Los archivos de salida se crean exclusivamente si no existen.

Graphviz opcional: `dot -Tsvg arquitectura.dot -o arquitectura.svg`. Mermaid CLI es la alternativa para diagramas Mermaid. Los renderizadores no están incluidos y su ausencia no impide analizar fuentes ni producir diagramas editables.

## MCP opcionales

[Investigación y elección de herramientas](skills/system-x-ray/references/herramientas-mcp.md): Serena para símbolos/referencias, Graphify para grafos persistentes. [Configuración de ejemplo](config/mcp.graphify.example.json); requiere adaptar rutas e instalar la dependencia en el entorno elegido. No se modifica la configuración global del cliente automáticamente.

## Diseño y validación

[Análisis y mejoras del prompt original](docs/analisis-del-prompt.md). [Pruebas de comportamiento propuestas](evals/cases.md). Los tests automatizados cubren los helpers; no equivalen a evaluar la skill con todos los modelos.

## Licencia

[GNU GPL versión 2 solamente](LICENSE), identificador `GPL-2.0-only`, elegida por el propietario siguiendo la licencia base del kernel Linux. La excepción de llamadas al sistema del kernel no se incorpora porque no corresponde a este proyecto. Consulta el texto completo de la licencia para sus condiciones de redistribución y modificación.
