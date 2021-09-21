from typing import Dict, List, TypedDict

from thtml.theming.theme_class import ThemeClassDict
from thtml.types import VariableName, VariableValue


class ThemeDict(TypedDict):
    classes: List[ThemeClassDict]
    """Classes available to be added to a style block as-needed."""

    defaults: List[ThemeClassDict]
    """Classes to always add to a style block."""

    variables: Dict[VariableName, VariableValue]
    """Variables available to be added to a style block as-needed."""
