from sqlalchemy import Engine, create_engine
from sqlmodel import SQLModel

from stockpulse.core.controllers.product_controller import ProductsController
from .environment import Environment


engine: Engine
productController: ProductsController

try:
    engine = create_engine(
        Environment.get_instance.database_connection,
        echo=True,
    )

    engine.connect()
    SQLModel.metadata.create_all(engine, checkfirst=True)
    productController = ProductsController(engine)
except Exception:
    print("Error connecting to database")
    exit()
