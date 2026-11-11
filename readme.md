# Análisis de productos para mejor compra

Proyecto en cuadernos Jupyter para encontrar la mejor alternativa de compra de un producto. La primera etapa extrae, mediante web scraping, la información de un producto publicado en la tienda en línea **Ktronix**.

## Autores

- Rene Zapata Hernandez
- Camilo Andres Mendez Cogollo
- Estid Esteban Vásquez

## Estructura del proyecto

| Archivo | Descripción |
|---|---|
| `AnalisisInformeProducto.ipynb` | Web scraping de la página del producto en Ktronix con `requests` y `BeautifulSoup`. Genera `producto_ktronix.json` y un DataFrame de resumen. |
| `AnalisisInformeProducto.ipynb` | Cuaderno de análisis e informe para elegir la mejor alternativa de producto. |
| `requirements.txt` | Librerías de Python requeridas. |

## Extracción de datos (web scraping)

- **Comercio:** Ktronix
- **Producto:** iPhone Duo 2TB 5G Blanco Estrella
- **URL:** https://www.ktronix.com/iphone-duo-2tb-5g-blanco-estrella/p/195951407074

### Pasos del cuaderno `AnalisisInformeProducto.ipynb`

1. **Instalación de librerías:** `pip install requests beautifulsoup4`.
2. **Prueba de conexión:** hace una petición HTTP con un `User-Agent` de navegador, verifica que el código de respuesta sea `200` e imprime el título de la página.
3. **Extracción de datos:** la función `extraer_datos_producto(url)` descarga el HTML, lo procesa con BeautifulSoup y obtiene los campos de la tabla siguiente. Si la respuesta no es `200`, lanza una excepción.
4. **Guardado:** la función `guardar_archivos(datos)` escribe los datos en `producto_ktronix.json` (UTF-8, con indentación).
5. **Visualización:** construye un DataFrame de pandas (`df_producto`) con los datos principales.

### Campos extraídos

| Campo | Origen en el HTML |
|---|---|
| `nombre` | `<h1 class="js-main-title">` |
| `sku` | `<span class="js-ean-pdp">` (código EAN) |
| `precio_actual` | Elemento con `id="js-original_price"`, sin la etiqueta "Hoy" |
| `precio_base` | Elemento con clase `before-price__basePrice`. Si no existe, se usa el precio actual |
| `moneda` | `<meta itemprop="priceCurrency">` (Schema.org). Valor por defecto: `COP` |
| `categorias` | Enlaces del breadcrumb, unidos con ` > ` |
| `imagen_url` | Primera `<img>` cuya ruta contiene `products` y el SKU |
| `descripcion` | Campo `description` del script `richSnippet(...)` |
| `especificaciones_principales` | Tabla de características técnicas (`new-container__table__classifications___type__item`) |

Los campos que no se encuentran en la página quedan con el valor `"No disponible"`.

### Resultado de la ejecución

| Campo | Valor |
|---|---|
| Producto | iPhone Duo 2TB 5G Blanco Estrella |
| SKU / Código | 195951407074 |
| Precio Actual | $14.549.010 COP |
| Categorías | Inicio > Ver Celulares > Ver Smartphones > Ver Celulares iPhone |
| Total Specs | 33 especificaciones técnicas |

Estos valores corresponden a la ejecución guardada en el cuaderno. El precio y las especificaciones pueden cambiar si la página de Ktronix se actualiza.

## Requisitos

Python 3 y las librerías de `requirements.txt`:

```bash
pip install pandas numpy requests beautifulsoup4 matplotlib seaborn papermill jupyter nbconvert
```

## Ejecución

1. Abrir `AnalisisInformeProducto.ipynb` en Jupyter o Google Colab.
2. Ejecutar las celdas en orden. Se necesita conexión a internet.
3. Revisar el archivo `producto_ktronix.json` generado en el directorio de trabajo y el DataFrame `df_producto` al final del cuaderno.
