from fastapi import APIRouter, Depends
from app.myModels.core import ProductCore, OrderCore
from app.myModels.rb import RBProduct, RBOrder
from app.myModels.schemas import SProductAdd, SProduct, SProductUpdDesc, SOrder


router = APIRouter(prefix='/products', tags=['Работа с товарами'])
router_ii = APIRouter(prefix='/orders', tags=['Работа с заказами'])


@router.post("/add/", summary="Добавить товары")
async def register_user(product: SProductAdd) -> dict:
    check = await ProductCore.add(**product.dict())
    if check:
        return {"message": "Успешно добавлен!", "product": product}
    else:
        return {"message": "Ошибка при добавлении!"}


@router.get("/get", summary="Получить все товары")
async def get_all_products(request_body: RBProduct = Depends()) -> list[SProduct]:
    return await ProductCore.find_all(**request_body.to_dict())


@router.get("/by_filter", summary="Получить один товар по фильтру")
async def get_product_by_filter(request_body: RBProduct = Depends()) -> SProduct | dict:
    rez = await ProductCore.find_one_or_none(**request_body.to_dict())
    if rez is None:
        return {'message': f'Товар с указанными вами параметрами не найден!'}
    return rez


@router.put("/update_description/", summary="Обновить товар")
async def update_product_description(product: SProductUpdDesc) -> dict:
    check = await ProductCore.update(filter_by={'product_name': product.major_name},
                                   product_description=product.product_description)
    if check:
        return {"message": "Описание успешно обновлено!", "product": product}
    else:
        return {"message": "Ошибка при обновлении описания!"}


@router.delete("/dell/{product_id}", summary="Удалить товар")
async def dell_product_by_id(product_id: int) -> dict:
    check = await ProductCore.delete_product_by_id(prodcut_id=product_id)
    if check:
        return {"message": f"Товар с ID {product_id} удален!"}
    else:
        return {"message": "Ошибка при удалении товара!"}


@router_ii.post("/add/", summary="Добавить товары")
async def register_user(product: SProductAdd) -> dict:
    check = await ProductCore.add(**product.dict())
    if check:
        return {"message": "Успешно добавлен!", "product": product}
    else:
        return {"message": "Ошибка при добавлении!"}


@router_ii.get("/get", summary="Получить все заказы")
async def get_all_orders(request_body: RBOrder = Depends()) -> list[SOrder]:
    return await OrderCore.find_all(**request_body.to_dict())


@router_ii.get("/by_filter", summary="Получить один заказ по фильтру")
async def get_order_by_filter(request_body: RBOrder = Depends()) -> SOrder | dict:
    rez = await OrderCore.find_one_or_none(**request_body.to_dict())
    if rez is None:
        return {'message': f'Заказ с указанными вами параметрами не найден!'}
    return rez


@router_ii.patch("/patch/{order_id}/status", summary="Обновление статуса заказа")
async def patch_order():
    pass
