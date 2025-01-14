from .confighandling import get_config

# Variable global con los valores del fichero de configuración
cfg = get_config()

__all__ = ["cfg"]
