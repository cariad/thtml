from typing import IO, Dict, List, Optional

from thtml.theming.theme import ThemeDict
from thtml.theming.theme_class import ThemeClass, ThemeClassDict
from thtml.types import VariableName, VariableValue


class StyleFragment:
    """Describes a `<style>...</style>` HTML fragment."""

    def __init__(self, theme: ThemeDict) -> None:

        self.headers: List[str] = []
        """@import, @keyframes, etc. to inject at the top of the block."""

        self._classes: List[ThemeClass] = []
        """Classes and their styles to add to the block."""

        self._variables: Dict[VariableName, VariableValue] = {}
        """  CSS variable declarations to inject into the first class. """

        self.theme = theme

        for default_class in self.theme["defaults"]:
            self.add_class(is_default=True, values=default_class)

    def add_class(self, values: ThemeClassDict, is_default: bool = False) -> None:
        """Adds a CSS class."""

        theme_class = ThemeClass(is_default=is_default, values=values)
        self._classes.append(theme_class)

        for name in theme_class.variables:
            self._classes[0].add_style(
                f"--{name}",
                self.theme["variables"][name],
            )

        for header in theme_class.headers:
            if header not in self.headers:
                self.headers.append(header)

    def find_class(self, name: str) -> Optional[ThemeClassDict]:
        for c in self.theme["classes"]:
            if c["name"] == name:
                return c
        return None

    @property
    def has_classes(self) -> bool:
        """Returns `True` if any styled classes have been added."""
        for c in self._classes:
            if c.is_styled:
                return True
        return False

    def use_class(self, name: str) -> None:
        if theme_class_dict := self.find_class(name):
            self.add_class(values=theme_class_dict)

    def write(self, writer: IO[str]) -> None:
        if not self.headers and not self.has_classes:
            return

        writer.write('<style type="text/css">')

        is_first = True

        for header in self.headers:
            if is_first:
                is_first = False
            else:
                writer.write(" ")
            writer.write(header)

        for theme_class in self._classes:
            if not theme_class.is_styled:
                continue
            if is_first:
                is_first = False
            else:
                writer.write(" ")
            theme_class.write(writer)

        writer.write("</style>")
