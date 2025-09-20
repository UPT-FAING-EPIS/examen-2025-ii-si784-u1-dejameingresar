from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from ..database import get_db

router = APIRouter()

@router.post("/")
def add_to_cart(item: schemas.CartItemCreate, user_id: int = 1, db: Session = Depends(get_db)):
    # user_id is placeholder; integrate auth to get actual user
    return crud.add_cart_item(db, user_id, item)

@router.get("/")
def get_cart(user_id: int = 1, db: Session = Depends(get_db)):
    return crud.get_cart(db, user_id)
