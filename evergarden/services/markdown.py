import markdown

from evergarden.core.config import settings


class MarkdownService:

    md = markdown.Markdown(extensions=settings.MARKDOWN_EXTENSIONS)

    def to_html(self, text: str) -> str:
        return self.md.convert(text)


markdown_service = MarkdownService()
