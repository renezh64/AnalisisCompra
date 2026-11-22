import re


def limpiar_precio(precio: str):
    """
    Convierte un precio en formato texto a número entero.

    Ejemplo:
    $999.010 -> 999010
    """

    if not preciou or preciou == "No disponible":
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


def extraer_horas_autonomia(texto: str):
    """
    Obtiene la cantidad de horas mencionada
    en el texto de autonomía.
    """

    if not texto or texto == "No disponible":
        return None

    match = re.search(r"(\d+)", texto)

    if not match:
        return None

    return int(match.group(1))

def calcular_costo_beneficio(productos: list) -> list:
    """
    Calcula un puntaje de costo-beneficio para cada producto.

    Ponderaciones:
    - Precio: 40 %
    - Autonomía: 25 %
    - Cancelación de ruido: 20 %
    - Resistencia al agua: 15 %

    Retorna los productos ordenados de mayor a menor puntaje.
    """

    productos_normalizados = [
        normalizar_caracteristicas(producto)
        for producto in productos
    ]

    precios = [
        producto["precio"]
        for producto in productos_normalizados
        if producto["precio"] is not None
    ]

    autonomias = [
        extraer_horas_autonomia(producto["autonomia"])
        for producto in productos_normalizados
    ]

    autonomias_validas = [
        autonomia
        for autonomia in autonomias
        if autonomia is not None
    ]

    if not precios:
        return []

    precio_minimo = min(precios)

    autonomia_maxima = (
        max(autonomias_validas)
        if autonomias_validas
        else 0
    )

    resultados = []

    for producto in productos_normalizados:

        precio = producto["precio"]

        autonomia = extraer_horas_autonomia(
            producto["autonomia"]
        )

        # Precio: menor precio obtiene mejor puntuación
        puntaje_precio = 0

        if precio:
            puntaje_precio = (
                precio_minimo / precio
            ) * 40

        # Autonomía: mayor autonomía obtiene mejor puntuación
        puntaje_autonomia = 0

        if autonomia and autonomia_maxima > 0:
            puntaje_autonomia = (
                autonomia / autonomia_maxima
            ) * 25

        # Cancelación de ruido
        puntaje_cancelacion = (
            20
            if producto["cancelacion_ruido"] == "Sí"
            else 0
        )

        # Resistencia al agua
        puntaje_resistencia = (
            15
            if producto["resistencia_agua"] != "No disponible"
            else 0
        )

        puntaje_total = (
            puntaje_precio
            + puntaje_autonomia
            + puntaje_cancelacion
            + puntaje_resistencia
        )

        producto_resultado = producto.copy()

        producto_resultado["puntaje"] = round(
            puntaje_total,
            2
        )

        resultados.append(producto_resultado)

    return sorted(
        resultados,
        key=lambda producto: producto["puntaje"],
        reverse=True
    )