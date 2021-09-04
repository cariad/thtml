from enum import Enum
from typing import TypedDict


class Scope(Enum):
    DOCUMENT = "document"
    FRAGMENT = "fragment"


class Options(TypedDict):
    scope: Scope
