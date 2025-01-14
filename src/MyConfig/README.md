# Módulo My Config
Proporciona una variable global "cfg" para tener acceso a los valores de configuración de una aplicación desde todos 
sus módulos.. Utiliza el estándar [TOMLI](https://pypi.org/project/tomli/) para definir el fichero de configuración 
(_config.toml_)

## Características
- **Definición sencilla de valores**: TOMLI admite variables atomícas, listas y diccionarios.
- **Acceso unificado a la configuración**: mediante una variable global ('cfg') que se carga al importar el módulo.

## Requisitos
- Python 3.10 o superior.
- Librerías necesarias:
  - `tomli`

Se instalan ejecutando:
```bash
pip install -r requirements.txt
```

## Instalación
Basta con incluir el módulo o copiar directamente las funciones en otro proyecto.

## Uso
``` 
# Config file (config.toml) in toml format

excel_dir = '../Excel'
client_sheets = ['ClientA', 'ClientB']
cols_and_types = {'A'='str', 'B'='int'}
```

```python
from config import cfg

print("Excel Directory:", cfg["excel_dir"])
print("Client Sheets:", cfg["client_sheets"])
print("Columns and Types:", cfg["cols_and_types"])
```

## Funciones
No es necesario importar funciones, basta con importar la variable "cfg" de módulo.

## Manejo de Errores
- FileNotFoundError si no se encuentra el fichero de configuración (config.toml).
- ValueError si hay algún error con la definición de valores en el fichero de configuración.

## Licencia
Este módulo es de uso libre. Se puede modificar y adaptar sin limitación alguna.
