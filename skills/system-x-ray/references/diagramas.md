# Diagramas claros y verificables

| Pregunta | Diagrama |
| --- | --- |
| Quién usa el sistema y con qué externos interactúa | Contexto C4 representado en flowchart |
| Qué se ejecuta y cómo se conecta | Contenedores/componentes y despliegue separados |
| Qué sucede durante una operación | sequenceDiagram con condiciones y errores |
| Cómo se transforma la información | Flujo de datos |
| Qué estados puede adoptar una entidad | stateDiagram-v2 con guardas verificadas |
| Qué relaciones tienen los datos | erDiagram con cardinalidad demostrada |

Usa nombres reales, IDs estables, título, descripción y leyenda. Conserva fuentes .mmd además del Markdown cuando se exporten imágenes. Los ejemplos nunca deben pasar por arquitectura del sistema analizado.

Divide contexto, componentes y detalle; como orientación, revisa diagramas que superen unos 15 nodos visibles. Etiqueta flechas con su significado (HTTP, llamada, lectura, evento). Marca INFERIDO en la etiqueta y usa trazo discontinuo; no dependas solo del color. No traces conexiones PENDIENTE como hechos; colócalas en la lista de preguntas.

Mermaid básico maximiza compatibilidad de Markdown. `architecture-beta` y C4 requieren comprobar versión y soporte del visor; C4 conceptual no obliga a usar la sintaxis C4 experimental. Graphviz/D2 sirven para grafos con disposición más controlada. SVG es apropiado para exportar; conserva el fuente editable.

Renderizado Mermaid, si el binario ya está instalado:

```sh
mmdc -i contexto.mmd -o contexto.svg -t neutral -b white
```

Renderizado DOT, si Graphviz está instalado:

```sh
python skills/system-x-ray/scripts/xray.py dot grafo.json --output arquitectura.dot
dot -Tsvg arquitectura.dot -o arquitectura.svg
```

Revisa etiquetas truncadas, cruces, contraste, tamaño de fuente, dirección de flechas, leyenda y coherencia con evidencia. Una salida exitosa del renderizador prueba sintaxis renderizable, no la exactitud del modelo. Si no puedes inspeccionar la imagen, registra esa limitación.
