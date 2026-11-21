import re


def limpiar_precio(precio: str):
    """
    Convierte un precio en formato texto a un número entero.

    Ejemplo:
    $999.010 -> 999010
    """

    if not precio or precio == "No disponible":
        return None

    precio_limpio = re.sub(r"[^\d]", "", precio)

    if not precio_limpio:
        return None

    return int(precio_limpio)