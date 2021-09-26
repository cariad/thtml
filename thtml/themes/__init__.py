from importlib.resources import open_text
from typing import cast

from yaml import safe_load

from thtml.theming import Theme


def load_package_theme() -> Theme:
    with open_text(__package__, "default.yml") as t:
        theme_dict = safe_load(t)
    return cast(Theme, theme_dict)
