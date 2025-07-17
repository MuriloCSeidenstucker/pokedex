from typing import Optional


class PokedexBaseError(Exception):

    def __init__(self, msg: Optional[str] = "an unknown error was raised") -> None:
        super().__init__(msg)
        self.msg = msg
        self.name = "unknown error"
        self.status_code = 1


class InvalidFieldValueError(PokedexBaseError):
    def __init__(self, msg="an unknown error was raised"):
        super().__init__(msg)
        self.name = "invalid field value"
        self.status_code = 2


class MissingRequiredFieldError(PokedexBaseError):
    def __init__(self, msg="an unknown error was raised"):
        super().__init__(msg)
        self.name = "missing required field"
        self.status_code = 3


class PokemonNotFoundError(PokedexBaseError):
    def __init__(self, msg="an unknown error was raised"):
        super().__init__(msg)
        self.name = "pokemon not found"
        self.status_code = 4
