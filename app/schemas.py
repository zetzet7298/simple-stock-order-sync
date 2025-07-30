from typing import Optional

from pydantic import BaseModel, ConfigDict


class ProductSchema(BaseModel):
    id: int
    sku: str
    name: Optional[str] = None
    stock_quantity: int

    model_config = ConfigDict(from_attributes=True)
