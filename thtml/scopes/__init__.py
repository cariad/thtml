from importlib.resources import open_text

from thtml.options import Scope


def get_template(scope: Scope) -> str:
    """Gets a scope's template."""
    with open_text(__package__, f"{scope.value}.html") as t:
        return t.read().strip()
