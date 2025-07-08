# pylint: disable=C0103:invalid-name

from dataclasses import dataclass
from typing import Literal


@dataclass
class By:
    ID: str = "id"
    NAME: str = "name"

    ByType = Literal["id", "name"]

    def __contains__(self, value):
        return value in self.ByType
