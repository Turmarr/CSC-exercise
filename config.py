from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    ID: str
    SECRET: str

    model_config = SettingsConfigDict(env_file=".env")