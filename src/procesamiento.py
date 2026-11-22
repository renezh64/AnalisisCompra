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

def normalizar_caracteristicas(producto: dict) -> dict:
    """
    Convierte las especificaciones de diferentes tiendas
    a una estructura común para facilitar la comparación.
    """

    especificaciones = producto.get("especificaciones", {})

    datos = {
        "tienda": producto.get("tienda"),
        "nombre": producto.get("nombre"),
        "precio": limpiar_precio(
            producto.get("precio_actual")
        ),
        "modelo": "No disponible",
        "conectividad": "No disponible",
        "autonomia": "No disponible",
        "resistencia_agua": "No disponible",
        "cancelacion_ruido": "No disponible"
    }

    for clave, valor in especificaciones.items():

        clave_normalizada = clave.lower()

        # Modelo
        if (
            "modelo" in clave_normalizada
            or "referencia de los audífonos" in clave_normalizada
        ):
            datos["modelo"] = valor

        # Conectividad
        if (
            "conectividad" in clave_normalizada
            or clave_normalizada == "conexión"
        ):
            datos["conectividad"] = valor

        # Batería / autonomía
        if (
            "bateria" in clave_normalizada
            or "batería" in clave_normalizada
            or "autonomía" in clave_normalizada
        ):
            datos["autonomia"] = valor

        # Resistencia al agua
        if "resistencia al agua" in clave_normalizada:
            datos["resistencia_agua"] = valor

        # Cancelación de ruido
        if (
            "tipo de audifonos" in clave_normalizada
            or "tipo de audífonos" in clave_normalizada
        ):
            if "ruido" in valor.lower():
                datos["cancelacion_ruido"] = "Sí"

    return datos