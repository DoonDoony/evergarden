from typing import List

from pydantic import BaseSettings


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


settings = Settings()
