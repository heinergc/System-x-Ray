# Contrato de intercambio v1

JSON UTF-8 con `schema_version: 1`, `revision` (commit o identificación de la muestra), listas `evidence`, `nodes` y `edges`. Evidencia: `id`, `path` relativo a la raíz, `symbol` y opcional `lines` como [inicio, fin]. No almacena fragmentos ni secretos.

Nodo: `id`, `label`, `kind`. Arista dirigida: `source`, `target`, `relation`, `status` (CONFIRMADO, INFERIDO o PENDIENTE), `evidence` (lista de IDs). INFERIDO exige `reason`; PENDIENTE exige `question`. Una arista PENDIENTE es una hipótesis, no una conexión demostrada, y no se dibuja por defecto.

`validate` detecta IDs duplicados, endpoints inexistentes, referencias de evidencia rotas, rutas absolutas/traversal y trazabilidad ausente. No comprueba existencia de rutas contra un repositorio ni semántica del código. Grafos de otras herramientas necesitan conversión explícita: no se presume compatibilidad con Graphify.

Ejemplo de uso del contrato: [grafo sintético](../assets/graph.example.json). Sirve exclusivamente para demostrar validación/exportación, no describe el proyecto del usuario.
