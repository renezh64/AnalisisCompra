from src.procesamiento import limpiar_precio


def test_limpiar_precio():
    resultado = limpiar_precio("$999.010")
    assert resultado == 999010


def test_limpiar_precio_millon():
    resultado = limpiar_precio("$1.299.900")
    assert resultado == 1299900


def test_precio_no_disponible():
    resultado = limpiar_precio("No disponible")
    assert resultado is None