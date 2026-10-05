# Herramientas y MCP

Investigación: 2026-10-05. La configuración MCP depende del cliente y debe adaptarse a su formato; no prometer soporte de MCP por parte de cualquier modelo aislado.

| Herramienta | Uso recomendado | Dependencias / límite |
| --- | --- | --- |
| rg + lectura del código | Inventario y verificación directa | Disponible sin MCP; texto no resuelve llamadas dinámicas |
| Serena MCP | Símbolos y referencias mediante servidores de lenguaje | Requiere soporte del lenguaje y proyecto; también incluye edición |
| Graphify MCP | Consultar un grafo persistente de dependencias y evidencia | Requiere construir/actualizar grafo; comprobar fuentes y versión |
| Mermaid CLI | Secuencias, estados, ER y flujos editables, SVG/PNG/PDF | Node y navegador para renderizado; no requiere MCP |
| Graphviz / D2 | Exportación y disposición de diagramas | Binarios adicionales; no detectan arquitectura por sí mismos |
| MCP filesystem | Acceso a fuentes cuando el cliente carece de lectura | Incluye escritura; directorio permitido no equivale a solo lectura |

Recomendación inicial: lectura/rg + Mermaid; añadir Serena para navegación semántica y Graphify cuando el tamaño del sistema justifique un grafo persistente. Ningún MCP deduce por sí solo la arquitectura funcional con certeza.

Configuración Graphify opcional en [mcpServers de ejemplo](../assets/mcp.graphify.example.json), basada en su comando oficial `python -m graphify.serve <graph.json>`. Requiere el paquete y el grafo existente; adapta rutas absolutas y ejecutable Python. Este ejemplo no instala ni habilita servidores automáticamente. No mezcles su grafo con el contrato propio de X-Ray sin conversión.

Antes de añadir un MCP: verifica repositorio oficial, versión exacta, herramientas expuestas y permisos; configura únicamente el proyecto necesario. Para filesystem de solo lectura real puede usarse un volumen Docker `ro` según la documentación oficial. No envíes código privado a renderizadores públicos sin autorización. Usa renderizado local o un servicio propio.

Fuentes primarias:

- [Serena](https://github.com/oraios/serena) y [clientes y configuración](https://oraios.github.io/serena/02-usage/030_clients.html).
- [Graphify](https://github.com/Graphify-Labs/graphify), sección Using the graph directly.
- [Mermaid CLI](https://github.com/mermaid-js/mermaid-cli).
- [MCP filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem).
- [D2](https://d2lang.com/) y [Graphviz](https://graphviz.org/).

AWS Diagram MCP es una opción a evaluar para iconografía cloud; en esta investigación sus páginas no pudieron consultarse correctamente, por lo que no se incluye una configuración sin verificar. La iconografía no sustituye evidencia del despliegue.
