from pydantic import BaseModel


class FetchUserByTokenRequestDto(BaseModel):
    token: str
