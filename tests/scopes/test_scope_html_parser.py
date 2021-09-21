from io import StringIO
from typing import List

from pytest import mark, raises

from thtml.options import Scope
from thtml.scopes import ScopeHtmlParser


@mark.parametrize(
    "scope, expect_len",
    [
        (Scope.DOCUMENT, 242),
        (Scope.FRAGMENT, 164),
    ],
)
def test_get_template(scope: Scope, expect_len: int) -> None:
    assert len(ScopeHtmlParser.get_template(scope)) == expect_len


@mark.parametrize(
    "path, data, expect",
    [
        ([], "foo\nbar", "foobar"),
        (["code"], "foo\nbar", "foo\nbar"),
    ],
)
def test_handle_data(path: List[str], data: str, expect: str) -> None:
    writer = StringIO()
    p = ScopeHtmlParser(body_io=StringIO(), style_io=StringIO(), writer=writer)
    p.path = path
    p.handle_data(data)
    assert writer.getvalue() == expect


def test_handle_decl() -> None:
    writer = StringIO()
    p = ScopeHtmlParser(body_io=StringIO(), style_io=StringIO(), writer=writer)
    p.handle_decl("foo")
    assert writer.getvalue() == "<!foo>"


def test_handle_endtag__ok() -> None:
    writer = StringIO()
    p = ScopeHtmlParser(body_io=StringIO(), style_io=StringIO(), writer=writer)
    p.path = ["foo"]
    p.handle_endtag("foo")
    assert writer.getvalue() == "</foo>"


def test_handle_endtag__fail() -> None:
    writer = StringIO()
    p = ScopeHtmlParser(body_io=StringIO(), style_io=StringIO(), writer=writer)
    p.path = ["foo"]
    with raises(ValueError):
        p.handle_endtag("bar")


def test_handle_startendtag__body() -> None:
    body_io = StringIO("this is the body")
    writer = StringIO()
    p = ScopeHtmlParser(body_io=body_io, style_io=StringIO(), writer=writer)
    p.handle_startendtag("thtml", [("body", None)])
    assert writer.getvalue() == "this is the body"


def test_handle_startendtag__css() -> None:
    style_io = StringIO("this is the css")
    writer = StringIO()
    p = ScopeHtmlParser(body_io=StringIO(), style_io=style_io, writer=writer)
    p.handle_startendtag("thtml", [("css", None)])
    assert writer.getvalue() == "this is the css"


def test_handle_startendtag__html() -> None:
    writer = StringIO()
    p = ScopeHtmlParser(body_io=StringIO(), style_io=StringIO(), writer=writer)
    p.handle_startendtag("foo", [("woo", "boo")])
    assert writer.getvalue() == '<foo woo="boo" />'


def test_handle_startendtag__invalid() -> None:
    writer = StringIO()
    p = ScopeHtmlParser(body_io=StringIO(), style_io=StringIO(), writer=writer)
    with raises(ValueError):
        p.handle_startendtag("thtml", [("nope", None)])


def test_handle_startendtag__scope() -> None:
    body_io = StringIO("this is the body")
    style_io = StringIO("this is the css")
    writer = StringIO()
    p = ScopeHtmlParser(body_io=body_io, style_io=style_io, writer=writer)
    p.handle_startendtag("thtml", [("scope", "fragment")])
    assert (
        writer.getvalue()
        == 'this is the css<pre class="nohighlight thtml"><code class="thtml-code">this is the body</code></pre>'
    )
