from typing import Optional
from pydantic import BaseModel as SCBaseModel


class ProdutosSchema(SCBaseModel):

    id: Optional[int]
    title: str
    price: float
    sku: str

    class config:
        orm_mode = True
