import re


def limpiar_precio(precio: str):
    """
    Convierte un precio en formato texto a número entero.

    Ejemplo:
    $999.010 -> 999010
    """

    if not precio or precio == "No disponible":
        return None

    precio_limpio = re.sub(r"[^\d]", "", precio)

    if not precio_limpio:
        return None

    return int(precio_limpio)


def comparar_productos(productos: list) -> list:
    """
    Recibe una lista de productos y los ordena
    de menor a mayor precio.
    """

    productos_procesados = []

    for producto in productos:

        producto_procesado = producto.copy()

        producto_procesado["precio_numerico"] = limpiar_precio(
            producto["precio_actual"]
        )

        productos_procesados.append(producto_procesado)

    productos_disponibles = [
        producto
        for producto in productos_procesados
        if producto["precio_numerico"] is not None
    ]

    productos_ordenados = sorted(
        productos_disponibles,
        key=lambda producto: producto["precio_numerico"]
    )

    return productos_ordenados