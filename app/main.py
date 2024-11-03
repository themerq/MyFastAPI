from fastapi import FastAPI
from app.myModels.router import router as router_products
from app.myModels.router import router_ii as router_orders


app = FastAPI()

@app.get("/", summary="Главная")
def home_page():
    return {"message": "Добро пожаловать!"}


app.include_router(router_products)
app.include_router(router_orders)