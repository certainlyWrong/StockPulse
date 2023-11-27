from datetime import datetime

from typing import Optional
from sqlmodel import Field, SQLModel


class ProductModel(SQLModel, table=True, schema="stockpulse"):
    id: Optional[int] = Field(
        default=None,
        primary_key=True,
    )
    name: str
    price: float
    quantity: int
    description: Optional[str]
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime]
