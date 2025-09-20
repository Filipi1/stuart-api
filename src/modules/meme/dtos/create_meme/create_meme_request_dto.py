from pydantic import BaseModel, Field
from typing import Optional


class CreateMemeRequestDto(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    description: Optional[str] = Field(None, max_length=1000)
    image: str = Field(min_length=1)
