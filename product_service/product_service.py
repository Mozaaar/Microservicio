from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Habilitar CORS para permitir peticiones del frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # o ["http://localhost:8001"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Datos simulados
products = [
    {"id": 1, "name": "Laptop", "price": 1000},
    {"id": 2, "name": "Mouse", "price": 25},
    {"id": 3, "name": "Teclado", "price": 45},
    {"id": 4, "name": "Monitor", "price": 300},
    {"id": 5, "name": "Impresora", "price": 150},
    {"id": 6, "name": "Escáner", "price": 200},
    {"id": 7, "name": "Proyector", "price": 500},
    {"id": 8, "name": "Altavoces", "price": 100},
    {"id": 9, "name": "Webcam", "price": 75},
    {"id": 10, "name": "Auriculares", "price": 50},
    {"id": 11, "name": "Microfono", "price": 80},
    {"id": 12, "name": "Router", "price": 120},
    {"id": 13, "name": "Switch", "price": 90},
    {"id": 14, "name": "Cable HDMI", "price": 15},
    {"id": 15, "name": "Cable USB", "price": 10},
    {"id": 16, "name": "Disco Duro Externo", "price": 200},
    {"id": 17, "name": "Pendrive", "price": 20},
    {"id": 18, "name": "Tarjeta de Video", "price": 400},
    {"id": 19, "name": "Placa Base", "price": 150},
    {"id": 20, "name": "Fuente de Poder", "price": 100} 
]

@app.get("/products")
def get_products():
    return products
