from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class CoachEntity(BaseModel):
    id: int = Field(alias="id")
    message: str = Field(alias="message")
    author: str = Field(alias="author")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")