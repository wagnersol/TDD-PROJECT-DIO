from pydantic import Field
from store.schemas.base import BaseSchemasMixin


class productIn(BaseSchemasMixin):
    name: str = Field(..., description="product name")
    quantity: int = Field(..., description="product quantity")
    price: float = Field(..., description="product price")
    status: bool = Field(..., description="product status")
