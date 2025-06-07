from pydantic import BaseModel


class FetchEarnedMemesByUserRequestDto(BaseModel):
    user_id: int
