from src.scraping import extraer_datos_ktronix
from src.procesamiento import limpiar_precio
#URL del producto a extraer (se debe cambiar por la URL del producto que se desea extraer :D)
url = "https://www.ktronix.com/audifonos-apple-airpods-pro-3-estuche-magsafe-usb-c-blanco/p/195950543612"

datos = extraer_datos_producto(url)
precio_numerico = limpiar_precio(datos["precio_actual"])

print("Tienda:", datos["tienda"])
print("Producto:", datos["nombre"])
print("Precio:", datos["precio_actual"])
print("Disponibilidad:", datos["disponibilidad"])
print("SKU:", datos["sku"])
print("precio númerico:", precio_numerico)

print("\nEspecificaciones:")

for caracteristica, valor in datos["especificaciones"].items():
    print(f"{caracteristica}: {valor}")