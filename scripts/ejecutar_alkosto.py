from src.scraping import extraer_datos_alkosto
from src.procesamiento import limpiar_precio


url = "https://www.alkosto.com/audifonos-apple-airpods-5-con-cancelacion-activa-ruido/p/195951378886"

datos = extraer_datos_alkosto(url)

precio_numerico = limpiar_precio(datos["precio_actual"])

print("\n--- DATOS ALKOSTO ---")

print("Tienda:", datos["tienda"])
print("Producto:", datos["nombre"])
print("SKU:", datos["sku"])
print("Precio original:", datos["precio_actual"])
print("Precio numérico:", precio_numerico)
print("Disponibilidad:", datos["disponibilidad"])

print("\nEspecificaciones:")

for caracteristica, valor in datos["especificaciones"].items():
    print(f"{caracteristica}: {valor}")