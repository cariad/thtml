from thtml.options import Scope
from thtml.scopes import ScopeHtmlParser
from thtml.version import get_version


def render(body: str, scope: Scope = Scope.DOCUMENT) -> str:
    return ScopeHtmlParser(body).render(scope)


__all__ = ["get_version", "Scope"]
