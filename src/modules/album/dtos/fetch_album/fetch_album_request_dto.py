from pydantic import BaseModel, Field


class FetchAlbumRequestDto(BaseModel):
    page: int = Field(default=1, ge=1)
    token: str
