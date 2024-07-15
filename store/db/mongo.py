from motor.motor_asyncio import AsyncIOMotorClient
from store.core.config import settings


class mongoClient:
    def __inti__(self) -> None:
        self.Client: AsyncIOMotorClient = AsyncIOMotorClient(settings.DATABASE_URL)

        def get(self) -> AsyncIOMotorClient:
            return self.Client


db_client = mongoClient()
