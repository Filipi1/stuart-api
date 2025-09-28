from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class FetchRandomCoachResponseDto(BaseModel):
    id: int = Field()
    message: str = Field()
    author: str = Field()
    created_at: Optional[datetime] = Field()
    updated_at: Optional[datetime] = Field()
