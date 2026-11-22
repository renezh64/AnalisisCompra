from src.procesamiento import comparar_productos


productos = [
    {
        "tienda": "Ktronix",
        "nombre": "AirPods Pro 3",
        "precio_actual": "$999.010",
        "disponibilidad": "Disponible"
    },
    {
        "tienda": "Alkosto",
        "nombre": "AirPods 5",
        "precio_actual": "$569.000",
        "disponibilidad": "Disponible"
    },
    {
        "tienda": "Falabella",
        "nombre": "AirPods 5",
        "precio_actual": "$569.900",
        "disponibilidad": "Disponible"
    }
]

resultado = comparar_productos(productos)

print("\n--- COMPARACIÓN DE PRODUCTOS ---")

for producto in resultado:

    print(
        producto["tienda"],
        "-",
        producto["nombre"],
        "- $",
        f'{producto["precio_numerico"]:,}'
    )