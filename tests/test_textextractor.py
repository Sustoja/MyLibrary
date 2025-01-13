import pytest
from pathlib import Path
from src.FilesAndFolders.textextractor import extract_content, _get_extractor, VALID_EXTENSIONS


test_files_dir = Path("myfilesfolders/textextractor")  # Asegúrate de que esta ruta apunte al directorio correcto.

# Datos de prueba con rutas de archivos de prueba y sus contenidos esperados.
TEST_CASES = [
    ("example.txt", "Contenido del archivo TXT\náéíóúñÑ"),
    ("example.md", "Contenido del archivo Markdown\náéíóúñÑ"),
    ("example.docx", "Contenido del archivo DOCX\náéíóúñÑ"),
    ("example.pdf", "Contenido del archivo PDF áéíóúñÑ"),
]

@pytest.mark.parametrize("file_name, expected_content", TEST_CASES)
def test_extract_content(file_name, expected_content):
    file_path = test_files_dir / file_name
    assert file_path.exists(), f"El archivo de prueba {file_name} no existe."

    # Extraemos contenido y lo comparamos con el esperado.
    extracted_content = extract_content(str(file_path))
    assert extracted_content.strip() == expected_content.strip(), f"El contenido del archivo {file_name} no coincide."

def test_invalid_extension():
    invalid_file = test_files_dir / "example.unsupported"

    with pytest.raises(FileNotFoundError):
        extract_content(str(invalid_file))

def test_get_extractor():
    for ext in VALID_EXTENSIONS:
        extractor = _get_extractor(ext)
        assert callable(extractor), f"No se encontró extractor para la extensión {ext}."

    # Verificamos que extensiones no válidas devuelven None.
    assert _get_extractor("unsupported") is None

def test_extraction_error():
    invalid_file_path = test_files_dir / "example.notvalid"

    with pytest.raises(ValueError):
        extract_content(str(invalid_file_path))
