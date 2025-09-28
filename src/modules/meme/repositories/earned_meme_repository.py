from modules.meme.entities import EarnedMemeEntity
from modules.shared.adapters import RepositoryAdapter
from modules.shared.services.supabase.supabase_service import SupabaseService


class EarnedMemeRepository(RepositoryAdapter):
    def __init__(self, supabase_service: SupabaseService) -> None:
        self.__supabase_service = supabase_service
        super().__init__("earned_memes")

    async def get_earned_memes_by_user_id(self, user_id: int) -> list[EarnedMemeEntity]:
        response = await self.__supabase_service.read(self.table, {"userId": user_id})
        return [EarnedMemeEntity(**meme) for meme in response] if response else []

    async def get_earned_memes_with_meme_info(
        self, user_id: int
    ) -> list[EarnedMemeEntity]:
        response = await self.__supabase_service.custom_query(
            main_table="earned_memes",
            select_fields=[
                "id",
                "userId",
                "memeId",
                "earnedTimes",
                "updatedAt",
                "createdAt",
                "memes(id, title, description, image)",
            ],
            where_conditions={"userId": user_id},
        )
        return [EarnedMemeEntity(**meme) for meme in response] if response else []

    async def increase_meme_to_user(
        self, user_id: int, meme_id: int
    ) -> EarnedMemeEntity:
        response = await self.__supabase_service.read(
            self.table, {"userId": user_id, "memeId": meme_id}
        )
        if response and len(response) > 0:
            earned_meme = EarnedMemeEntity(**response[0])
            response = await self.__supabase_service.update(
                self.table,
                earned_meme.id,
                {"earnedTimes": earned_meme.earned_times + 1},
            )
            return EarnedMemeEntity(**response[0])
        response = await self.__supabase_service.create(
            self.table,
            {
                "userId": user_id,
                "memeId": meme_id,
                "earnedTimes": 1,
            },
        )
        return EarnedMemeEntity(**response)
