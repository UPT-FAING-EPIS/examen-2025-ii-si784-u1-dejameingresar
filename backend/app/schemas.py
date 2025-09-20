from pydantic import BaseModel
from typing import Optional, List
class UserCreate(BaseModel):
    username: str
    password: str
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
class ProductBase(BaseModel):
    name: str
    description: Optional[str] = ""
    price: float
    stock: int
    category: Optional[str] = None
class ProductCreate(ProductBase):
    pass
class Product(ProductBase):
    id: int
    class Config:
        orm_mode = True
class CartItemCreate(BaseModel):
    product_id: int
    quantity: int
class CartItem(BaseModel):
    id: int
    user_id: int
    product_id: int
    quantity: int
    class Config:
        orm_mode = True
class OrderCreate(BaseModel):
    items: List[CartItemCreate]
class Order(BaseModel):
    id: int
    user_id: int
    status: str
    class Config:
        orm_mode = True
