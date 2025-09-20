from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class CreateMemeResponseDto(BaseModel):
    id: int = Field()
    title: str = Field()
    description: Optional[str] = Field()
    image: str = Field()
    earned_times: int = Field(default=0)
    created_at: Optional[datetime] = Field()
    updated_at: Optional[datetime] = Field()
