from src.FilesAndFolders.csvdecoder  import detect_encoding_and_separator

def test_detect_csv_encoding_and_separator():
    test_cases = [
        ("./myfilesfolders/csv/Comas.csv", (',', 'utf-8')),
        ("./myfilesfolders/csv/WinPuntoComa.txt", (';', 'windows-1252')),
        ("./myfilesfolders/csv/Tabulador.csv", ('\t', 'windows-1252')),
    ]

    for file_path, expected in test_cases:
        separator, encoding = detect_encoding_and_separator(file_path)
        assert (separator,
                encoding) == expected, f"Error en {file_path}: esperado {expected}, obtenido {(separator, encoding)}"

