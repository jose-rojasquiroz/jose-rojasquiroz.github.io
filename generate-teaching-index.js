#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

// Ruta base del seminario
const basePath = path.join(__dirname, 'teaching', 'srgvua_25_26');
const pdfsPath = path.join(basePath, 'pdfs');
const notebooksPath = path.join(basePath, 'notebooks');
const outputFile = path.join(basePath, 'index.json');

function getFiles(dirPath) {
  if (!fs.existsSync(dirPath)) {
    return [];
  }
  
  const files = fs.readdirSync(dirPath);
  return files
    .filter(file => !file.startsWith('.')) // Ignorar archivos ocultos
    .map(file => ({
      name: file,
      path: path.join(path.basename(dirPath), file).replace(/\\/g, '/'),
      type: path.extname(file).toLowerCase().substring(1) || 'file'
    }))
    .sort((a, b) => (a.name < b.name ? -1 : a.name > b.name ? 1 : 0));
}

// Generar estructura
const index = {
  datasets: [],
  slides: getFiles(pdfsPath),
  notebooks: getFiles(notebooksPath)
};

// Guardar JSON
fs.writeFileSync(outputFile, JSON.stringify(index, null, 2), 'utf-8');
console.log(`✅ Index generado: ${outputFile}`);
console.log(`📄 Slides encontrados: ${index.slides.length}`);
console.log(`📓 Notebooks encontrados: ${index.notebooks.length}`);
