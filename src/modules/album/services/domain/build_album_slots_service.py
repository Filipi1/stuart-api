from modules.album.entities.album_figure import AlbumFigureEntity
from modules.album.entities.album_slot import AlbumSlotEntity
from modules.album.dtos.build_album_slots import BuildAlbumSlotsRequestDto

from modules.shared.adapters import DomainService


class BuildAlbumSlotsDomainService(DomainService):
    def process(self, input: BuildAlbumSlotsRequestDto) -> list[AlbumSlotEntity]:
        earned_memes_dict = {meme.meme_id: meme for meme in input.user_earned_memes}
        
        slots = []
        
        for index, meme in enumerate(input.paginated_memes):
            slot_number = input.slot_offset + index + 1
            slot_str = str(slot_number).zfill(3)
            
            if meme.id in earned_memes_dict:
                earned_meme = earned_memes_dict[meme.id]
                figure = AlbumFigureEntity(
                    name=meme.title,
                    description=meme.description,
                    image=meme.image,
                    drawed_times=earned_meme.earned_times,
                    earned_at=earned_meme.created_at,
                )
            else:
                figure = None
            
            slot = AlbumSlotEntity(
                slot=slot_str,
                figure=figure
            )
            slots.append(slot)
        
        return slots
