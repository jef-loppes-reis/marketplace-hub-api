from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from ..core.database import DBBaseModel


class ProdutosModel(DBBaseModel):
    __tablename__ = 'produtos'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[String] = mapped_column(String(100))
    price: Mapped[Float] = mapped_column(Float)
    available_quantity: Mapped[int] = mapped_column(Integer)
    sku: Mapped[String] = mapped_column(String(100))
    status: Mapped[String] = mapped_column(String(100))
