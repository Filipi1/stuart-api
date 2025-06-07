from modules.meme.entities.meme import MemeEntity
from modules.shared.adapters import RepositoryAdapter
from modules.shared.services.supabase.supabase_service import SupabaseService


class MemeRepository(RepositoryAdapter):
    def __init__(self, supabase_service: SupabaseService) -> None:
        self.__supabase_service = supabase_service
        super().__init__("memes")

    async def get_meme_by_id(self, meme_id: int) -> MemeEntity:
        response = await self.__supabase_service.read(self.table, {"id": meme_id})
        return MemeEntity(**response[0]) if response else None
