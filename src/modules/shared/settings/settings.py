from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    environment: Optional[str] = None
    supabase_url: Optional[str] = None
    supabase_key: Optional[str] = None
    supabase_schema: Optional[str] = None

    def is_development(self) -> bool:
        return self.environment == "development"

    class Config:
        env_file = ".env"
