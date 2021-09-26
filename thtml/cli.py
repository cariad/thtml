from tempfile import TemporaryFile
from typing import IO, Optional, Union

from yaml import safe_load

from thtml.body_fragment import BodyFragment
from thtml.options import Scope
from thtml.scopes import ScopeHtmlParser
from thtml.themes import load_package_theme
from thtml.theming import StyleFragment, Theme


def load_theme(source: Optional[str]) -> Theme:
    if source is None:
        theme_dict = load_package_theme()
    else:
        with open(source, "r") as t:
            theme_dict = safe_load(t)

    # Set any missing defaults:
    theme_dict["classes"] = theme_dict.get("classes", [])
    theme_dict["defaults"] = theme_dict.get("defaults", [])
    theme_dict["variables"] = theme_dict.get("variables", {})
    return theme_dict


def write_html(
    text: str,
    writer: IO[str],
    theme: Optional[Union[str, Theme]] = None,
    scope: Scope = Scope.DOCUMENT,
) -> None:
    """
    Translates `text` to HTML and writes a fragment of `scope` to `writer` using
    theme `theme`.
    """

    if not isinstance(theme, dict):
        theme = load_theme(theme)

    style_fragment = StyleFragment(theme)
    body_fragment = BodyFragment(body=text, style=style_fragment)

    with TemporaryFile("a+") as body_io:
        with TemporaryFile("a+") as style_io:
            body_fragment.write(body_io)
            style_fragment.write(style_io)

            body_io.seek(0)
            style_io.seek(0)

            parser = ScopeHtmlParser(body_io=body_io, style_io=style_io, writer=writer)
            parser.render(scope)

            writer.flush()
