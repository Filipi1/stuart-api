from typing import Optional

from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    port: Optional[int] = 10300
    environment: Optional[str] = None
    supabase_url: Optional[str] = None
    supabase_key: Optional[str] = None
    supabase_schema: Optional[str] = None
    redis_host: Optional[str] = "localhost"
    redis_port: Optional[int] = 6379
    redis_db: Optional[int] = 0
    redis_password: Optional[str] = None
    model_config = ConfigDict(env_file=".env")

    def is_development(self) -> bool:
        return self.environment == "development"
