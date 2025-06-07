from typing import Optional
from pydantic import BaseModel, Field


class MemeEntity(BaseModel):
    title: str = Field(alias="title")
    description: Optional[str] = Field(alias="description")
    image: str = Field(alias="image")