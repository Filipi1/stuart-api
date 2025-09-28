from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class User(BaseModel):
    id: int = Field(alias="id")
    username: str = Field(alias="username")
    display_name: Optional[str] = Field(
        alias="displayName", serialization_alias="display_name", default=None
    )
    token: str = Field(alias="token")
    created_at: datetime = Field(alias="createdAt", serialization_alias="created_at")
