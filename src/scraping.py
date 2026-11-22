import requests
from bs4 import BeautifulSoup
import re


def extraer_datos_ktronix(url: str) -> dict:

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "es-CO,es;q=0.9,en;q=0.8"
    }

    response = requests.get(url, headers=headers, timeout=15)

    if response.status_code != 200:
        raise Exception(
            f"Error al cargar la página. "
            f"Código de estado: {response.status_code}"
        )

    soup = BeautifulSoup(response.text, "html.parser")

    # Nombre del producto
    titulo_tag = soup.find("h1", class_="js-main-title")

    nombre = (
        titulo_tag.get_text(strip=True)
        if titulo_tag
        else "No disponible"
    )

    # SKU / código EAN
    sku_tag = soup.find("span", class_="js-ean-pdp")

    sku = (
        sku_tag.get_text(strip=True)
        if sku_tag
        else "No disponible"
    )

    # Precio actual
    precio_tag = soup.find(id="js-original_price")

    precio_actual = "No disponible"

    if precio_tag:

        etiqueta_hoy = precio_tag.find(
            class_="font-title--product-price__today"
        )

        if etiqueta_hoy:
            etiqueta_hoy.decompose()

        precio_actual = precio_tag.get_text(strip=True)

    # Precio base
    precio_base_tag = soup.find(
        class_="before-price__basePrice"
    )

    precio_base = (
        precio_base_tag.get_text(strip=True)
        if precio_base_tag
        else precio_actual
    )

    # Disponibilidad
    disponibilidad = (
        "Disponible"
        if precio_actual != "No disponible"
        else "No disponible"
    )

    # Especificaciones técnicas
    especificaciones = {}

    items_specs = soup.find_all(
        class_="new-container__table__classifications___type__item"
    )

    for item in items_specs:

        caracteristica = item.find(
            class_="new-container__table__classifications___type__item_feature"
        )

        valor = item.find(
            class_="new-container__table__classifications___type__item_result"
        )

        if caracteristica and valor:

            clave = caracteristica.get_text(strip=True)

            resultado = re.sub(
                r"\s+",
                " ",
                valor.get_text(strip=True)
            )

            if clave and resultado:
                especificaciones[clave] = resultado

    return {
        "tienda": "Ktronix",
        "url": url,
        "nombre": nombre,
        "sku": sku,
        "precio_actual": precio_actual,
        "precio_base": precio_base,
        "disponibilidad": disponibilidad,
        "especificaciones": especificaciones
    }


def extraer_datos_alkosto(url: str) -> dict:

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "es-CO,es;q=0.9,en;q=0.8"
    }

    response = requests.get(url, headers=headers, timeout=15)

    if response.status_code != 200:
        raise Exception(
            f"Error al cargar Alkosto. "
            f"Código de estado: {response.status_code}"
        )

    soup = BeautifulSoup(response.text, "html.parser")

    # Nombre del producto
    titulo_tag = soup.find(
        "h1",
        class_="js-main-title"
    )

    nombre = (
        titulo_tag.get_text(strip=True)
        if titulo_tag
        else "No disponible"
    )

    # SKU
    sku_tag = soup.find(
        "span",
        class_="js-ean-pdp"
    )

    sku = (
        sku_tag.get_text(strip=True)
        if sku_tag
        else "No disponible"
    )

    # Precio actual
    precio_tag = soup.find(
        id="js-original_price"
    )

    precio_actual = "No disponible"

    if precio_tag:

        etiqueta_hoy = precio_tag.find(
            class_="font-title--product-price__today"
        )

        if etiqueta_hoy:
            etiqueta_hoy.decompose()

        precio_actual = precio_tag.get_text(
            strip=True
        )

    # Disponibilidad
    disponibilidad = (
        "Disponible"
        if precio_actual != "No disponible"
        else "No disponible"
    )

    # Especificaciones técnicas
    especificaciones = {}

    items_specs = soup.find_all(
        class_="new-container__table__classifications___type__item"
    )

    for item in items_specs:

        caracteristica = item.find(
            class_="new-container__table__classifications___type__item_feature"
        )

        valor = item.find(
            class_="new-container__table__classifications___type__item_result"
        )

        if caracteristica and valor:

            clave = caracteristica.get_text(
                strip=True
            )

            resultado = re.sub(
                r"\s+",
                " ",
                valor.get_text(strip=True)
            )

            if clave and resultado:
                especificaciones[clave] = resultado

    return {
        "tienda": "Alkosto",
        "url": url,
        "nombre": nombre,
        "sku": sku,
        "precio_actual": precio_actual,
        "disponibilidad": disponibilidad,
        "especificaciones": especificaciones
    }


def extraer_datos_falabella(url: str) -> dict:

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "es-CO,es;q=0.9,en;q=0.8"
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=15
    )

    if response.status_code != 200:
        raise Exception(
            f"Error al cargar Falabella. "
            f"Código de estado: {response.status_code}"
        )

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    # Nombre del producto
    titulo_tag = soup.find("h1")

    nombre = (
        titulo_tag.get_text(strip=True)
        if titulo_tag
        else "No disponible"
    )

    # Código obtenido desde la URL
    match_codigo = re.search(
        r"/product/(\d+)",
        url
    )

    codigo = (
        match_codigo.group(1)
        if match_codigo
        else "No disponible"
    )

    # Precio actual
    precio_actual = "No disponible"

    texto_pagina = soup.get_text(
        " ",
        strip=True
    )

    match_precio = re.search(
        r"\$\s*([\d\.]+)",
        texto_pagina
    )

    if match_precio:
        precio_actual = (
            "$" + match_precio.group(1)
        )

    # Disponibilidad
    disponibilidad = (
        "Disponible"
        if precio_actual != "No disponible"
        else "No disponible"
    )

    # Especificaciones técnicas
    especificaciones = {}

    tablas = soup.find_all("table")

    for tabla in tablas:

        filas = tabla.find_all("tr")

        for fila in filas:

            columnas = fila.find_all(
                ["th", "td"]
            )

            if len(columnas) >= 2:

                caracteristica = columnas[0].get_text(
                    " ",
                    strip=True
                )

                valor = columnas[1].get_text(
                    " ",
                    strip=True
                )

                if caracteristica and valor:
                    especificaciones[caracteristica] = valor

    return {
        "tienda": "Falabella",
        "url": url,
        "nombre": nombre,
        "sku": codigo,
        "precio_actual": precio_actual,
        "disponibilidad": disponibilidad,
        "especificaciones": especificaciones
    }