from pydantic import BaseModel

from modules.meme.entities.earned_meme import EarnedMemeEntity
from modules.meme.entities.meme import MemeEntity


class BuildAlbumSlotsRequestDto(BaseModel):
    user_earned_memes: list[EarnedMemeEntity]
    paginated_memes: list[MemeEntity]
    slot_offset: int
