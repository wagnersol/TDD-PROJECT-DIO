from store.models.base import CreateBaseModel
from store.schemas.product import productIn


class productModel(productIn, CreateBaseModel):
    ...
