from html.parser import HTMLParser
from importlib.resources import open_text
from typing import IO, List, Optional, Tuple

from thtml.options import Scope

TAttribute = Tuple[str, Optional[str]]


class ScopeHtmlParser(HTMLParser):
    """
    Injects `body_io` and `style_io` into the HTML fragment of given scope.
    """

    def __init__(
        self,
        body_io: IO[str],
        style_io: IO[str],
        writer: IO[str],
    ) -> None:
        super().__init__()
        self.body_fragment = body_io
        self.path: List[str] = []
        self.style_fragment = style_io
        self.writer = writer
        self.nest_count = 0

    @staticmethod
    def get_template(scope: Scope) -> str:
        """Gets a scope's template."""
        with open_text(__package__, f"{scope.value}.html") as t:
            return t.read().strip()

    def handle_data(self, data: str) -> None:
        if "code" not in self.path:
            data = data.replace("\n", "")

        self.writer.write(data)

    def handle_decl(self, decl: str) -> None:
        self.writer.write(f"<!{decl}>")

    def handle_endtag(self, tag: str) -> None:
        popped = self.path.pop()
        if popped != tag:
            raise ValueError(f'expected to end "{popped}" but got "{tag}"')

        self.writer.write(f"</{tag}>")

    def handle_startendtag(self, tag: str, attrs: List[TAttribute]) -> None:
        if tag == "thtml":
            attribute = attrs[0]
            if attribute[0] == "scope":
                scope_str = attrs[0][1]
                self.render_child(scope=Scope(scope_str))
                return
            if attribute[0] == "body":
                self.writer.write(self.body_fragment.read())
                return
            if attribute[0] == "css":
                self.writer.write(self.style_fragment.read())
                return

            raise ValueError("unhandled thtml state")

        attributes = self.make_attributes(attrs) if attrs else ""
        inner = f"{tag} {attributes}".strip()
        self.writer.write(f"<{inner} />")

    def handle_starttag(self, tag: str, attrs: Optional[List[TAttribute]]) -> None:
        attributes = self.make_attributes(attrs) if attrs else ""
        inner = f"{tag} {attributes}".strip()
        self.writer.write(f"<{inner}>")
        self.path.append(tag)

    @staticmethod
    def make_attribute(attribute: TAttribute) -> str:
        return f'{attribute[0]}="{attribute[1]}"'

    @staticmethod
    def make_attributes(attributes: List[TAttribute]) -> str:
        return " ".join([ScopeHtmlParser.make_attribute(a) for a in attributes])

    def render_child(self, scope: Scope) -> None:
        parser = ScopeHtmlParser(
            body_io=self.body_fragment,
            style_io=self.style_fragment,
            writer=self.writer,
        )
        parser.render(scope)

    def render(self, scope: Scope) -> None:
        self.feed(self.get_template(scope))
        self.close()
