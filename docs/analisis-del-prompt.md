# Análisis del documento original

El archivo contiene 40 secciones de instrucciones para radiografiar un sistema; no contiene código ni describe una arquitectura concreta. Sus fortalezas son el foco funcional extremo a extremo, la clasificación de certeza, la trazabilidad código/datos y la protección de secretos.

| Limitación encontrada | Mejora implementada |
| --- | --- |
| Prompt extenso con obligaciones repetidas | Entrada corta y referencias que se leen según necesidad |
| Estructura completa aun cuando la pregunta es pequeña | Modos panorama, completo e impacto |
| Ejemplos centrados en capas web y SQL | Criterios para arquitecturas híbridas, eventos, batch, serverless y escritorio |
| CONFIRMADO puede confundirse con ejecución real | Diferenciar lectura de fuente, configuración declarada y observación en ejecución |
| Diagramas sin contrato verificable | Grafo JSON con estados/evidencia por arista y validador estructural |
| Sin estrategia para repositorios grandes | Análisis por módulo, revisión y registro de cobertura/puntos de continuación |
| Mermaid sin ruta de exportación | Guía Mermaid CLI y exportador DOT opcional para Graphviz |
| Sin estrategia de integración entre modelos | Núcleo Markdown independiente del proveedor y MCP opcionales del cliente |
| No define qué hacer con información contradictoria | Registrar diferencias entre documentos, código y despliegue |

La skill conserva la profundidad del original en su referencia de entregables, incluyendo CRUD, botones/UI, procedencia de valores, SQL, transacciones, estados, permisos y mantenimiento. El original se conserva sin alterarlo para permitir comparación.

No hay una aplicación para radiografiar en este repositorio. El grafo de ejemplo es sintético. Los helpers automatizan inventario e integridad/exportación; no identifican patrones arquitectónicos automáticamente.

## Criterios de aceptación

- Skill invocable y autocontenida al copiar su carpeta.
- Hechos diferenciados de hipótesis y ausencia de acceso.
- Arquitectura sustentada por límites/dependencias, sin imponer capas ficticias.
- Ningún salto dinámico confirmado sin evidencia.
- Diagramas editables y relaciones trazables.
- Sin requisitos de API, credenciales o proveedor de modelos.
- Configuración MCP explícitamente opcional.
- Helpers ejecutados con casos positivos y negativos.
- Publicación asociada a un destino definido por el usuario.
