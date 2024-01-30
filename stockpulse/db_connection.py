from sqlalchemy import Engine, create_engine
from sqlmodel import SQLModel

from stockpulse.core.controllers.product_controller import ProductsController
import os

DATABASE_URL = os.getenv('DATABASE_URL', 'localhost:3301')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'stockpulse')
DATABASE_USER = os.getenv('DATABASE_USER', 'admin')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', '123456')

database_url = (f"mysql+mysqlconnector://{DATABASE_USER}:{DATABASE_PASSWORD}"
                f"@{DATABASE_URL}")

print("database_url", database_url)

print("database_url", database_url)
print("DATABASE_HOST", DATABASE_URL)
print("DATABASE_NAME", DATABASE_NAME)
print("DATABASE_USER", DATABASE_USER)
print("DATABASE_PASSWORD", DATABASE_PASSWORD)

engine: Engine
productController: ProductsController

try:
    engine = create_engine(
        f'{database_url}/{DATABASE_NAME}',
        echo=True,
    )

    engine.connect()
    SQLModel.metadata.create_all(engine, checkfirst=True)
    productController = ProductsController(engine)
except Exception:
    print("Error connecting to database")
    exit()
