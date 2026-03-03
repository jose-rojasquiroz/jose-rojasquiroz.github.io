#!/usr/bin/env python3
"""
Script para generar un índice JSON de los archivos en las carpetas
de datos y PDFs del seminario de Housing Retrofit.
"""

import os
import json
from pathlib import Path

def get_files_from_directory(dir_path):
    """Lee los archivos de una carpeta y retorna una lista ordenada."""
    if not os.path.exists(dir_path):
        return []
    
    files = []
    for filename in sorted(os.listdir(dir_path)):
        if filename.startswith('.'):
            continue
        
        file_path = os.path.join(dir_path, filename)
        if os.path.isfile(file_path):
            ext = Path(filename).suffix.lower().lstrip('.')
            files.append({
                "name": filename,
                "path": f"{os.path.basename(dir_path)}/{filename}".replace('\\', '/'),
                "type": ext if ext else "file"
            })
    
    return files

def main():
    base_path = os.path.dirname(os.path.abspath(__file__))
    teaching_path = os.path.join(base_path, 'teaching', 'srgvua_25_26')
    data_path = os.path.join(teaching_path, 'data')
    pdfs_path = os.path.join(teaching_path, 'pdfs')
    notebooks_path = os.path.join(teaching_path, 'notebooks')
    output_file = os.path.join(teaching_path, 'index.json')
    
    # Generar índice
    index = {
        "datasets": get_files_from_directory(data_path),
        "slides": get_files_from_directory(pdfs_path),
        "notebooks": get_files_from_directory(notebooks_path)
    }
    
    # Guardar JSON
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Index generado: {output_file}")
    print(f"📊 Datasets encontrados: {len(index['datasets'])}")
    print(f"📄 Slides encontrados: {len(index['slides'])}")
    print(f"📓 Notebooks encontrados: {len(index['notebooks'])}")
    
    # Mostrar contenido
    if index['datasets']:
        print("\n📊 Datasets:")
        for f in index['datasets']:
            print(f"  - {f['name']}")
    
    if index['slides']:
        print("\n📄 Slides:")
        for f in index['slides']:
            print(f"  - {f['name']}")
    
    if index['notebooks']:
        print("\n📓 Notebooks:")
        for f in index['notebooks']:
            print(f"  - {f['name']}")

if __name__ == '__main__':
    main()
