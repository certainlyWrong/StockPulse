from .routes.hello_router import router_root
from stockpulse.routes.v1.all_routes import router_v1
from fastapi import FastAPI


app = FastAPI(debug=True)

app.include_router(router_root)
app.include_router(router_v1)
