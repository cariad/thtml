from importlib.resources import open_text
from typing import cast

from yaml import safe_load

from thtml.theming import Theme


def load_package_theme(filename: str) -> Theme:
    with open_text(__package__, filename) as t:
        theme_dict = safe_load(t)
    return cast(Theme, theme_dict)
