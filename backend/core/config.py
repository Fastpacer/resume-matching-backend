from pydantic_settings import BaseSettings
from dotenv import load_dotenv
load_dotenv("backend\.env")

class Settings(BaseSettings):
    LLM_API_KEY: str
    LLM_ENDPOINT: str
    class Config:
        env_file = ".env"

def get_settings():
    return Settings()

