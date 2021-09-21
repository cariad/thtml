from io import StringIO
from typing import List

from pytest import mark

from thtml.theming.style_fragment import StyleFragment
from thtml.theming.theme import ThemeDict
from thtml.theming.theme_class import ThemeClassDict


@mark.parametrize(
    "theme, expect",
    [
        ({"defaults": []}, ""),
        (
            {"defaults": [{"name": "foo", "styles": {"one": "1"}}]},
            '<style type="text/css">.foo { one: 1; }</style>',
        ),
    ],
)
def test_init(theme: ThemeDict, expect: str) -> None:
    fragment = StringIO()
    StyleFragment(theme).write(fragment)
    assert fragment.getvalue() == expect


@mark.parametrize(
    "theme, classes, expect",
    [
        (
            {"defaults": [], "variables": {}},
            [{"name": "foo"}],
            "",
        ),
        (
            {"defaults": [], "variables": {}},
            [
                {
                    "name": "foo",
                    "styles": {"one": "1"},
                }
            ],
            '<style type="text/css">.foo { one: 1; }</style>',
        ),
        (
            {"defaults": [], "variables": {}},
            [
                {"name": "foo"},
                {
                    "name": "bar",
                    "styles": {"one": "1"},
                },
            ],
            '<style type="text/css">.bar { one: 1; }</style>',
        ),
        (
            {"defaults": [], "variables": {}},
            [
                {
                    "name": "foo",
                    "styles": {"one": "1"},
                },
                {
                    "name": "bar",
                    "styles": {"two": "2"},
                },
            ],
            '<style type="text/css">.foo { one: 1; } .bar { two: 2; }</style>',
        ),
        (
            {"defaults": [], "variables": {"variable-1": "value-1"}},
            [
                {"name": "foo", "variables": ["variable-1"]},
                {
                    "name": "bar",
                    "styles": {"two": "2"},
                },
            ],
            '<style type="text/css">.foo { --variable-1: value-1; } .bar { two: 2; }</style>',
        ),
        (
            {"defaults": [], "variables": {"variable-1": "value-1"}},
            [
                {"name": "foo", "styles": {"one": "1"}, "variables": ["variable-1"]},
                {
                    "name": "bar",
                    "styles": {"two": "2"},
                },
            ],
            '<style type="text/css">.foo { one: 1; --variable-1: value-1; } .bar { two: 2; }</style>',
        ),
        (
            {"defaults": [], "variables": {"variable-1": "value-1"}},
            [
                {"name": "foo", "styles": {"one": "1"}},
                {
                    "name": "bar",
                    "styles": {"two": "2"},
                    "variables": ["variable-1"],
                },
            ],
            '<style type="text/css">.foo { one: 1; --variable-1: value-1; } .bar { two: 2; }</style>',
        ),
        (
            {"defaults": [], "variables": {}},
            [
                {"name": "foo", "headers": ["header-1;"]},
                {
                    "name": "bar",
                    "styles": {"two": "2"},
                    "headers": ["header-1;"],
                },
            ],
            '<style type="text/css">header-1; .bar { two: 2; }</style>',
        ),
    ],
)
def test_add_class(
    theme: ThemeDict,
    classes: List[ThemeClassDict],
    expect: str,
) -> None:
    sf = StyleFragment(theme)

    for c in classes:
        sf.add_class(values=c)

    fragment = StringIO()
    sf.write(fragment)
    assert fragment.getvalue() == expect


@mark.parametrize(
    "classes, name, expect",
    [
        ([], "foo", None),
        ([{"name": "foo"}], "foo", {"name": "foo"}),
        ([{"name": "foo"}, {"name": "bar"}], "bar", {"name": "bar"}),
    ],
)
def test_find_class(
    classes: List[ThemeClassDict],
    name: str,
    expect: ThemeClassDict,
) -> None:
    theme: ThemeDict = {"defaults": [], "classes": classes, "variables": {}}
    assert StyleFragment(theme).find_class(name) == expect


@mark.parametrize(
    "classes, expect",
    [
        ([], False),
        ([{"name": "foo"}], False),
        ([{"name": "foo", "headers": ["header-1"]}], False),
        ([{"name": "foo", "styles": {"one": "1"}}], True),
        ([{"name": "foo", "variables": ["variable-1"]}], True),
    ],
)
def test_has_classes(classes: List[ThemeClassDict], expect: bool) -> None:
    sf = StyleFragment(
        {
            "defaults": [],
            "classes": [],
            "variables": {"variable-1": "value-1"},
        },
    )
    for c in classes:
        sf.add_class(values=c)
    assert sf.has_classes == expect


@mark.parametrize(
    "theme, name, expect",
    [
        (
            {
                "defaults": [],
                "classes": [{"name": "foo", "styles": {"one": "1"}}],
            },
            "bar",
            "",
        ),
        (
            {
                "defaults": [],
                "classes": [{"name": "foo", "styles": {"one": "1"}}],
            },
            "foo",
            '<style type="text/css">.foo { one: 1; }</style>',
        ),
    ],
)
def test_use_class(theme: ThemeDict, name: str, expect: str) -> None:
    sf = StyleFragment(theme)
    sf.use_class(name)
    fragment = StringIO()
    sf.write(fragment)
    assert fragment.getvalue() == expect


def test_write() -> None:
    sf = StyleFragment(
        {
            "defaults": [],
            "classes": [],
            "variables": {
                "variable-1": "value-1",
                "variable-2": "value-2",
            },
        }
    )
    sf.add_class(
        values={
            "headers": ["header-1;"],
            "name": "foo",
            "styles": {
                "a": "b",
            },
            "variables": ["variable-1"],
        },
    )
    sf.add_class(
        values={
            "headers": ["header-2;"],
            "name": "bar",
            "styles": {
                "c": "d",
            },
            "variables": ["variable-2"],
        },
    )

    fragment = StringIO()
    sf.write(fragment)
    assert (
        fragment.getvalue()
        == '<style type="text/css">header-1; header-2; .foo { a: b; --variable-1: value-1; --variable-2: value-2; } .bar { c: d; }</style>'
    )
