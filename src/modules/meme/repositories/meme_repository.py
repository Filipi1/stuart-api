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

    async def increase_earned_times(self, meme: MemeEntity):
        new_earned_times = int(meme.earned_times) + 1

        response = await self.__supabase_service.update(
            self.table, str(meme.id), {"drawnTimes": new_earned_times}
        )

        updated_meme = MemeEntity(**response[0])
        return updated_meme

    async def get_random_meme(self) -> MemeEntity:
        import random

        # Busca todos os memes
        response = await self.__supabase_service.custom_query(
            main_table=self.table, select_fields=["*"], where_conditions={}
        )

        if not response:
            return None

        # Seleciona um meme aleatório
        random_meme = random.choice(response)
        return MemeEntity(**random_meme)

    async def count_total_memes(self) -> int:
        response = await self.__supabase_service.custom_query(
            main_table=self.table, select_fields=["count"], where_conditions={}
        )
        return response[0]["count"] if response else 0

    async def get_memes_paginated(
        self, page: int, items_per_page: int
    ) -> list[MemeEntity]:
        offset = (page - 1) * items_per_page
        response = await self.__supabase_service.custom_query(
            main_table=self.table,
            select_fields=["id", "title", "description", "image"],
            order_by={"id": "asc"},
            limit=items_per_page,
            where_conditions={"id": {"gte": offset + 1}},
        )
        return [MemeEntity(**meme) for meme in response] if response else []

    async def create_meme(self, title: str, description: str, image: str) -> MemeEntity:
        data = {
            "title": title,
            "description": description,
            "image": image,
            "isActive": True,
            "drawnTimes": 0,
        }

        response = await self.__supabase_service.create(self.table, data)
        return MemeEntity(**response[0]) if response else None
