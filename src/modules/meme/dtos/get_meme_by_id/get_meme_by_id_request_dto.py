from pydantic import BaseModel


class GetMemeByIdRequestDto(BaseModel):
    meme_id: int
