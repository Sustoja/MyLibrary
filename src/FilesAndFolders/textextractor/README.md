# Módulo Text Extractor
Devuelve como texto plano el contenido del fichero que se le pase como argumento. Admite documentos con extensión 
PDF, DOCX, MD y TXT.

## Características
- **Admite ficheros PDF, Word, Markdown y texto plano**: pdf, docx, md, txt.
- **Detecta el tipo de fichero según su extensión**: evita distinguir mayúsuculas y minúsculas.

## Requisitos
- Python 3.10 o superior.
- Librerías necesarias:
  - `pypdf`
  - `python-docx`

Se instalan ejecutando:
```bash
pip install -r requirements.txt
```

## Instalación
Basta con incluir el módulo o copiar directamente las funciones en otro proyecto.

## Uso
```python
from textextractor import extract_content, VALID_EXTENSIONS

print(f"Extensiones aceptadas: {VALID_EXTENSIONS}")

text = extract_content('MsWord_file.docx')
print(f"Contenido del fichero: {text}")
```

## Funciones
**def extract_content(file_path: str) -> str:**
Devuelve como una cadena de texto todo el contenido del fichero que se le pase como argumento.

## Manejo de Errores
- FileNotFoundError si no se encuentra el fichero a procesar.
- ValueError si el fichero no tiene una extensión admitida o no se puede extraer el contenido.

## Licencia
Este módulo es de uso libre. Se puede modificar y adaptar sin limitación alguna.
