from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True


class OrderBase(BaseModel):
    user_id: int
    product_id: int
    date_ordered: Optional[str] = None
    status: Optional[str] = None


class Order(OrderBase):
    id: int

    class Config:
        orm_mode = True
