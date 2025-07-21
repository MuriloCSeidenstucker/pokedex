from typing import Optional


class PokedexBaseError(Exception):

    def __init__(self, msg: Optional[str] = "an unknown error was raised") -> None:
        super().__init__(msg)
        self.msg = msg
        self.name = "unknown error"
        self.status_code = 1


class InvalidFieldValueError(PokedexBaseError):
    def __init__(self, msg: str = "invalid field value provided") -> None:
        super().__init__(msg)
        self.name = "invalid field value"
        self.status_code = 2


class MissingRequiredFieldError(PokedexBaseError):
    def __init__(self, msg: str = "a required field is missing") -> None:
        super().__init__(msg)
        self.name = "missing required field"
        self.status_code = 3


class PokemonNotFoundError(PokedexBaseError):
    def __init__(self, msg: str = "pokemon not found in repository") -> None:
        super().__init__(msg)
        self.name = "pokemon not found"
        self.status_code = 4


class DuplicatePokemonError(PokedexBaseError):
    def __init__(self, msg: str = "pokemon already exists in repository") -> None:
        super().__init__(msg)
        self.name = "duplicate pokemon"
        self.status_code = 5
