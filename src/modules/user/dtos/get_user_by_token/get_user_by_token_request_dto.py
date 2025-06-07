from pydantic import BaseModel


class GetUserByTokenRequestDto(BaseModel):
    token: str
