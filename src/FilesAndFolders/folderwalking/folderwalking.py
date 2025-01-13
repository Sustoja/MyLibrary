from pathlib import Path


def _clean_up_file_extensions(file_extensions: list[str]) -> list[str]:
    return [ext.lower() if ext.startswith('.') else f".{ext.lower()}" for ext in file_extensions]

def get_files_in_folder_tree(folder: Path|str, valid_extensions: list[str] = None) -> list[Path]:
    if valid_extensions:
        valid_extensions = _clean_up_file_extensions(valid_extensions)

    folder = Path(folder)
    if not folder.exists():
        raise FileNotFoundError(f"El directorio '{folder}' no existe.")
    if not folder.is_dir():
        raise NotADirectoryError(f"'{folder}' no es un directorio.")

    return [file for file in folder.rglob('*')
            if file.is_file() and
            (valid_extensions is None or file.suffix.lower() in valid_extensions) and
               not file.name.startswith(('~', '.'))
            ]

def get_files_in_folder(folder: Path|str, valid_extensions: list[str] = None) -> list[Path]:
    if valid_extensions:
        valid_extensions = _clean_up_file_extensions(valid_extensions)

    folder = Path(folder)
    if not folder.exists():
        raise FileNotFoundError(f"El directorio '{folder}' no existe.")
    if not folder.is_dir():
        raise NotADirectoryError(f"'{folder}' no es un directorio.")

    return [file for file in folder.iterdir()
            if file.is_file() and
            (valid_extensions is None or file.suffix.lower() in valid_extensions) and
            not file.name.startswith(('~', '.'))
            ]
