# Módulo Folder Walking
Devuelve la lista de ficheros de un directorio incluyendo, o no, los que haya en todos sus subdirectorios. Permite
limitar la extensión de los ficheros que se desea obtener (PDF, XLSX, JPG, etc.)


## Características
- **Extensiones admitidas para la selección:** todas las que se pasen como argumento, sin límites ni requisitos. No
distingue mayúsuculas de minúsculas y es indiferente si se pone el punto antes de la extesnión ('.pdf' se trata igual 
que 'PdF')
- **Excluye ficheros especiales de Windows y MacOS** que comiencen por punto o por virgulilla (~).

## Requisitos
- Python 3.10 o superior.

## Instalación
Basta con incluir el módulo o copiar directamente las funciones en otro proyecto.

## Uso
```python
from folderwalking import get_files_in_folder, get_files_in_folder_tree

test_folder = './tests/mydata'
extensions = ['tXt', '.pdF']

print("\nFicheros de texto en el directorio")
for file in get_files_in_folder(test_folder, extensions):
    print(file)

print("\nFicheros de texto en el árbol de directorios")
for file in get_files_in_folder_tree(test_folder, extensions):
    print(file)
```

## Funciones
**get_files_in_folder(folder: Path|str, valid_extensions: list[str] = None) -> list[Path]**
Devuelve los ficheros con las extensiones especificadas que haya en el primer nivel del directorio. Si no se pasa
una lista de extensiones, entonces devuelve todos los ficheros.

**get_files_in_folder_tree(folder: Path|str, valid_extensions: list[str] = None) -> list[Path]**
Devuelve los ficheros con las extensiones especificadas que haya en todos los subniveles del directorio. Si no se 
pasa una lista de extensiones, entonces devuelve todos los ficheros.

## Manejo de Errores
- FileNotFoundError si no se encuentra el directorio de búsqueda utilizado como argumento.
- NotADirectoryError si el directorio de búsqueda no es realmente un directorio.

## Licencia
Este módulo es de uso libre. Se puede modificar y adaptar sin limitación alguna.
