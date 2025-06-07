from pydantic import BaseModel
from modules.meme.entities.earned_meme import EarnedMemeEntity


class BuildAlbumSlotsRequestDto(BaseModel):
    user_earned_memes: list[EarnedMemeEntity]
