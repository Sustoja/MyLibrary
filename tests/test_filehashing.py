import pytest
import hashlib
import pickle
from pathlib import Path
from tempfile import TemporaryDirectory
from src.FilesAndFolders.filehashing import *


FHASH_DICT = {"file1.txt": "dummyhash1",
              "file2.txt": "dummyhash2"}


@pytest.fixture
def temp_files():
    with TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        file_1 = tmp_path / "file1.txt"
        file_2 = tmp_path / "file2.txt"
        hash_file = tmp_path / "hashes.pkl"

        # Crear archivos de prueba
        file_1.write_text("Contenido del archivo 1")
        file_2.write_text("Otro contenido del archivo 2")
        yield file_1, file_2, hash_file


def test_compute_hash_valid_file_with_path(temp_files):
    file_1, _, _ = temp_files
    expected_hash = hashlib.sha256()
    expected_hash.update(str(file_1).encode('utf-8'))
    expected_hash.update(file_1.read_bytes())

    assert compute_hash(file_1, True) == expected_hash.hexdigest()


def test_compute_hash_valid_file_no_path(temp_files):
    file_1, _, _ = temp_files
    expected_hash = hashlib.sha256()
    expected_hash.update(file_1.read_bytes())

    assert compute_hash(file_1) == expected_hash.hexdigest()


def test_compute_hash_nonexistent_file():
    non_existent_file = Path("no_existe.txt")
    with pytest.raises(FileNotFoundError):
        compute_hash(non_existent_file)


def test_save_hash_file(temp_files):
    _, _, hash_file = temp_files

    save_hashes_and_filenames(hash_file, FHASH_DICT)
    assert hash_file.exists()

    with hash_file.open('rb') as f:
        loaded_fhashes = pickle.load(f)
    assert loaded_fhashes == FHASH_DICT


def test_read_hash_file(temp_files):
    _, _, hash_file = temp_files

    with hash_file.open('wb') as f:
        pickle.dump(FHASH_DICT, f)

    loaded_fhashes = read_hashes_and_filenames(hash_file)
    assert loaded_fhashes == FHASH_DICT


def test_read_hash_file_nonexistent():
    non_existent_file = Path("no_existe.pkl")
    with pytest.raises(IOError):
        read_hashes_and_filenames(non_existent_file)


def test_save_and_read_hash_file_integration(temp_files):
    _, _, hash_file = temp_files

    save_hashes_and_filenames(hash_file, FHASH_DICT)
    loaded_fhashes = read_hashes_and_filenames(hash_file)

    assert loaded_fhashes == FHASH_DICT
