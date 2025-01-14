import tomli
from pathlib import Path

# Constantes para los posibles caminos del fichero de configuración
CONFIG_PATHS = {
    "script": Path(__file__).parent / "config.toml",
    "exe": Path.cwd() / "config/config.toml",
}


def load_config(file_path: Path) -> dict:
    if not file_path.exists():
        raise FileNotFoundError(f"No se encuentra el fichero de configuración: {file_path}")

    try:
        with file_path.open(mode="rb") as fp:
            return tomli.load(fp)
    except tomli.TOMLDecodeError as e:
        raise ValueError(f"Error al analizar el archivo de configuración {file_path}: {e}") from e


def get_config() -> dict:
    for env, path in CONFIG_PATHS.items():
        if path.exists():
            return load_config(path)

    raise FileNotFoundError(
        "No se encuentra el fichero de configuración (config.toml). "
        "Debería estar en la subcarpeta 'config'."
    )
