from src.scraping import extraer_datos_falabella
from src.procesamiento import limpiar_precio
from src.config import URL_FALABELLA

url = URL_FALABELLA

datos = extraer_datos_falabella(url)

precio_numerico = limpiar_precio(datos["precio_actual"])

print("\n--- DATOS FALABELLA ---")

print("Tienda:", datos["tienda"])
print("Producto:", datos["nombre"])
print("SKU:", datos["sku"])
print("Precio original:", datos["precio_actual"])
print("Precio numérico:", precio_numerico)
print("Disponibilidad:", datos["disponibilidad"])
print("\nEspecificaciones:")

for caracteristica, valor in datos["especificaciones"].items():
    print(f"{caracteristica}: {valor}")