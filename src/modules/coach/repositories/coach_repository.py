from typing import Optional
import random

from modules.coach.entities.coach_entity import CoachEntity
from modules.shared.adapters import RepositoryAdapter
from modules.shared.services.supabase.supabase_service import SupabaseService


class CoachRepository(RepositoryAdapter):
    def __init__(self, supabase_service: SupabaseService):
        self.__supabase_service = supabase_service
        super().__init__("coachs")

    async def get_random_coach(self) -> Optional[CoachEntity]:
        response = await self.__supabase_service.custom_query(
            main_table=self.table, select_fields=["*"], where_conditions={}
        )
        if not response or len(response) == 0:
            return None
        random_coach_data = random.choice(response)
        return CoachEntity(**random_coach_data)
        
