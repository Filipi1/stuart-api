from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from modules.meme.entities.meme import MemeEntity


class EarnedMemeEntity(BaseModel):
    id: int = Field(alias="id")
    user_id: int = Field(alias="userId")
    meme_id: int = Field(alias="memeId")
    earned_times: int = Field(alias="earnedTimes")
    meme: Optional[MemeEntity] = Field(default=None, alias="memes")
    updated_at: datetime = Field(alias="updatedAt")
    created_at: datetime = Field(alias="createdAt")
