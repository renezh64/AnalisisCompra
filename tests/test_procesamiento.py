from src.procesamiento import (
    limpiar_precio,
    comparar_productos,
    normalizar_caracteristicas
)


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

def test_normalizar_caracteristicas():

    producto = {
        "tienda": "Ktronix",
        "nombre": "AirPods Pro 3",
        "precio_actual": "$999.010",
        "especificaciones": {
            "Linea Modelo Referencia": "AirPods Pro 3",
            "Opciones de Conectividad": "Bluetooth",
            "Duracion de la Bateria": "8 Horas Aproximadas",
            "Resistencia al Agua": "Resistencia al Agua (IP57)",
            "Tipo de Audifonos": "Cancelación de Ruido In Ear"
        }
    }

    resultado = normalizar_caracteristicas(producto)

    assert resultado["precio"] == 999010
    assert resultado["modelo"] == "AirPods Pro 3"
    assert resultado["conectividad"] == "Bluetooth"
    assert resultado["autonomia"] == "8 Horas Aproximadas"
    assert resultado["resistencia_agua"] == "Resistencia al Agua (IP57)"
    assert resultado["cancelacion_ruido"] == "Sí"
    