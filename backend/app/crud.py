from sqlalchemy.orm import Session
from . import models, schemas
from .security import get_password_hash
def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()
def create_user(db: Session, user: schemas.UserCreate):
    hashed = get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()
def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()
def create_product(db: Session, product: schemas.ProductCreate):
    db_obj = models.Product(**product.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
def update_product(db: Session, product_id: int, data: dict):
    p = get_product(db, product_id)
    if not p:
        return None
    for k, v in data.items():
        setattr(p, k, v)
    db.add(p)
    db.commit()
    db.refresh(p)
    return p
def delete_product(db: Session, product_id: int):
    p = get_product(db, product_id)
    if not p:
        return False
    db.delete(p)
    db.commit()
    return True
def add_cart_item(db: Session, user_id: int, item: schemas.CartItemCreate):
    ci = models.CartItem(user_id=user_id, product_id=item.product_id, quantity=item.quantity)
    db.add(ci)
    db.commit()
    db.refresh(ci)
    return ci
def get_cart(db: Session, user_id: int):
    return db.query(models.CartItem).filter(models.CartItem.user_id == user_id).all()
def clear_cart(db: Session, user_id: int):
    db.query(models.CartItem).filter(models.CartItem.user_id == user_id).delete()
    db.commit()
def create_order(db: Session, user_id: int, order: schemas.OrderCreate):
    ord_obj = models.Order(user_id=user_id)
    db.add(ord_obj)
    db.flush()
    for it in order.items:
        prod = get_product(db, it.product_id)
        price = prod.price if prod else 0.0
        oi = models.OrderItem(order_id=ord_obj.id, product_id=it.product_id, quantity=it.quantity, price=price)
        db.add(oi)
    db.commit()
    db.refresh(ord_obj)
    clear_cart(db, user_id)
    return ord_obj
def get_orders_by_user(db: Session, user_id: int):
    return db.query(models.Order).filter(models.Order.user_id == user_id).all()
