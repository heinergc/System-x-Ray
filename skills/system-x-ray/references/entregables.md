# Documentación por profundidad

Panorama: índice/resumen, arquitectura, un flujo representativo, evidencia y pendientes. Completo: estructura siguiente, con capítulos no aplicables identificados como tales y capítulos sin acceso marcados PENDIENTE. Impacto: cambio consultado, dependencias y consumidores, reglas/datos afectados, evidencia y límites.

```text
docs/analisis-sistema/
  README.md
  01-vision-general.md
  02-arquitectura.md
  03-entradas-salidas.md
  04-flujos-negocio.md
  05-componentes.md
  06-base-datos.md
  07-reglas-negocio.md
  08-integraciones.md
  09-autenticacion-autorizacion.md
  10-manejo-errores-logs.md
  11-configuracion.md
  12-despliegue.md
  13-dependencias.md
  14-riesgos-deuda-tecnica.md
  15-guia-mantenimiento.md
  16-trazabilidad.md
  17-glosario.md
  diagramas/
    README.md
```

README: propósito, actores, funciones/entradas/salidas y tecnología detectada, índice relativo, sistema en una página y cobertura. Registra revisión, fuentes consultadas, áreas excluidas y preguntas pendientes. Una ausencia en la muestra no demuestra ausencia en el sistema.

Para cada PROC: objetivo, actor/disparador, entradas/formato, validaciones y RN, permisos, llamadas con rutas/símbolos, datos e integraciones, transacción, resultado, errores y secuencia. Selecciona operaciones por relevancia para el usuario; en modo completo apunta a 3–10 si existen, sin inventarlas ni limitar artificialmente el alcance pedido.

Tablas útiles:

- Procesos: ID, actor, entrada, procesamiento, datos, salida, evidencia, enlace al detalle.
- RN: ID, condición/regla, componente/símbolo, impacto, estado, evidencia.
- Datos: objeto/tipo, propósito, consumidor, evidencia; CRUD por proceso y tabla con lectura/escritura demostrada.
- UI: pantalla, acción, handler/endpoint, resultado y tablas afectadas.
- Integraciones: dirección, protocolo, contrato, autenticación por nombre, errores/reintentos y evidencia.
- Configuración: nombre, propósito, consumidor, sensibilidad; nunca valor secreto.
- Dependencias: manifiesto, versión declarada y resuelta si disponible, uso observado; obsolescencia requiere verificación externa vigente.
- Riesgos: observación, condición necesaria, impacto y estado; no confundir posibilidad con vulnerabilidad explotable.
- Evidencia: ID, ruta, símbolo/líneas, revisión, qué demuestra y qué no demuestra.

Mantenimiento: dónde cambiar pantallas, campos, reglas, consultas, reportes y permisos, con rutas verificadas. Glosario: términos específicos del negocio. Errores: captura → registro → tratamiento → salida, incluyendo silencios observados. Despliegue: recursos definidos frente a estado operativo comprobado.
