from hashlib import sha256
from modules.shared.adapters import DomainService

from modules.user.services.domain.create_user_service import CreateUserDomainService
from modules.user.services.domain.get_user_by_username_service import GetUserByUsernameDomainService

class GenerateTokenDomainService(DomainService):
    def __init__(self, get_user_by_username: GetUserByUsernameDomainService, create_user: CreateUserDomainService):
        self.__get_user_by_username = get_user_by_username
        self.__create_user = create_user    
        super().__init__(GenerateTokenDomainService.__name__)

    async def process(self, username: str) -> str:
        user = await self.__get_user_by_username.process(username)
        if not user:
            self.logger.info(f"User not found, creating new user: {username}")
            token = sha256(username.encode()).hexdigest()
            user = await self.__create_user.process(username, token)
            return user.token

        return user.token