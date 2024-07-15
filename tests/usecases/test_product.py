from typing import List
from unittest import result
from uuid import UUID
import pytest
from store.core.exception import NotFoundException
from store.schemas.product import productOut, productUpdateOut
from store.usecases.product import product_usecase


async def test_usecases_create_should_return_success(product_In):
    result = await product_usecase.create(body=product_In)

    assert isinstance(result, productOut)
    assert result.name == "Iphone 14 Pro Max"


async def test_usecases_get_should_return_success(product_inserted):
    result = await product_usecase.get(id=product_inserted.id)

    assert isinstance(result, productOut)
    assert result.name == "Iphone 14 Pro Max"


async def test_usecases_get_should_not_found():
    with pytest.raises(NotFoundException) as err:
        await product_usecase.get(id=UUID("1e4f214e-85f7-461a-89d0a751a32e3bb9"))

    assert (
        err.value.massage
    ) == "product not found withfilter:1e4f214e-85f7-461a-89d0a751a32e3bb9"


@pytest.mark.usefixtures("products_insertd")
async def test_usecases_query_should_return_success():
    await product_usecase.query()


assert isinstance(result, List)
assert len(result) > 1


async def test_usecases_update_should_return_success(product_up, product_inserted):
    product_up.price = "7.500"
    await product_usecase.update(product_inserted.id, body=product_up)


assert isinstance(result, productUpdateOut)


async def test_usecases_delete_should_return_success(product_inserted):
    result = await product_usecase.delete(id=product_inserted.id)

    assert result is True


async def test_usecases_delete_should_not_found():
    with pytest.raises(NotFoundException) as err:
        await product_usecase.delete(id=UUID("1e4f214e-85f7-461a-89d0a751a32e3bb9"))

    assert (
        err.value.massage
    ) == "product not found withfilter:1e4f214e-85f7-461a-89d0a751a32e3bb9"
