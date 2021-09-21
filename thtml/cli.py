from importlib.resources import open_text
from tempfile import TemporaryFile
from typing import IO

from yaml import safe_load

from thtml.body_fragment import BodyFragment
from thtml.options import Scope
from thtml.scopes import ScopeHtmlParser
from thtml.theming import StyleFragment


def write(body: str, scope: Scope, writer: IO[str]) -> None:
    with open_text(__package__, "theme.yml") as t:
        theme_dict = safe_load(t)

    # Set any missing defaults:
    theme_dict["classes"] = theme_dict.get("classes", [])
    theme_dict["defaults"] = theme_dict.get("defaults", [])
    theme_dict["variables"] = theme_dict.get("variables", {})

    style_fragment = StyleFragment(theme_dict)
    body_fragment = BodyFragment(body=body, style=style_fragment)

    with TemporaryFile("a+") as body_io:
        with TemporaryFile("a+") as style_io:
            body_fragment.write(body_io)
            style_fragment.write(style_io)

            body_io.seek(0)
            style_io.seek(0)

            parser = ScopeHtmlParser(body_io=body_io, style_io=style_io, writer=writer)
            parser.render(scope)

            writer.flush()
