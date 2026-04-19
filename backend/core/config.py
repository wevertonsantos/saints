from typing import List
from pydantic_settings import BaseSettings
from pydantic import field_validator

class Settings(BaseSettings):
    GROQ_API_KEY: str

    RSS_URL: str
    RSS_TAGS: str = ""

    @field_validator("RSS_TAGS")
    def parse_rss_tags(cls, v: str) -> list:
        return v.split(",") if v else []

    API_PREFIX: str = "/api"
    DEBUG: bool = False

    DATABASE_URL: str

    ALLOWED_ORIGINS: str = ""

    @field_validator("ALLOWED_ORIGINS")
    def parse_allowed_origins(cls,v: str) -> List[str]:
        return v.split(",") if v else []
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

settings = Settings()