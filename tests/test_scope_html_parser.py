from pytest import mark

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


@mark.parametrize(
    "scope, expect",
    [
        (
            Scope.DOCUMENT,
            """<!doctype html><html><head><meta charset="utf-8" /><meta name="viewport" content="width=device-width, initial-scale=1" /><title>cariad/thtml</title><meta name="author" content="cariad/thtml" /></head><body><style type="text/css">.thtml { font-family: monospace; } .thtml .fg-red { color: #f00; } .thtml .fg-green { color: #0f0; }</style><pre class="nohighlight thtml"><code>foo\nbar</code></pre></body></html>""",
        ),
        (
            Scope.FRAGMENT,
            """<style type="text/css">.thtml { font-family: monospace; } .thtml .fg-red { color: #f00; } .thtml .fg-green { color: #0f0; }</style><pre class="nohighlight thtml"><code>foo\nbar</code></pre>""",
        ),
    ],
)
def test_render(scope: Scope, expect: str) -> None:
    assert ScopeHtmlParser("foo\nbar").render(scope) == expect
