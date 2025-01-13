# Módulo CSV Decoder
Detecta la codificación del texto y el carácter separador de los campos en ficheros CSV. Ambos elementos son
fundamentales para evitar errores al cargar los datos en un dataframe a partir de ficheros sobre cuya 
generación no se tiene control.

## Características
- **Codificaciones reconocidas**: utf-8, windows-1252, cp1252, iso-8859-1, utf-8-sig y ascii
- **Separadores reconocidos**: coma, punto y coma, tabulador, dos puntos y barra vertical (|)

## Requisitos
- Python 3.10 o superior.
- Librerías necesarias:
  - `pandas`

## Instalación
Basta con incluir el módulo o copiar directamente las funciones en otro proyecto.

## Uso
```python
import pandas as pd
import csvdecoder as csv

# Detección
file_path = 'datos.csv'
separator, encoding = csv.detect_encoding_and_separator(file_path)

# y carga de un dataframe
df = pd.read_csv(file_path, sep = separator, encoding = encoding)
```

## Funciones

**detect_csv_encoding_and_separator(file: Path | str) -> (str, str)**
Es la función principal: devuelve el separador y la codificación, en ese orden.

**detect_csv_separator(file: Path | str) -> str**
Detecta el separador analizando la primera línea como un fichero de texto corriente (no CSV).

**detect_csv_encoding(file: Path | str, separator: str) -> str**
Detecta la codificación del fichero tratándolo como un fichero CSV. Requiere conocer de antemano
el separador de campos.

## Manejo de Errores
- ValueError si no se reconoce la codificación o el separador de campos.
- RuntimeError si se produce un error inesperado durante el reconocimiento.

## Licencia
Este módulo es de uso libre. Se puede modificar y adaptar sin limitación alguna.
