# app/routes.py
from fastapi import APIRouter
from app.scaper import obtener_barajas

router = APIRouter()

@router.get("/barajas-theory11", tags=["Barajas"])
def get_all_barajas():
    barajas = obtener_barajas()
    for b in barajas:
        b.pop("precio_float", None)
    return {"barajas": barajas}


@router.get("/barajas-theory11/precio/{valor}", tags=["Barajas"])
def get_barajas_por_precio(valor: float):
    barajas = obtener_barajas()

    filtradas = [
        {
            "titulo": b["titulo"],
            "precio": b["precio"],
            "imagen_url": b["imagen_url"]
        }
        for b in barajas if b["precio_float"] == valor
    ]

    return {
        "valor_buscado": f"${valor:,.0f}".replace(",", "."),
        "coincidencias": len(filtradas),
        "barajas": filtradas
    }

