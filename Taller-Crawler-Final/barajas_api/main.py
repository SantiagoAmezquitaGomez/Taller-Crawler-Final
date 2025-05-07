# main.py
from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="API de Barajas Theory11",
    description="API que devuelve barajas de MagicHouse y permite filtrarlas por precio",
    version="1.0"
)

app.include_router(router)
