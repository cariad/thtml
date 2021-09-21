from typing import IO, Dict, List, TypedDict

from thtml.types import ClassName, PropertyName, PropertyValue


class ThemeClassRequiredDict(TypedDict):
    name: ClassName
    """CSS class name."""


class ThemeClassDict(ThemeClassRequiredDict, total=False):
    headers: List[str]
    """
    @imports, @keywords, etc, that this class requires at the top of the
    `<style>` block.
    """

    styles: Dict[PropertyName, PropertyValue]
    """ CSS class styles. """

    variables: List[str]
    """  Names of CSS variables that this class uses. """


class ThemeClass:
    """
    Represents a CSS class (either a default or pluckable) in a theme
    configuration dictionary.
    """

    def __init__(self, values: ThemeClassDict, is_default: bool = False) -> None:
        self.is_default = is_default
        self.values = values

    def add_style(self, name: PropertyName, value: PropertyValue) -> None:
        """Adds a style or variable."""

        try:
            self.values["styles"][name] = value
        except KeyError:
            self.values["styles"] = {}
            self.add_style(name, value)

    @property
    def is_styled(self) -> bool:
        return not not self.styles

    @property
    def styles(self) -> Dict[PropertyName, PropertyValue]:
        return self.values.get("styles", {})

    @property
    def headers(self) -> List[str]:
        """
        Gets the @imports, @keywords, etc, that this class requires at the top
        of the `<style>` block.
        """
        return self.values.get("headers", [])

    @property
    def name(self) -> str:
        """Gets the class name."""
        return self.values["name"]

    @property
    def variables(self) -> List[str]:
        """Gets the names of CSS variables that this class uses."""
        return self.values.get("variables", [])

    def write(self, writer: IO[str]) -> None:
        """Writes a `<style>` entry for this CSS class."""

        if not self.is_styled:
            return

        writer.write(f".{self.name} {{ ")
        for name in self.styles:
            writer.write(f"{name}: {self.styles[name]}; ")
        writer.write("}")
