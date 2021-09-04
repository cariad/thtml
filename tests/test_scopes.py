from pytest import mark

from thtml.options import Scope
from thtml.scopes import get_template


@mark.parametrize(
    "scope, expect_len",
    [
        (Scope.DOCUMENT, 284),
        (Scope.FRAGMENT, 298),
    ],
)
def test_get_template(scope: Scope, expect_len: int) -> None:
    assert len(get_template(scope)) == expect_len
