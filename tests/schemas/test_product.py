import pytest
from pydantic import ValidationError
from store.schemas import productIn
from tests.factories import product_data


def test_schemas_return_success():
    data = product_data()
    product = productIn.model_validate(data)

    assert product.name == "Iphone 14 pro Max"


def test_schemas_return_raise():
    data = {"nome": "Iphone 14 Pro Max", "quantity": 10, "price": 8.500}
    productIn.model_validate(data)

    with pytest.raises(ValidationError) as err:
        productIn.model_validate(data)

    assert err.value.errors()[0] == {
        "type": "missing",
        "loc": ("status",),
        "msg": "Field required",
        "input": {"nome": "Iphone 14 pro Max", "quantity": 10, "price": 8.5},
        "url": "https://errors.pydentic.dev/2.5//vmissing",
    }
