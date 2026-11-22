from src.procesamiento import limpiar_precio, comparar_productos


def test_limpiar_precio():
    resultado = limpiar_precio("$999.010")
    assert resultado == 999010


def test_limpiar_precio_millon():
    resultado = limpiar_precio("$1.299.900")
    assert resultado == 1299900


def test_precio_no_disponible():
    resultado = limpiar_precio("No disponible")
    assert resultado is None


def test_comparar_productos():

    productos = [
        {
            "tienda": "Ktronix",
            "precio_actual": "$999.010"
        },
        {
            "tienda": "Alkosto",
            "precio_actual": "$569.000"
        },
        {
            "tienda": "Falabella",
            "precio_actual": "$569.900"
        }
    ]

    resultado = comparar_productos(productos)

    assert resultado[0]["tienda"] == "Alkosto"
    assert resultado[1]["tienda"] == "Falabella"
    assert resultado[2]["tienda"] == "Ktronix"

    assert resultado[0]["precio_numerico"] == 569000