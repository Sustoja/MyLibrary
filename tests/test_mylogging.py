from pathlib import Path
from src.MyLogging import logger, LOG_FILE_NAME



def test_reset_log_file_no_limit():
    logger.reset_log_file()
    assert logger.log_path.read_text() == ""


def test_reset_log_file_with_limit():
    logger.reset_log_file(limit=10)
    assert logger.log_path.read_text() == ""

    # Rellenar el archivo nuevamente
    logger.log_path.write_text("Nuevo contenido.")

    # Archivo no supera el límite
    logger.reset_log_file(limit=50)
    assert logger.log_path.read_text() == "Nuevo contenido."


def test_log_path_property():
    assert logger.log_path == Path(LOG_FILE_NAME).absolute()


def test_log_size_property():
    assert logger.log_size == len(Path(LOG_FILE_NAME).read_text())


def test_file_filter_removes_colors():
    logger.log.error("\033[91mMensaje con color.\033[97m")
    log_contents = logger.log_path.read_text()
    assert "\033" not in log_contents
    assert "Mensaje con color." in log_contents

def test_clean_temp_file():
    # Por último se borra el fichero de log que se ha generado durante las pruebas
    logger.log_path.unlink()
    assert not logger.log_path.exists()
