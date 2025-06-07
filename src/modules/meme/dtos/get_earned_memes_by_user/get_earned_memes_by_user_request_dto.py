from pydantic import BaseModel


class GetEarnedMemesByUserRequestDto(BaseModel):
    user_id: int
