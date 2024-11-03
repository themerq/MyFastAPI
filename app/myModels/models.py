from sqlalchemy import ForeignKey, text, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.database import Base, str_uniq, int_pk, str_null_true
from datetime import date


# модель таблицы Product
class Product(Base):
    id: Mapped[int_pk]
    name: Mapped[str]
    description: Mapped[str_null_true]
    price: Mapped[float]
    quantity: Mapped[int]

# модель таблицы Order
class Order(Base):
    id: Mapped[int_pk]
    created_date: Mapped[date]
    status: Mapped[bool]

# модель таблицы OrderItem
class OrderItem(Base):
    id: Mapped[int_pk]
    order_id: Mapped[int] = mapped_column(ForeignKey("orders.id"), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), nullable=False)
    quantity: Mapped[int]
