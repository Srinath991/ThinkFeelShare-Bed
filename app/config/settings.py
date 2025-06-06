from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    SUPABASE_URL: str
    FRONTEND_URL: str

    model_config = SettingsConfigDict(env_file=".env")
    
settings = Settings()