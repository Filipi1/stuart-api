from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class FetchRandomCoachResponseDto(BaseModel):
    id: int = Field()
    message: str = Field()
    author: str = Field()
    created_at: Optional[datetime] = Field()
    updated_at: Optional[datetime] = Field()
