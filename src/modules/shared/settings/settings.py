from typing import Optional

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    environment: str
    supabase_url: str
    supabase_key: str
    supabase_schema: Optional[str] = None

    class Config:
        env_file = ".env"
