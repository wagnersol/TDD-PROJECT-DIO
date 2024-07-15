from typing import List
from uuid import UUID
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
import pymongo
from store.db.mongo import db_client
from store.models.product import productModel
from store.schemas import productIn, productOut, productUpdate, productUpdateOut
from store.core.exception import NotFoundException


class productUsecase:
    def __init__(self) -> None:
        self.client: AsyncIOMotorClient = db_client.get()
        self.database: AsyncIOMotorDatabase = self.client.get_database()
        self.collection = self.database.get_collection("products")

    async def create(self, body: productIn) -> productOut:
        product_model = productModel(**body.model_dump())
        await self.collection.insert_one(product_model.model_dump())

        return productOut(**product_model.model_dump())

    async def get(self, id: UUID) -> productOut:
        result = await self.collection.find_one({"id": id})

        if not result:
            raise NotFoundException(massage="product not found with filter:{id}")

        return productOut(**result)

    async def query(self) -> List[productOut]:
        return [productOut(**item) async for item in self.collection.find()]

    async def update(self, id: UUID, body: productUpdate) -> productUpdateOut:
        result = await self.collection.find_one_and_update(
            filter={"id": id},
            update={"$set": body.model_drump(exclude_none=True)},
            return_document=pymongo.ReturnDocument.AFTER,
        )

        return productUpdateOut(**result)

    async def delete(self, id: UUID) -> bool:
        product = await self.collection.find_one({"id": id})
        if not product:
            raise NotFoundException(massage="product not found withfilter:{id}")

        result = await self.collection.delete_one({"id": id})

        return True if result.deleted_count > 0 else False


product_usecase = productUsecase()
