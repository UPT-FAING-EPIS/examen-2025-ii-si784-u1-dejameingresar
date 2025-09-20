from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db
router = APIRouter()
@router.get("/", response_model=list[schemas.Product])
def list_products(skip: int = 0, limit: int = 100, q: str | None = Query(None), category: str | None = Query(None), db: Session = Depends(get_db)):
    products = crud.get_products(db, skip=skip, limit=limit)
    if q:
        products = [p for p in products if q.lower() in p.name.lower()]
    if category:
        products = [p for p in products if p.category == category]
    return products
@router.get("/{product_id}", response_model=schemas.Product)
def get_product(product_id: int, db: Session = Depends(get_db)):
    p = crud.get_product(db, product_id)
    if not p:
        raise HTTPException(status_code=404, detail="Product not found")
    return p
@router.post("/", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)
@router.put("/{product_id}", response_model=schemas.Product)
def update_product(product_id: int, product: schemas.ProductCreate, db: Session = Depends(get_db)):
    updated = crud.update_product(db, product_id, product.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated
@router.delete("/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    ok = crud.delete_product(db, product_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"ok": True}
