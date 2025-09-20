from fastapi import FastAPI
from .database import engine, Base
from .routers import auth, products, cart, orders
# create tables if alembic not used yet
Base.metadata.create_all(bind=engine)
app = FastAPI(title="Ecommerce API - Full")
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(products.router, prefix="/api/products", tags=["products"])
app.include_router(cart.router, prefix="/api/cart", tags=["cart"])
app.include_router(orders.router, prefix="/api/orders", tags=["orders"])
@app.get("/api/")
def read_root():
    return {"message": "Ecommerce API - FastAPI (full backend)"}
