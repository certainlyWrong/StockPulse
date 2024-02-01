from sqlalchemy import Engine, create_engine
from sqlmodel import SQLModel

from stockpulse.core.controllers.product_controller import ProductsController
from .enviroments import Enviroments


engine: Engine
productController: ProductsController

try:
    engine = create_engine(
        Enviroments.get_instance.database_connection,
        echo=True,
    )

    engine.connect()
    SQLModel.metadata.create_all(engine, checkfirst=True)
    productController = ProductsController(engine)
except Exception:
    print("Error connecting to database")
    exit()
