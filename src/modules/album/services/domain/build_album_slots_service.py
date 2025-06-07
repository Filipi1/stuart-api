from modules.album.entities.album_figure import AlbumFigureEntity
from modules.album.entities.album_slot import AlbumSlotEntity
from modules.album.dtos.build_album_slots import BuildAlbumSlotsRequestDto, BuildAlbumSlotsResponseDto

from modules.shared.adapters import DomainService

class BuildAlbumSlotsDomainService(DomainService):
    def process(self, input: BuildAlbumSlotsRequestDto) -> list[AlbumSlotEntity]:
        # Para cada meme no input.user_earned_memes, criar um slot com o meme.
        # O slot deve conter em str o id do meme com no minimo dois digitos 0 a esquerda
        # O figure deve conter uma instancia de AlbumFigureEntity com os dados do meme

        return [ AlbumSlotEntity(
            slot=str(slot.meme_id).zfill(2), 
            figure=AlbumFigureEntity(
                name=meme.meme.title, 
                description=meme.meme.description, 
                image=meme.meme.image, 
                drawed_times=meme.earned_times, 
                earned_at=meme.created_at
            )
        ) for slot, meme in zip(input.user_earned_memes, input.user_earned_memes) ]