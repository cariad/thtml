from io import StringIO
from typing import Dict, List

from pytest import mark

from thtml.theming.theme_class import ThemeClass, ThemeClassDict
from thtml.types import PropertyName, PropertyValue


@mark.parametrize(
    "values, expect",
    [
        ({}, {"foo": "bar"}),
        ({"styles": {}}, {"foo": "bar"}),
        ({"styles": {"woo": "boo"}}, {"foo": "bar", "woo": "boo"}),
    ],
)
def test_add_style(
    values: ThemeClassDict,
    expect: Dict[PropertyName, PropertyValue],
) -> None:
    tc = ThemeClass(values=values)
    tc.add_style("foo", "bar")
    assert tc.styles == expect


@mark.parametrize(
    "values, expect",
    [
        ({}, []),
        ({"variables": ["foo"]}, ["foo"]),
    ],
)
def test_variables(values: ThemeClassDict, expect: List[str]) -> None:
    assert ThemeClass(values=values).variables == expect


@mark.parametrize(
    "values, expect",
    [
        ({}, []),
        ({"headers": ["foo"]}, ["foo"]),
    ],
)
def test_headers(values: ThemeClassDict, expect: List[str]) -> None:
    assert ThemeClass(values=values).headers == expect


@mark.parametrize(
    "values, expect",
    [
        (
            {
                "name": "foo",
            },
            "",
        ),
        (
            {
                "name": "foo",
                "styles": {
                    "one": "1",
                    "two": "2",
                    "three": "3",
                },
            },
            ".foo { one: 1; two: 2; three: 3; }",
        ),
    ],
)
def test_write(values: ThemeClassDict, expect: str) -> None:
    fragment = StringIO()
    ThemeClass(values).write(fragment)
    assert fragment.getvalue() == expect
