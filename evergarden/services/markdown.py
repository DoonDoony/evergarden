import uuid
from pathlib import Path

import markdown
from fastapi import UploadFile

from evergarden.core.config import settings
from evergarden.utils.aws.s3 import S3


class MarkdownService:

    s3 = S3(settings.AWS_S3_ASSET_BUCKET_NAME)
    md = markdown.Markdown(extensions=settings.MARKDOWN_EXTENSIONS)

    def to_html(self, text: str) -> str:
        return self.md.convert(text)

    async def upload_to_s3(self, file: UploadFile) -> str:
        extensions = Path(file.filename).suffix
        key = uuid.uuid4().hex + extensions
        return await self.s3.upload(key, file)


markdown_service = MarkdownService()
