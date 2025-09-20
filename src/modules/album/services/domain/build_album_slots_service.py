from modules.album.entities.album_figure import AlbumFigureEntity
from modules.album.entities.album_slot import AlbumSlotEntity
from modules.album.dtos.build_album_slots import BuildAlbumSlotsRequestDto

from modules.shared.adapters import DomainService


class BuildAlbumSlotsDomainService(DomainService):
    def process(self, input: BuildAlbumSlotsRequestDto) -> list[AlbumSlotEntity]:
        # Criar um dicionário com os memes ganhos pelo usuário para fácil acesso
        earned_memes_dict = {meme.meme_id: meme for meme in input.user_earned_memes}

        # Criar slots para todos os memes da página atual
        slots = []
        for meme in input.paginated_memes:
            meme_id = meme.id
            slot = AlbumSlotEntity(slot=str(meme_id).zfill(3), figure=None)

            # Se o usuário ganhou este meme, preencher o slot
            if meme_id in earned_memes_dict:
                earned_meme = earned_memes_dict[meme_id]
                slot.figure = AlbumFigureEntity(
                    name=earned_meme.meme.title,
                    description=earned_meme.meme.description,
                    image=earned_meme.meme.image,
                    drawed_times=earned_meme.earned_times,
                    earned_at=earned_meme.created_at,
                )

            slots.append(slot)

        return slots
