from fastapi import APIRouter
from sqlalchemy import Engine, create_engine
from sqlmodel import SQLModel

from stockpulse.core.controllers.products_controller import ProductsController
from stockpulse.core.models.product_model import ProductModel

import os

DATABASE_HOST = os.getenv('DATABASE_HOST', 'localhost')
DATABASE_PORT = os.getenv('DATABASE_PORT', '3306')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'stockpulse')
DATABASE_USER = os.getenv('DATABASE_USER', 'root')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', '123456')

database_url = (f"mysql+mysqlconnector://{DATABASE_USER}:{DATABASE_PASSWORD}"
                f"@{DATABASE_HOST}:{DATABASE_PORT}")

print("database_url", database_url)
print("DATABASE_HOST", DATABASE_HOST)
print("DATABASE_PORT", DATABASE_PORT)
print("DATABASE_NAME", DATABASE_NAME)
print("DATABASE_USER", DATABASE_USER)
print("DATABASE_PASSWORD", DATABASE_PASSWORD)

engine: Engine
productsController: ProductsController

try:
    engine = create_engine(
        f'{database_url}/{DATABASE_NAME}',
        echo=True,
    )

    engine.connect()
    SQLModel.metadata.create_all(engine, checkfirst=True)
    productsController = ProductsController(engine)
except Exception:
    print("Error connecting to database")
    exit()


products_router = APIRouter(prefix='/products')


@products_router.get('/')
def find_all_products():
    products = productsController.find_all()
    return products


@products_router.get('/{product_id}/')
def find_product_by_uid(product_id: int):
    product = productsController.find_by_id(product_id)
    if product is None:
        return {"message": "Product not found"}
    return product


@products_router.post('/')
def create_product(product: ProductModel):
    product = productsController.create(product)
    return product

# update


@products_router.put('/')
def update_product(product: ProductModel):
    result = productsController.update(product)

    if result is None:
        return {"message": "Product not found"}
    return result


@products_router.delete('/{product_id}/')
def delete_product(product_id: int):
    result = productsController.delete(product_id)

    if result:
        return {"message": "Product deleted successfully"}
    else:
        return {"message": "Product not found"}
