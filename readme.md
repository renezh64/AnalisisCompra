# Comparador de Audífonos con Web Scraping y DevOps

## Descripción

Este proyecto desarrolla una herramienta en Python y Jupyter Notebook para extraer, procesar y comparar información de audífonos disponibles en diferentes tiendas en línea.

La solución utiliza técnicas de web scraping para consultar información directamente desde:

- Ktronix
- Alkosto
- Falabella

Los datos obtenidos incluyen precio, disponibilidad y diferentes características técnicas de los productos.

Posteriormente, la información es procesada y normalizada para facilitar la comparación de productos, identificar las alternativas con menor precio y calcular un indicador de relación costo-beneficio.

El proyecto también implementa prácticas DevOps mediante Git, GitHub, pruebas automatizadas con Pytest y posteriormente un pipeline de CI/CD mediante GitHub Actions.

---

## Objetivo general

Desarrollar de manera colaborativa una herramienta en Jupyter Notebook para la extracción, procesamiento y comparación de información de audífonos disponibles en diferentes tiendas en línea, implementando prácticas DevOps mediante Git y GitHub para el control de versiones, así como un pipeline de integración y despliegue continuo (CI/CD) con GitHub Actions, que permita automatizar las pruebas del proyecto y mantener documentado el proceso de desarrollo.

---

## Objetivos específicos

- Desarrollar una herramienta de extracción y análisis de datos que permita consultar información de audífonos en al menos tres tiendas en línea.
- Recopilar datos relevantes como precio, características técnicas y disponibilidad.
- Procesar y comparar la información obtenida.
- Identificar diferencias entre productos y alternativas de compra.
- Implementar un modelo de análisis costo-beneficio.
- Utilizar Git para gestionar el historial de cambios.
- Gestionar el código fuente mediante GitHub.
- Utilizar un flujo de trabajo basado en commits e integración progresiva de funcionalidades.
- Implementar pruebas automatizadas con Pytest.
- Configurar un pipeline de CI/CD mediante GitHub Actions.
- Automatizar la validación del proyecto ante nuevos cambios.
- Documentar la arquitectura, funcionamiento y proceso de desarrollo de la solución.

---

## Tecnologías utilizadas

- Python
- Jupyter Notebook
- Requests
- BeautifulSoup
- Pandas
- Matplotlib
- Pytest
- Git
- GitHub
- GitHub Actions

---

## Estructura del proyecto

```text
AnalisisCompra/
│
├── notebooks/
│   └── analisis_audifonos.ipynb
│
├── scripts/
│   ├── ejecutar_scraping.py
│   ├── ejecutar_alkosto.py
│   ├── ejecutar_falabella.py
│   ├── probar_comparacion.py
│   ├── comparar_tiendas.py
│   └── analizar_costo_beneficio.py
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── scraping.py
│   └── procesamiento.py
│
├── tests/
│   └── test_procesamiento.py
│
├── requirements.txt
└── README.md
```

---

## Descripción de los componentes

### `src/config.py`

Centraliza las URL de los productos utilizados durante el análisis.

Esto permite modificar los productos o las páginas consultadas sin tener que cambiar las URL en diferentes scripts.

Ejemplo conceptual:

```python
URL_KTRONIX = "..."
URL_ALKOSTO = "..."
URL_FALABELLA = "..."
```

---

### `src/scraping.py`

Contiene la lógica relacionada con la extracción de información desde las tiendas.

Actualmente incluye funciones independientes para:

```python
extraer_datos_ktronix()
extraer_datos_alkosto()
extraer_datos_falabella()
```

Las funciones utilizan `requests` para obtener el código HTML de cada página y `BeautifulSoup` para encontrar la información relevante.

Entre los datos recopilados se encuentran:

- Nombre del producto.
- SKU o código.
- Precio.
- Disponibilidad.
- Especificaciones técnicas.
- URL de origen.

---

### `src/procesamiento.py`

Contiene las funciones encargadas de transformar y analizar los datos obtenidos mediante web scraping.

Entre sus responsabilidades se encuentran:

- Limpieza de precios.
- Conversión de precios a valores numéricos.
- Comparación de productos.
- Ordenamiento por precio.
- Normalización de características.
- Extracción de valores de autonomía.
- Análisis de costo-beneficio.

Por ejemplo:

```text
$569.000
   ↓
569000
```

Esto permite realizar cálculos y comparaciones utilizando los precios obtenidos.

---

## Scripts de ejecución

Los scripts fueron utilizados para desarrollar y validar progresivamente los diferentes componentes del proyecto.

### `scripts/ejecutar_scraping.py`

Ejecuta individualmente la extracción de información desde Ktronix.

Permite verificar que el scraper pueda obtener correctamente los datos del producto.

---

### `scripts/ejecutar_alkosto.py`

Ejecuta y valida la extracción de información desde Alkosto.

---

### `scripts/ejecutar_falabella.py`

Ejecuta y valida la extracción de información desde Falabella.

---

### `scripts/probar_comparacion.py`

Permite validar independientemente la lógica de comparación y ordenamiento de productos según su precio.

---

### `scripts/comparar_tiendas.py`

Integra los scrapers de las tres tiendas.

El flujo principal es:

```text
Ktronix ─────┐
Alkosto ─────┼──> Procesamiento ──> Comparación
Falabella ───┘
```

Los precios obtenidos directamente desde las páginas son transformados a valores numéricos y ordenados de menor a mayor.

---

### `scripts/analizar_costo_beneficio.py`

Ejecuta el análisis de costo-beneficio utilizando las características normalizadas de los productos.

El modelo implementado actualmente utiliza las siguientes ponderaciones:

| Criterio | Peso |
|---|---:|
| Precio | 40 % |
| Autonomía | 25 % |
| Cancelación de ruido | 20 % |
| Resistencia al agua | 15 % |
| **Total** | **100 %** |

El objetivo es complementar la comparación de precios con características técnicas relevantes.

---

## Jupyter Notebook

El análisis principal del proyecto se encuentra en:

```text
notebooks/analisis_audifonos.ipynb
```

El Notebook funciona como capa de análisis y presentación.

Incluye:

1. Descripción del proyecto.
2. Explicación de la arquitectura.
3. Extracción de información.
4. Construcción de DataFrames con Pandas.
5. Comparación de precios.
6. Normalización de características.
7. Análisis costo-beneficio.
8. Gráficos comparativos.
9. Identificación de alternativas.
10. Conclusiones.

La lógica principal no se encuentra duplicada dentro del Notebook. El Notebook reutiliza las funciones existentes en `src/`.

---

## Flujo de funcionamiento

El flujo general de la solución es:

```text
Configuración
      ↓
URLs de productos
      ↓
Web Scraping
      ↓
Ktronix / Alkosto / Falabella
      ↓
Extracción de datos
      ↓
Procesamiento y normalización
      ↓
Comparación de precios
      ↓
Análisis costo-beneficio
      ↓
Jupyter Notebook
      ↓
Tablas + gráficos + conclusiones
```

---

## Instalación

### 1. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

Acceder al proyecto:

```bash
cd AnalisisCompra
```

---

### 2. Crear un entorno virtual

En Windows:

```powershell
python -m venv .venv
```

Activarlo:

```powershell
.\.venv\Scripts\Activate.ps1
```

---

### 3. Instalar las dependencias

```powershell
python -m pip install -r requirements.txt
```

Las principales dependencias utilizadas son:

```text
requests
beautifulsoup4
pytest
pandas
jupyter
ipykernel
```

---

## Ejecución

### Probar Ktronix

```powershell
python -m scripts.ejecutar_scraping
```

### Probar Alkosto

```powershell
python -m scripts.ejecutar_alkosto
```

### Probar Falabella

```powershell
python -m scripts.ejecutar_falabella
```

### Comparar tiendas

```powershell
python -m scripts.comparar_tiendas
```

### Ejecutar análisis costo-beneficio

```powershell
python -m scripts.analizar_costo_beneficio
```

---

## Ejecución del Jupyter Notebook

El análisis completo puede ejecutarse desde:

```text
notebooks/analisis_audifonos.ipynb
```

Desde VS Code debe seleccionarse como Kernel el entorno virtual `.venv`.

También es posible iniciar Jupyter mediante:

```powershell
jupyter notebook
```

---

## Pruebas automatizadas

El proyecto utiliza `pytest` para verificar el comportamiento de los componentes de procesamiento.

Para ejecutar todas las pruebas:

```powershell
python -m pytest
```

Actualmente las pruebas verifican funcionalidades como:

- Limpieza de precios.
- Manejo de precios no disponibles.
- Comparación de productos.
- Ordenamiento por precio.
- Normalización de características.
- Procesamiento de autonomía.
- Cálculo de costo-beneficio.

Esto permite detectar errores antes de integrar nuevos cambios al proyecto.

---

## Control de versiones

El proyecto utiliza Git para registrar progresivamente los cambios realizados.

El desarrollo se ha dividido en pequeños incrementos funcionales, por ejemplo:

```text
Estructura inicial
        ↓
Scraper Ktronix
        ↓
Normalización de precios
        ↓
Pruebas automatizadas
        ↓
Scraper Alkosto
        ↓
Scraper Falabella
        ↓
Comparación de productos
        ↓
Normalización de características
        ↓
Costo-beneficio
        ↓
Jupyter Notebook
        ↓
CI/CD
```

Este enfoque permite mantener trazabilidad sobre la evolución de la solución.

---

## Estrategia de commits

Se utilizan mensajes descriptivos siguiendo una estructura similar a Conventional Commits:

```text
 nueva funcionalidad
pruebas automatizadas
reorganización del código
 documentación
 corrección de errores
 cambios relacionados con CI/CD
```


---

## Integración continua y CI/CD

El proyecto contempla la implementación de GitHub Actions para ejecutar automáticamente las pruebas.

El objetivo del pipeline es validar los cambios realizados mediante eventos como:

```text
Push
    ↓
GitHub Actions
    ↓
Instalación de Python
    ↓
Instalación de dependencias
    ↓
Pytest
    ↓
Validación
```

Esto permite identificar errores antes de integrar nuevas versiones del proyecto.

---

## Consideraciones

La información de precios y características es obtenida directamente desde las páginas de las tiendas y puede cambiar con el tiempo.

El funcionamiento del scraping también depende de la estructura HTML de cada sitio web. Si una tienda modifica su página, puede ser necesario actualizar los selectores definidos en `scraping.py`.

El análisis costo-beneficio corresponde a un modelo definido para este proyecto y depende de los criterios y ponderaciones establecidos.

---

## Estado actual

Actualmente el proyecto cuenta con:

- Extracción de información desde tres tiendas.
- Procesamiento de precios.
- Normalización de características.
- Comparación automática de productos.
- Análisis costo-beneficio.
- Pruebas automatizadas mediante Pytest.
- Jupyter Notebook para análisis y visualización.
- Control de versiones mediante Git.

La siguiente etapa corresponde a completar la automatización mediante GitHub Actions y documentar el flujo de CI/CD.