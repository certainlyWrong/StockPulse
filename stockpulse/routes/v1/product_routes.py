from fastapi import APIRouter
from sqlalchemy import Engine, create_engine, text
from sqlmodel import SQLModel

from stockpulse.core.controllers.products_controller import ProductsController
from stockpulse.core.models.product_model import ProductModel


database_url = "mysql+pymysql://root:1234@localhost:3306"

engine: Engine
productsController: ProductsController


try:
    engine = create_engine(
        f'{database_url}/stockpulse',
        echo=True,
    )

    engine.dispose()
    engine.connect()
    SQLModel.metadata.create_all(engine, checkfirst=True)
    productsController = ProductsController(engine)

except Exception as e:
    print(e)
    with create_engine(database_url, echo=True).connect() as conn:
        conn.execute(text("CREATE DATABASE stockpulse"))

    engine = create_engine(
        f'{database_url}/stockpulse',
        echo=True,
    )
    engine.dispose()
    engine.connect()
    SQLModel.metadata.create_all(engine, checkfirst=True)
    productsController = ProductsController(engine)

products_router = APIRouter(prefix='/products')


@products_router.get('/')
def find_all_products():
    products = productsController.find_all()
    return products


@products_router.get('/{product_id}/')
def find_product_by_uid(product_id: int):
    product = productsController.find_by_id(product_id)

    if product is None:
        return {"error": "Product not found"}
    return product


@products_router.post('/')
def create_product(product: ProductModel):
    product = productsController.create(product)
    return product


@products_router.delete('/{product_id}/')
def delete_product(product_id: int):
    result = productsController.delete(product_id)
    return {"success": result}
