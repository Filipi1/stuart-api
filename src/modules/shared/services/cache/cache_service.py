from typing import Callable, Optional, TypeVar

import redis
from pydantic import BaseModel

from modules.shared.services.logger.logger_service import LoggerService

T = TypeVar("T", bound=BaseModel)


class CacheService:
    def __init__(
        self,
        host: str = "localhost",
        port: int = 6379,
        db: int = 0,
        password: Optional[str] = None,
    ) -> None:
        self.__host = host
        self.__port = port
        self.__db = db
        self.__password = password
        self.__client: Optional[redis.Redis] = None
        self.__logger = LoggerService("CacheService")

    def __get_client(self) -> Optional[redis.Redis]:
        try:
            if self.__client is None:
                self.__client = redis.Redis(
                    host=self.__host,
                    port=self.__port,
                    db=self.__db,
                    password=self.__password,
                    decode_responses=True,
                    socket_connect_timeout=5,
                    socket_timeout=5,
                )
            self.__client.ping()
            return self.__client
        except Exception:
            self.__client = None
            return None

    def get(self, key: str) -> Optional[str]:
        try:
            client = self.__get_client()
            if client is None:
                self.__logger.error(
                    f"Error getting client for key: <yellow>{key}</yellow>."
                )
                return None

            self.__logger.info(
                f"Getting value from cache for key: <yellow>{key}</yellow>."
            )
            return client.get(key)
        except Exception:
            return None

    def set(self, key: str, value: str, expire: Optional[int] = None) -> bool:
        try:
            client = self.__get_client()
            if client is None:
                self.__logger.error(
                    f"Error getting client for key: <yellow>{key}</yellow>."
                )
                return False
            if expire:
                self.__logger.info(
                    f"Setting value in cache for key: <yellow>{key}</yellow> with expire: <yellow>{expire}</yellow> seconds."
                )
                client.setex(key, expire, value)
            else:
                self.__logger.info(
                    f"Setting value in cache for key: <yellow>{key}</yellow> without expire."
                )
                client.set(key, value)
            return True
        except Exception:
            return False

    def delete(self, key: str) -> bool:
        try:
            client = self.__get_client()
            if client is None:
                return False
            client.delete(key)
            return True
        except Exception:
            return False

    def exists(self, key: str) -> bool:
        try:
            client = self.__get_client()
            if client is None:
                return False
            return bool(client.exists(key))
        except Exception:
            return False

    def get_model(self, key: str, model_class: type[T]) -> Optional[T]:
        try:
            cached_data = self.get(key)
            if cached_data is None:
                return None
            return model_class.model_validate_json(cached_data)
        except Exception:
            return None

    def set_model(
        self, key: str, model: BaseModel, expire: Optional[int] = None
    ) -> bool:
        try:
            if model is None:
                return False
            cache_data = model.model_dump_json()
            return self.set(key, cache_data, expire)
        except Exception:
            return False

    async def get_or_compute_model(
        self,
        key: str,
        compute_func: Callable[[], T],
        model_class: type[T],
        expire: Optional[int] = None,
    ) -> Optional[T]:

        cached_model = self.get_model(key, model_class)
        if cached_model is not None:
            return cached_model

        try:
            if callable(compute_func):
                import asyncio

                if asyncio.iscoroutinefunction(compute_func):
                    model = await compute_func()
                else:
                    model = compute_func()
            else:
                return None

            if model is not None:
                self.set_model(key, model, expire)

            return model
        except Exception:
            return None
