from pydantic import BaseModel, Field


class AuthenticateRequestDto(BaseModel):
    identifier: str = Field(min_length=1)
