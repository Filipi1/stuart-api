from pydantic import BaseModel


class AuthenticateResponseDto(BaseModel):
    token: str
