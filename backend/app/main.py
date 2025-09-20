from fastapi import FastAPI
from .routers import products, auth, cart, orders
from .database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Ecommerce API")

app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(products.router, prefix="/api/products", tags=["products"])
app.include_router(cart.router, prefix="/api/cart", tags=["cart"])
app.include_router(orders.router, prefix="/api/orders", tags=["orders"])

@app.get("/")
def read_root():
    return {"message": "Ecommerce API - FastAPI"}
