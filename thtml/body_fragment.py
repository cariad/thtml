from enum import Enum
from typing import IO, Any, List, cast

from ansiscape import Interpretation, Sequence
from ansiscape.types import RGBA

from thtml.theming.style_fragment import StyleFragment


class BodyFragment:
    def __init__(self, body: str, style: StyleFragment) -> None:
        self.body = body
        self.style = style

    @staticmethod
    def kebab(value: str) -> str:
        wip = ""
        prev_was_lower = False
        for c in value:
            if c == "_":
                c = "-"
            if str.isupper(c) and prev_was_lower:
                wip += "-"
            prev_was_lower = str.islower(c)
            wip += str.lower(c)

        return wip

    @staticmethod
    def make_rgba(color: RGBA, key: str) -> str:
        prop_name = "background" if key == "background" else "color"
        r = color[0] * 100
        g = color[1] * 100
        b = color[2] * 100
        return f"{prop_name}: rgba({r}%, {g}%, {b}%, {color[3]});"

    @staticmethod
    def to_class_name(key: str, name: Any) -> str:
        if isinstance(name, Enum):
            return BodyFragment.kebab(key) + "-" + BodyFragment.kebab(name.name)
        return BodyFragment.kebab(key) + "-" + BodyFragment.kebab(str(name))

    def write(self, writer: IO[str]) -> None:
        sequence = Sequence(self.body)

        # is_first_span = True
        has_open_span = False

        for resolution in sequence.resolved:
            if isinstance(resolution, str):
                while "\n" in resolution:
                    resolution.replace("\n", "<br />")
                while "<br /> " in resolution:
                    resolution.replace("<br /> ", "<br /> &nbsp;")

                writer.write(resolution)
                continue

            if has_open_span:
                writer.write("</span>")
                has_open_span = False

            if self.write_span(resolution, writer):
                has_open_span = True

        if has_open_span:
            writer.write("</span>")

    def write_span(self, interpretation: Interpretation, writer: IO[str]) -> bool:
        """
        Attempts to writes a `<span>` element for the given interpretation. Will
        not write a `<span>` if the interpretation uses a class that isn't
        defined in the theme. Returns `False` if a span was not written.
        """

        classes: List[str] = []
        styles: List[str] = []

        for key in interpretation:
            value = interpretation[key]  # type: ignore

            if key in ["background", "foreground"] and isinstance(value, tuple):
                styles.append(BodyFragment.make_rgba(color=cast(RGBA, value), key=key))
            else:
                class_name = BodyFragment.to_class_name(key, value)
                if self.style.use_class(class_name):
                    classes.append(class_name)

        if not classes and not styles:
            return False

        writer.write("<span")

        if classes:
            writer.write(f' class="{" ".join(classes)}"')

        if styles:
            writer.write(f' style="{" ".join(styles)}"')

        writer.write(">")
        return True
