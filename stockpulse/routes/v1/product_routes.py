from fastapi import APIRouter
from stockpulse.core.models.product_model import ProductModel

from stockpulse.db_connection import productController


products_router = APIRouter(prefix='/product', tags=['product'])


@products_router.get('/')
async def find_all_products():
    products = productController.find_all()
    return products


@products_router.get('/{product_id}/')
async def find_product_by_uid(product_id: int):
    product = productController.find_by_id(product_id)
    return product or {"message": "Product not found"}


@products_router.post('/')
async def create_product(product: ProductModel):
    product = productController.create(product)
    return product


@products_router.patch('/{product_id}/')
async def update_product(product_id: int, product: ProductModel):
    result = productController.update(product_id, product)
    return result or {"message": "Product not found"}


@products_router.delete('/{product_id}/')
async def delete_product(product_id: int):
    result = productController.delete(product_id)

    return (
        {"message": "Product deleted successfully"}
        if result
        else
        {"message": "Product not found"}
    )
