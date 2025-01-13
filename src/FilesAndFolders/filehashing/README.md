# Módulo File Hashing
Calcula y almacena hashes de archivos utilizando el algoritmo SHA-256. Puede incluir también la ruta
del archivo en el cálculo para detectar cambios en la localización además de en el contenido.

## Características
- **Calcula hashes de archivos**: Genera el hash de un archivo incluyendo en el cálculo, opcionalmente, su ruta.
- **Guarda y recupera hashes**: Guarda en disco y recupera diccionarios con pares {hash:nombre_archivo}.
- **Útil para detectar cambios**: Permite detectar rápidamente cambios en árboles de directorios con miles de archivos.

## Requisitos
- Python 3.10 o superior.

## Instalación
Basta con incluir el módulo o copiar directamente las funciones en otro proyecto.

## Uso
```python
from pathlib import Path
import filehashing as fh

# Rutas a los archivos
fichero1 = Path("/user/data/example.txt")
fichero2 = Path("/user/temp/example.txt")
persistent_storage = Path('almacen.pickle')

# Cálculo de hashes teniendo en cuenta la ruta
hash1 = fh.compute_hash(file_path = fichero1, include_path_in_hash = True)
hash2 = fh.compute_hash(file_path = fichero2, include_path_in_hash = True)

# Lista con los pares fichero-hash calculados previamente
hash_dict = {hash1:fichero1, hash2:fichero2}

# Almacenamiento en fichero
fh.save_hashes_and_filenames(persistent_storage, hash_dict)

# Lectura desde el fichero
hash_dict = fh.read_hashes_and_filenames(persistent_storage)
```

## Funciones

**compute_hash(file_path: Path, include_path_in_hash: bool = False) -> str**
Calcula el hash SHA-256 del contenido de un archivo.
Si include_path_in_hash es True, entonces toma en cuenta la ruta del archivo para el cálculo del hash.

**save_hashes_and_filenames(file_path: Path, files_hashes: dict) -> None**
Guarda un diccionario con rutas y hashes en un archivo pickle.

**read_hashes_and_filenames(file_path: Path) -> dict**
Lee un archivo pickle y devuelve un diccionario con rutas y hashes.

## Manejo de Errores
- FileNotFoundError si el archivo para calcular el hash no se encuentra.
- IOError si hay problemas al leer o escribir el archivo pickle.

## Licencia
Este módulo es de uso libre. Se puede modificar y adaptar sin limitación alguna.
