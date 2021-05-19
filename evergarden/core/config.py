from pydantic import BaseSettings


class Settings(BaseSettings):
    API_URL_PREFIX = "/api"


settings = Settings()
