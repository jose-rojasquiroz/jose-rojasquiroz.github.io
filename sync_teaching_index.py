#!/usr/bin/env python3
"""
Script para mantener sincronizado teaching/index.html con index.html
El archivo teaching/index.html es idéntico pero con la sección Teaching
activada por defecto.
"""

import os
import re
from pathlib import Path

def create_teaching_index():
    """Crea teaching/index.html a partir de index.html con Teaching activado"""
    
    base_path = os.path.dirname(os.path.abspath(__file__))
    main_index = os.path.join(base_path, 'index.html')
    teaching_index = os.path.join(base_path, 'teaching', 'index.html')
    
    # Leer el archivo principal
    with open(main_index, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Cambiar secciones activas: deactivar home, activar teaching
    content = content.replace(
        'id="btn-home" class="active-btn"',
        'id="btn-home"'
    )
    content = content.replace(
        'id="btn-teaching"',
        'id="btn-teaching" class="active-btn"'
    )
    
    content = content.replace(
        'id="home" class="content-section active-section"',
        'id="home" class="content-section"'
    )
    content = content.replace(
        'id="teaching" class="content-section"',
        'id="teaching" class="content-section active-section"'
    )
    
    # 2. Ajustar rutas relativas: teaching/srgvua_25_26 -> srgvua_25_26
    # Esto es necesario porque teaching/index.html está un nivel más abajo
    content = content.replace(
        'href="teaching/srgvua_25_26/',
        'href="srgvua_25_26/'
    )
    content = content.replace(
        "fetch('teaching/srgvua_25_26/",
        "fetch('srgvua_25_26/"
    )
    
    # 3. Cambiar referencias a archivos estáticos que están en la raíz
    # foto, svg, etc deben apuntar a ../
    content = content.replace(
        'src="foto_joserojasquiroz.jpg"',
        'src="../foto_joserojasquiroz.jpg"'
    )
    content = content.replace(
        'src="svg/',
        'src="../svg/'
    )
    content = content.replace(
        'href="https://cdn.jsdelivr.net/gh/dreampulse/computer-modern-web-font@master/fonts.css"',
        'href="https://cdn.jsdelivr.net/gh/dreampulse/computer-modern-web-font@master/fonts.css"'
    )
    
    # Guardar el nuevo archivo
    os.makedirs(os.path.dirname(teaching_index), exist_ok=True)
    with open(teaching_index, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ teaching/index.html generado correctamente")
    print(f"📍 Ubicación: {teaching_index}")

if __name__ == '__main__':
    create_teaching_index()
