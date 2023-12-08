from fastapi import APIRouter

from stockpulse.routes.v1.product_routes import products_router

router_v1 = APIRouter(prefix='/v1')
router_v1.__doc__ = "Version 1 of the StockPulse API"
router_v1.include_router(products_router)
