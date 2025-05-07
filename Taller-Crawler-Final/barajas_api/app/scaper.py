# app/scraper.py
from bs4 import BeautifulSoup
import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}
URL = "https://magichouse.com.co/categoria-producto/cartas-barajas/barajas-coleccion/barajas-theory-11/"

def obtener_barajas():
    response = requests.get(URL, headers=HEADERS)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    productos = soup.find_all("li", class_="product")

    barajas = []

    for producto in productos:
        titulo_tag = producto.find("h2", class_="woocommerce-loop-product__title")
        precio_tag = producto.find("span", class_="woocommerce-Price-amount")
        imagen_tag = producto.find("img")

        titulo = titulo_tag.text.strip() if titulo_tag else "Sin título"
        precio_formateado = precio_tag.text.strip() if precio_tag else "$0"

        # Ejemplo: "$69.000,00" → "69000.00"
        precio_numerico = precio_formateado.replace("$", "").replace(".", "").replace(",", ".")

        try:
            precio_float = float(precio_numerico)
        except ValueError:
            precio_float = 0.0

        imagen = imagen_tag.get("data-src") or imagen_tag.get("src") if imagen_tag else None

        barajas.append({
            "titulo": titulo,
            "precio": precio_formateado,
            "precio_float": precio_float,
            "imagen_url": imagen
        })

    return barajas
