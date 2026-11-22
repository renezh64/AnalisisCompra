from src.scraping import (
    extraer_datos_ktronix,
    extraer_datos_alkosto,
    extraer_datos_falabella
)

from src.procesamiento import calcular_costo_beneficio

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


resultado = calcular_costo_beneficio(productos)


print("\n--- ANÁLISIS COSTO-BENEFICIO ---")

for posicion, producto in enumerate(resultado, start=1):

    print(f"\n{posicion}. {producto['tienda']}")

    print(
        f"Producto: {producto['nombre']}"
    )

    print(
        f"Precio: ${producto['precio']:,}"
    )

    print(
        f"Modelo: {producto['modelo']}"
    )

    print(
        f"Autonomía: {producto['autonomia']}"
    )

    print(
        f"Cancelación de ruido: "
        f"{producto['cancelacion_ruido']}"
    )

    print(
        f"Resistencia al agua: "
        f"{producto['resistencia_agua']}"
    )

    print(
        f"Puntaje costo-beneficio: "
        f"{producto['puntaje']}/100"
    )


if resultado:

    mejor_producto = resultado[0]

    print("\n--- MEJOR COSTO-BENEFICIO ---")

    print(
        f"Tienda: {mejor_producto['tienda']}"
    )

    print(
        f"Producto: {mejor_producto['nombre']}"
    )

    print(
        f"Puntaje: {mejor_producto['puntaje']}/100"
    )