from modules.shared.adapters import DomainService
from modules.user.entities.user import User
from modules.user.repositories.user_repository import UserRepository


class CreateUserDomainService(DomainService):
    def __init__(self, user_repository: UserRepository):
        self.__user_repository = user_repository
        super().__init__(CreateUserDomainService.__name__)

    async def process(self, username: str, token: str) -> User:
        user = await self.__user_repository.create_user(username, token)
        return user
