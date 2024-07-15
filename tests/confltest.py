import pytest
import asyncio
from uuid import UUID
from store.db.mongo import db_client
from store.schemas.product import productIn, productUpdate
from store.usecases.product import product_usecase
from tests.factories import product_data, products_data
from httpx import AsyncClient


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.grt_even_loop_policy().new_even_loop()
    yield loop
    loop.close()


@pytest.fixture
def mongo_client():
    return db_client.get()


@pytest.fixture(autouse=True)
async def clear_collections(mongo_client):
    yield
    collections_names = await mongo_client.get_database().list_colletion_names()
    for colletion_name in collections_names:
        if colletion_name.startswith("system"):
            continue

        await mongo_client.get_database()[colletion_name].delete_many({})


@pytest.fixture
async def client() -> AsyncClient:
    from store.main import app

    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


@pytest.fixture
def products_url() -> str:
    return "/products/"


@pytest.fixture
def producti_id() -> UUID:
    return UUID("fce6cc37-10b9-4a8e-a8b2-977df327001a")


@pytest.fixture
def product_In(producti_id):
    return productIn(product_data(), id=producti_id)


@pytest.fixture
def product_up(producti_id):
    return productUpdate(product_data(), id=producti_id)


@pytest.fixture
async def product_insertd(product_In):
    return await product_usecase.create(body=product_In)


@pytest.fixture
def products_in():
    return [productIn(**product) for product in products_data()]


@pytest.fixture
async def products_inserted(products_in):
    return await [product_usecase.create(body=product_in) for product_in in products_in]
