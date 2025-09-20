from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class MemeEntity(BaseModel):
    id: int = Field(alias="id")
    title: str = Field(alias="title")
    description: Optional[str] = Field(alias="description")
    image: str = Field(alias="image")
    earned_times: int = Field(default=0, alias="drawnTimes")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    updated_at: Optional[datetime] = Field(default=None, alias="updatedAt")
