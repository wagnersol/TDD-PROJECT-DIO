from datetime import datetime
import uuid
from pydantic import BaseModel, Field


class BaseSchemasMixin(BaseModel):
    id = UUID4 = Field(defauld_factory=uuid.uuid4)
    created_at: datetime = Field(defauld_factory=datetime.utcnow)
    updated_at: datetime = Field(defauld_factory=datetime.utcnow)
