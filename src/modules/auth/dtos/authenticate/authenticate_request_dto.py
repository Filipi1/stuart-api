from pydantic import BaseModel, Field


class AuthenticateRequestDto(BaseModel):
    token: str = Field(min_length=1)
