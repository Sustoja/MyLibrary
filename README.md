# Librería de paquetes de uso común

Este proyecto consiste en un conjunto de paquetes y módulos Python que utilizo en diferentes proyectos y que, si bien
no tienen un objetivo común, constituyen mi librería de referencia para los proyectos que desarrollo.

## Requisitos
- Python 3.10 o superior.

## Instalación
Basta con incluir los módulos o copiar directamente las funciones en otro proyecto.

## Uso
1. **[CSVDecoder](./src/FilesAndFolders/csvdecoder/README.md):** Detecta la codificación del texto y el carácter 
separador de los campos en ficheros CSV. Ambos elementos son fundamentales para evitar errores al cargar los datos 
en un dataframe a partir de ficheros sobre cuya generación no se tiene control.

2. **[FileHashing](./src/FilesAndFolders/filehashing/README.md):** Calcula y almacena hashes de archivos utilizando el
algoritmo SHA-256. Puede incluir también la ruta del archivo en el cálculo para detectar cambios en la localización 
además de en el contenido.

3. **[FolderWalking](./src/FilesAndFolders/folderwalking/README.md):** Devuelve la lista de ficheros de un directorio 
incluyendo, o no, los que haya en todos sus subdirectorios. Permite limitar la extensión de los ficheros que se desea 
obtener (PDF, XLSX, JPG, etc.)

4. **[TextExtractor](./src/FilesAndFolders/textextractor/README.md):** Devuelve como texto plano el contenido del 
fichero que se le pase como argumento. Admite documentos con extensión PDF, DOCX, MD y TXT.


## Contribuciones
Se agradecen las contribuciones mediante fork del repositorio y solicitudes de pull request.

## Licencia
Este proyecto utiliza la Licencia MIT. Consulte el archivo [LICENSE](LICENSE.txt) para más información.

