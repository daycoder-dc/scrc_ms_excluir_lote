from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    api_key_token: str

    model_config = SettingsConfigDict(env_file=".env")

@lru_cache
def get_setting():
    return Settings()
