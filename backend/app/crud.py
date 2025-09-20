from sqlalchemy.orm import Session
from . import models, schemas

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

def add_cart_item(db: Session, user_id: int, item: schemas.CartItemCreate):
    ci = models.CartItem(user_id=user_id, product_id=item.product_id, quantity=item.quantity)
    db.add(ci)
    db.commit()
    db.refresh(ci)
    return ci

def get_cart(db: Session, user_id: int):
    return db.query(models.CartItem).filter(models.CartItem.user_id == user_id).all()

def create_order(db: Session, order: schemas.OrderCreate):
    ord_obj = models.Order(user_id=order.user_id)
    db.add(ord_obj)
    db.flush()
    for it in order.items:
        oi = models.OrderItem(order_id=ord_obj.id, product_id=it.product_id, quantity=it.quantity, price=0.0)
        db.add(oi)
    db.commit()
    db.refresh(ord_obj)
    return ord_obj

def get_orders_by_user(db: Session, user_id: int):
    return db.query(models.Order).filter(models.Order.user_id == user_id).all()
