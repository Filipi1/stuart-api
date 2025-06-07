from pydantic import BaseModel

from modules.user.entities.user import User


class FetchUserByTokenResponseDto(BaseModel):
    user: User
