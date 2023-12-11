
from abc import ABC

from sqlalchemy import (
    Engine,
)
from sqlmodel import (
    Session,
    select,
)

from stockpulse.core.models.product_model import ProductModel


class IProductController(ABC):
    """
    Interface for the ProductsController class.
    """

    @classmethod
    def find_all(cls) -> list[ProductModel]:
        raise NotImplementedError

    @classmethod
    def find_by_id(cls, id: int) -> ProductModel | None:
        raise NotImplementedError

    @classmethod
    def create(cls, product: ProductModel) -> ProductModel:
        raise NotImplementedError

    @classmethod
    def update(cls, id: int, product: ProductModel) -> ProductModel | None:
        raise NotImplementedError

    @classmethod
    def delete(cls, id: int) -> bool:
        raise NotImplementedError


class ProductsController(IProductController):
    """
    Controller for the Products entity.
    """

    def __init__(self, engine: Engine) -> None:
        self.engine = engine

    def find_all(self) -> list[ProductModel]:
        """
        Find all products.
        """
        with Session(self.engine) as session:
            statement = select(ProductModel)
            products = session.exec(statement).all()
            return list(products)

    def find_by_id(self, id: int) -> ProductModel | None:
        """
        Find a product by its uid.
        """
        with Session(self.engine) as session:
            statement = select(
                ProductModel
            ).where(ProductModel.id == id)

            product = session.exec(statement).first()
            return product

    def create(self, product: ProductModel) -> ProductModel:
        """
        Create a product.
        """
        with Session(self.engine) as session:
            session.add(product)
            session.commit()
            session.refresh(product)
            return product

    def update(self, id: int, product: ProductModel) -> ProductModel | None:
        """
        Update a product.
        """
        with Session(self.engine) as session:
            try:
                existing_product = session.exec(
                    select(ProductModel).where(ProductModel.id == id)).first()

                if existing_product:
                    for key, value in product.dict(exclude_unset=True).items():
                        setattr(existing_product, key, value)

                    session.commit()
                    session.refresh(existing_product)
                    return existing_product
                else:
                    return None
            except Exception as e:
                print(f"Erro ao atualizar: {e}")
                return None

    def delete(self, id: int) -> bool:
        """
        Delete a product.
        """
        with Session(self.engine) as session:
            statement = select(
                ProductModel
            ).where(ProductModel.id == id)

            if session.exec(statement).first() is None:
                return False

            product = session.exec(statement).first()
            session.delete(product)
            session.commit()
            return True
