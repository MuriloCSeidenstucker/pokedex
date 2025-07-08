# pylint: disable=C0103:invalid-name

from dataclasses import dataclass


@dataclass
class By:
    ID: str = "id"
    NAME: str = "name"

    ByType = ["id", "name"]

    def __contains__(self, value):
        return value in self.ByType
