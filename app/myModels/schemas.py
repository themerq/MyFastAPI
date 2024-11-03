from datetime import datetime, date
from typing import Optional
import re
from pydantic import BaseModel, Field, EmailStr, validator


class SProduct(BaseModel):
    id: int

class SProductUpdDesc(BaseModel):
    product_name: str = Field(..., description="Название")
    product_description: str = Field(None, description="Новое описание")

class SProductAdd(BaseModel):
    product_name: str = Field(..., description="Название")
    product_description: str = Field(None, description="Описание")
    count_product: int = Field(0, description="Количество")


class SOrder(BaseModel):
    order_name: str = Field(..., description="Название")
    order_description: str = Field(None, description="Новое описание")