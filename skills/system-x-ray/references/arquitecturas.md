# Identificación de arquitectura

Formula hipótesis y contrástalas con dependencias, wiring y límites de ejecución. Se permiten arquitecturas híbridas y diferencias entre módulos. Registra evidencia a favor, evidencia contradictoria, estado y alcance de cada hipótesis.

| Patrón candidato | Evidencia que buscar | Falso positivo habitual |
| --- | --- | --- |
| Monolito | Una unidad desplegable con módulos que comparten proceso | Un solo repositorio puede contener varios servicios |
| Monolito modular | Límites de módulos y APIs internas explícitas dentro de una unidad | Carpetas por funcionalidad sin restricciones de acceso |
| Capas | Dependencias dirigidas y responsabilidades efectivas de presentación, negocio y datos | Nombres Controller/Service/Repository |
| Hexagonal / Clean | Puertos del núcleo y adaptadores externos; dependencias hacia el núcleo | Carpeta Domain que importa infraestructura |
| Microservicios | Unidades desplegables separadas y comunicación remota; examinar propiedad de datos | Muchos proyectos o contenedores sin autonomía |
| Eventos | Productores, contratos, consumidores, broker/wiring y semántica de entrega | Eventos internos del framework |
| CQRS | Rutas diferenciadas de comandos y consultas; observar modelos y persistencia | Métodos llamados Command/Query; CQRS no implica event sourcing |
| Event sourcing | Eventos persistidos como fuente de verdad y reconstrucción por replay | Logs de auditoría |
| Serverless | Funciones y disparadores declarados, permisos y recursos de infraestructura | SDK de nube instalado |
| Batch / ETL | Scheduling, extracción, transformaciones y destinos | Script aislado sin evidencia de ejecución automática |
| Plugin / escritorio | Registro/carga de extensiones o ciclo de UI y persistencia local | DLLs o archivos estáticos |

Busca además ciclos de dependencia, acceso directo a tablas de otro módulo, singletons compartidos, reflexión, SQL dinámico y DI condicional. Para llamadas dinámicas conserva destinos posibles y condiciones, no una arista confirmada arbitraria. Distingue importación estática, llamada, acceso a datos, publicación de eventos y despliegue: no son la misma relación.

Separa arquitectura observada en fuentes, arquitectura prevista en documentación y ejecución observada mediante pruebas/logs. Un conflicto es un hallazgo, no un motivo para ajustar el código al diagrama.
