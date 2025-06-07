from pydantic import BaseModel
from modules.meme.entities.meme import MemeEntity


class GetMemeByIdResponseDto(BaseModel):
    meme: MemeEntity
