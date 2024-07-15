from decimal import Decimal
from typing import Annotated, Optional

from bson import Decimal128
from pydantic import AfterValidator, Field
from store.schemas.base import BaseSchemasMixin, outSchema


class productBase(BaseSchemasMixin):
    name: str = Field(..., description="product name")
    quantity: int = Field(..., description="product quantity")
    price: Decimal = Field(..., description="product price")
    status: bool = Field(..., description="product status")


class productIn(productBase, BaseSchemasMixin):
    ...


class productOut(productIn, outSchema):
    ...


def convert_decimal_128(v):
    return Decimal128(str(v))


Decimal_ = Annotated[Decimal, AfterValidator(convert_decimal_128)]


class productUpdate(BaseSchemasMixin):
    quantity: Optional[int] = Field(None, description="product quantity")
    price: Optional[Decimal_] = Field(None, description="product price")
    status: Optional[bool] = Field(None, description="product status")


class productUpdateOut(productOut):
    ...
