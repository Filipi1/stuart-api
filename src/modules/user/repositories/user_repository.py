from modules.shared.adapters import RepositoryAdapter
from modules.user.entities import User
from modules.shared.services.supabase.supabase_service import SupabaseService


class UserRepository(RepositoryAdapter):
    def __init__(self, supabase_service: SupabaseService) -> None:
        self.__supabase_service = supabase_service
        super().__init__("users")

    async def get_user_by_token(self, token: str) -> User:
        response = await self.__supabase_service.read(self.table, {"token": token})
        return User(**response[0]) if response else None

    async def get_user_by_username(self, username: str) -> User:
        response = await self.__supabase_service.read(self.table, {"username": username})
        return User(**response[0]) if response else None

    async def create_user(self, username: str, token: str) -> User:
        data = {
            "username": username,
            "token": token,
        }
        response = await self.__supabase_service.create(self.table, data)

        return User(**response)