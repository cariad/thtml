from pytest import mark

from tests import get_render_cases
from thtml.options import Scope
from thtml.scopes import ScopeHtmlParser


@mark.parametrize(
    "scope, expect_len",
    [
        (Scope.DOCUMENT, 289),
        (Scope.FRAGMENT, 295),
    ],
)
def test_get_template(scope: Scope, expect_len: int) -> None:
    assert len(ScopeHtmlParser.get_template(scope)) == expect_len


@mark.parametrize("body, scope, expect", get_render_cases())
def test_render(body: str, scope: Scope, expect: str) -> None:
    assert ScopeHtmlParser(body).render(scope) == expect
