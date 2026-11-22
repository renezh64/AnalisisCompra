from src.scraping import (
    extraer_datos_ktronix,
    extraer_datos_alkosto,
    extraer_datos_falabella
)

from src.procesamiento import comparar_productos

from src.config import (
    URL_KTRONIX,
    URL_ALKOSTO,
    URL_FALABELLA
)


print("Extrayendo información de las tiendas...")

producto_ktronix = extraer_datos_ktronix(URL_KTRONIX)
producto_alkosto = extraer_datos_alkosto(URL_ALKOSTO)
producto_falabella = extraer_datos_falabella(URL_FALABELLA)


productos = [
    producto_ktronix,
    producto_alkosto,
    producto_falabella
]


resultado = comparar_productos(productos)


print("\n--- COMPARACIÓN DE PRODUCTOS ---")

for posicion, producto in enumerate(resultado, start=1):

    precio = producto["precio_numerico"]

    print(
        f"{posicion}. "
        f"{producto['tienda']} | "
        f"{producto['nombre']} | "
        f"${precio:,}"
    )


if resultado:

    mejor_precio = resultado[0]

    print("\n--- MENOR PRECIO ---")

    print("Tienda:", mejor_precio["tienda"])
    print("Producto:", mejor_precio["nombre"])
    print(
        "Precio:",
        f"${mejor_precio['precio_numerico']:,}"
    )