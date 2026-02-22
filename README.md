## Introducción

Este repositorio incluye un script Python que mantiene sincronizado los archivos de docencia.

### generate_teaching_index.py

Escanea las carpetas `teaching/srgvua_25_26/data/` y `teaching/srgvua_25_26/pdfs/` y genera un archivo `index.json` con la lista de todos los archivos encontrados.

Ejecutar cuando:
- Agregue nuevos archivos de datos (CSV, XLSX, GPKG, MD, etc.)
- Suba nuevas láminas o materiales (PDF, HTML, DOCX, etc.)
- Elimine archivos de las carpetas

Comando:
```bash
uv run generate_teaching_index.py
```

Lo que queda <mark>pendiente</mark> es que no sirva sólo para `srgvua_25_26`, si no para cualquier carpeta de `teaching`.
