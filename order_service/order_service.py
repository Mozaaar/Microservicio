from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
import requests

app = FastAPI()

# Montar templates para interfaz web
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("interfaz.html", {"request": request})

@app.post("/order/{product_id}")
def create_order(product_id: int):
    # Obtener el producto desde el microservicio de productos
    res = requests.get("http://localhost:8000/products")
    products = res.json()

    product = next((p for p in products if p["id"] == product_id), None)

    if product:
        return {
            "message": "Pedido realizado",
            "product": product
        }
    return {"error": "Producto no encontrado"}
