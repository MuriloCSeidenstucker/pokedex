# pylint: disable=C0103:invalid-name

from dataclasses import dataclass


@dataclass
class By:
    ID: str = "id"
    NAME: str = "name"
