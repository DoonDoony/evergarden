from pathlib import Path
from typing import List

from pydantic import BaseSettings, Field, HttpUrl

BASE_DIR = Path(__file__)
ROOT_DIR = BASE_DIR.parents[2]  # Same as parent.parent.parent


class Settings(BaseSettings):
    API_URL_PREFIX = "/api"
    MARKDOWN_EXTENSIONS: List[str] = [
        "pymdownx.betterem",
        "pymdownx.caret",
        "pymdownx.details",
        "pymdownx.emoji",
        "pymdownx.inlinehilite",
        "pymdownx.keys",
        "pymdownx.magiclink",
        "pymdownx.mark",
        "pymdownx.progressbar",
        "pymdownx.smartsymbols",
        "pymdownx.striphtml",
        "pymdownx.superfences",
        "pymdownx.tabbed",
        "pymdownx.tasklist",
        "pymdownx.tilde",
    ]
    # AWS Settings
    AWS_S3_ASSET_BUCKET_NAME: str = Field(env="AWS_S3_ASSET_BUCKET_NAME")
    AWS_REGION: str = Field(env="AWS_REGION")
    USE_CLOUDFRONT_FOR_S3_BUCKET: bool = Field(env="USE_CLOUDFRONT_FOR_S3_BUCKET")

    # Domains
    BASE_URL: HttpUrl = Field(env="BASE_URL")
    MEDIA_URL: HttpUrl = Field(env="MEDIA_URL")

    class Config:
        env_file = ROOT_DIR / ".env.production"


settings = Settings()
