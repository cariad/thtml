from io import StringIO
from typing import Any

from ansiscape.enums import Weight
from ansiscape.types import RGBA, Interpretation
from pytest import mark

from thtml.body_fragment import BodyFragment
from thtml.theming.style_fragment import StyleFragment


@mark.parametrize(
    "value, expect",
    [
        ("foo", "foo"),
        ("Foo", "foo"),
        ("fooBar", "foo-bar"),
        ("FooBar", "foo-bar"),
        ("foo_bar", "foo-bar"),
    ],
)
def test_kebab(value: str, expect: str) -> None:
    assert BodyFragment.kebab(value) == expect


@mark.parametrize(
    "color, key, expect",
    [
        ((0, 0, 0, 0), "background", "background: rgba(0%, 0%, 0%, 0);"),
        (
            (0.2, 0.3, 0.4, 0.5),
            "background",
            "background: rgba(20.0%, 30.0%, 40.0%, 0.5);",
        ),
        ((1, 1, 1, 1), "foreground", "color: rgba(100%, 100%, 100%, 1);"),
    ],
)
def test_make_rgba(color: RGBA, key: str, expect: str) -> None:
    assert BodyFragment.make_rgba(color, key) == expect


@mark.parametrize(
    "key, name, expect",
    [
        ("foo", "bar", "foo-bar"),
        ("foo", Weight.HEAVY, "foo-heavy"),
    ],
)
def test_to_class_name(key: str, name: Any, expect: str) -> None:
    assert BodyFragment.to_class_name(key, name) == expect


def test_write() -> None:
    style = StyleFragment(
        {
            "defaults": [],
            "classes": [
                {
                    "name": "weight-heavy",
                    "styles": {"font-weight": "bold"},
                },
            ],
            "variables": {},
        }
    )
    writer = StringIO()
    BodyFragment("\033[1mHello, world!\033[22m", style).write(writer)
    assert (
        writer.getvalue()
        == '<span class="weight-heavy">Hello, world!</span><span class="weight-normal"></span>'
    )


def test_write__no_formatting() -> None:
    style = StyleFragment(
        {
            "defaults": [],
            "classes": [],
            "variables": {},
        }
    )
    writer = StringIO()
    BodyFragment("Hello, world!", style).write(writer)
    assert writer.getvalue() == "Hello, world!"


@mark.parametrize(
    "interpretation, expect_body, expect_style",
    [
        (
            {"background": (0, 0, 0, 0)},
            '<span style="background: rgba(0%, 0%, 0%, 0);">',
            "",
        ),
        (
            {"weight": Weight.LIGHT},
            '<span class="weight-light">',
            '<style type="text/css">.weight-light { font-weight: light; }</style>',
        ),
    ],
)
def test_write_span(
    interpretation: Interpretation,
    expect_body: str,
    expect_style: str,
) -> None:
    style = StyleFragment(
        {
            "defaults": [],
            "classes": [
                {
                    "name": "weight-light",
                    "styles": {"font-weight": "light"},
                },
            ],
            "variables": {},
        }
    )
    writer = StringIO()
    BodyFragment("body", style).write_span(interpretation, writer)
    assert writer.getvalue() == expect_body
    writer = StringIO()
    style.write(writer)
    assert writer.getvalue() == expect_style
