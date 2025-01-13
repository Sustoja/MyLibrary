import pandas as pd
from pathlib import Path


ENCODINGS = ['utf-8', 'windows-1252', 'cp1252', 'iso-8859-1', 'utf-8-sig', 'ascii']
SEPARATORS = [';', ',', '\t', '|', ':']


def detect_csv_encoding(file: Path|str, separator: str) -> str:
    for encoding in ENCODINGS:
        try:
            pd.read_csv(file, sep=separator, encoding=encoding, nrows=1)
            return encoding
        except UnicodeDecodeError:
            continue
        except Exception as e:
            raise RuntimeError(f"Error inesperado al intentar leer el archivo: {e}")
    raise ValueError("No se pudo detectar la codificación de texto.")


def detect_csv_separator(file: Path|str) -> str:
    for encoding in ENCODINGS:
        try:
            with open(file, 'r', encoding=encoding, errors='replace') as f:
                header = f.readline()
                if header:
                    separator = max(SEPARATORS, key=header.count)
                    return separator
        except UnicodeDecodeError:
            continue
        except Exception as e:
            raise RuntimeError(f"Error inesperado al intentar leer el archivo: {e}")
    raise ValueError("No se pudo detectar un separador válido.")


def detect_encoding_and_separator(file: Path|str) -> (str, str):
    separator = detect_csv_separator(file)
    encoding = detect_csv_encoding(file, separator)

    return separator, encoding
