# Módulo My Logging
Proporciona una variable global "logger" para registrar mensajes desde todos los modulos de una aplicación, tanto por 
el terminal como en fichero. Utiliza los mismos niveles de registro que el módulo estándar de logging:
- NOTSET=0
- DEBUG=10
- INFO=20
- WARN=30
- ERROR=40
- CRITICAL=50

## Características
- Se puede asignar distintos valores mínimos de logging a la salida por terminal y por fichero.
- Colorea en rojo los mensajes por terminal que tengan nivel WARN o superior.
- Acceso unificado mediante una variable global ('logger') que se carga al importar el módulo.

## Requisitos
- Python 3.10 o superior.

## Instalación
Basta con incluir el módulo o copiar directamente las funciones en otro proyecto.

## Uso
```python
from MyLogging import logger, LOG_FILE_NAME

# Vacía el fichero de log
print(LOG_FILE_NAME)
logger.reset_log_file()

# Registro de eventos en fichero y por terminal
logger.log.info('Somewhat relevant info')
logger.log.warning('Warning message')
logger.log.error('Application error')
```

## Funciones
**def reset_log_file(self, limit=-1) -> None**
Resetea el contenido del fichero de log al tamaño en bytes que se pase como argumento. Si no se indica, se
vacía por completo.

Para usar las funciones de log estándar del módulo logging se utiliza la variable global "logger" que se
importa con el módulo.

## Manejo de Errores
- RuntimeError si hay algún error al crear el objeto 'logger' en el momento de la importación.

## Licencia
Este módulo es de uso libre. Se puede modificar y adaptar sin limitación alguna.
