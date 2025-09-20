from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db
from ..deps import get_current_user
router = APIRouter()
@router.post("/", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return crud.create_order(db, user.id, order)
@router.get("/me", response_model=list[schemas.Order])
def list_my_orders(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return crud.get_orders_by_user(db, user.id)
