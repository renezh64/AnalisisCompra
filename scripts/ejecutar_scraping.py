from src.scraping import extraer_datos_alkosto
from src.procesamiento import limpiar_precio
from src.config import URL_KTRONIX


datos = URL_KTRONIX

precio_numerico = limpiar_precio(
    datos["precio_actual"]
)

print("\n--- DATOS KTRONIX ---")

print("Tienda:", datos["tienda"])
print("Producto:", datos["nombre"])
print("SKU:", datos["sku"])
print("Precio original:", datos["precio_actual"])
print("Precio numérico:", precio_numerico)
print("Disponibilidad:", datos["disponibilidad"])