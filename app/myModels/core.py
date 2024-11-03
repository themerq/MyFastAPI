from app.core.base import BaseCore
from app.myModels.models import Product, Order

class ProductCore(BaseCore):
    model = Product

class OrderCore(BaseCore):
    model = Order
