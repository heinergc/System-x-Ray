# Página de System X-Ray

Web pública bilingüe con una demostración sintética, explicación de evidencia, instalación por cliente y descarga ZIP de la skill. No analiza repositorios del visitante ni conecta a un modelo.

```sh
python -m http.server 4173 --directory web
```

Abre http://localhost:4173. No necesita npm, compilación ni API. Los diagramas son SVG y las interacciones funcionan con JavaScript local. La preferencia de idioma se guarda únicamente en localStorage del navegador.

Para actualizar la descarga, regenera `assets/system-x-ray.zip` a partir de la carpeta `skills/system-x-ray`, conservando `system-x-ray/` en la raíz del ZIP. Esta copia sirve para distribución y hosting estático. El checkout del sitio administrado se mantiene aparte en `website/` para no mezclar historias Git.

Verificado con Edge headless: idiomas, escenarios válido/inválido, selección de componentes, panel de código, recorrido del flujo, instrucciones por cliente, copia al portapapeles y descarga ZIP. Layout comprobado a 1440, 390 y 780 px; sin errores JavaScript ni desbordamiento horizontal. Capturas de escritorio y móvil inspeccionadas.

Licencia GPL-2.0-only, igual que el resto de este proyecto.
