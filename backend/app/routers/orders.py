from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter()

@router.post("/")
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db, order)

@router.get("/user/{user_id}")
def list_orders(user_id: int, db: Session = Depends(get_db)):
    return crud.get_orders_by_user(db, user_id)
