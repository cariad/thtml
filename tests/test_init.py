from pytest import mark

from tests import get_render_cases
from thtml import Scope, render


@mark.parametrize("body, scope, expect", get_render_cases())
def test_render(body: str, scope: Scope, expect: str) -> None:
    assert render(body, scope) == expect
