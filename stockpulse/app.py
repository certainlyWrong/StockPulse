from .routes.hello_router import router_root
from stockpulse.routes.v1.product_routes import products_router
from fastapi import FastAPI


app = FastAPI(debug=True)

app.include_router(router_root)
app.include_router(products_router, prefix='/v1', tags=['v1'])
