from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db
from ..deps import get_current_user
router = APIRouter()
@router.post("/", response_model=schemas.CartItem)
def add_to_cart(item: schemas.CartItemCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return crud.add_cart_item(db, user.id, item)
@router.get("/", response_model=list[schemas.CartItem])
def get_cart(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return crud.get_cart(db, user.id)
