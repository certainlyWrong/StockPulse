from fastapi import APIRouter
from stockpulse.core.models.product_model import ProductModel

from stockpulse.db_connection import productsController


products_router = APIRouter(prefix='/products')


@products_router.get('/')
def find_all_products():
    products = productsController.find_all()
    return products


@products_router.get('/{product_id}/')
def find_product_by_uid(product_id: int):
    product = productsController.find_by_id(product_id)
    return product or {"message": "Product not found"}


@products_router.post('/')
def create_product(product: ProductModel):
    product = productsController.create(product)
    return product


@products_router.patch('/{product_id}/')
def update_product(product_id: int, product: ProductModel):
    result = productsController.update(product_id, product)
    return result or {"message": "Product not found"}


@products_router.delete('/{product_id}/')
def delete_product(product_id: int):
    result = productsController.delete(product_id)

    return (
        {"message": "Product deleted successfully"}
        if result
        else
        {"message": "Product not found"}
    )
