from .routes.hello_router import router_root
from stockpulse.routes.v1.product_routes import products_router
from fastapi import FastAPI


app = FastAPI(
    title="Stock Pulse API",
    description="This is a very fancy project,"
)

app.include_router(router_root)
app.include_router(products_router, prefix='/api/v1', tags=['v1'])
