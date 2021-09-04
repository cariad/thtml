from html.parser import HTMLParser
from importlib.resources import open_text
from typing import List, Optional, Tuple

from thtml.options import Scope

TAttribute = Tuple[str, Optional[str]]


class ScopeHtmlParser(HTMLParser):
    """Wraps `body` into a given scope."""

    def __init__(self, body: str) -> None:
        super().__init__()
        self.body = body
        self.minimized = ""
        self.path: List[str] = []

    def append(self, content: str) -> None:
        self.minimized += content.strip()

    @property
    def can_strip_newlines(self) -> bool:
        return "code" not in self.path

    @staticmethod
    def get_template(scope: Scope) -> str:
        """Gets a scope's template."""
        with open_text(__package__, f"{scope.value}.html") as t:
            return t.read().strip()

    def handle_data(self, data: str) -> None:
        if self.can_strip_newlines:
            data = data.replace("\n", "")

        if self.path and self.path[-1] == "style":
            while "  " in data:
                data = data.replace("  ", " ")

        self.append(data)

    def handle_decl(self, decl: str) -> None:
        self.append(f"<!{decl}>")

    def handle_endtag(self, tag: str) -> None:
        popped = self.path.pop()
        if popped != tag:
            raise ValueError(popped)

        self.append(f"</{tag}>")

    def handle_startendtag(self, tag: str, attrs: Optional[List[TAttribute]]) -> None:
        if tag == "thtml":
            if not attrs:
                raise ValueError("thtml tag requires attributes")
            attribute = attrs[0]
            if attribute[0] == "scope":
                content = self.render(scope=Scope(attrs[0][1]))
                self.append(content)
                return
            if attribute[0] == "body":
                self.append(self.body)
                return

            raise ValueError("unhandled thtml state")

        attributes = self.make_attributes(attrs) if attrs else ""
        inner = f"{tag} {attributes}".strip()
        self.append(f"<{inner} />")

    def handle_starttag(self, tag: str, attrs: Optional[List[TAttribute]]) -> None:
        attributes = self.make_attributes(attrs) if attrs else ""
        inner = f"{tag} {attributes}".strip()
        self.append(f"<{inner}>")
        self.path.append(tag)

    @staticmethod
    def make_attribute(attribute: TAttribute) -> str:
        return f'{attribute[0]}="{attribute[1]}"'

    @staticmethod
    def make_attributes(attributes: List[TAttribute]) -> str:
        return " ".join([ScopeHtmlParser.make_attribute(a) for a in attributes])

    def render(self, scope: Scope) -> str:
        template = self.get_template(scope)

        parser = ScopeHtmlParser(body=self.body)
        parser.feed(template)
        parser.close()
        return parser.minimized
