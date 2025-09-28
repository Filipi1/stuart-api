from datetime import datetime

from pydantic import BaseModel


class GetUserByTokenResponseDto(BaseModel):
    id: str
    name: str
    email: str
    created_at: datetime
    updated_at: datetime
