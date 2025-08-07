"""Define exceções personalizadas utilizadas na aplicação Pokédex.

Cada exceção herda de `PokedexBaseError`, que fornece uma estrutura comum 
para mensagens, nome do erro e código de status.
"""

from typing import Optional


class PokedexBaseError(Exception):
    """Classe base para todas as exceções da Pokédex.

    Atributos:
        msg (str): Mensagem descritiva do erro.
        name (str): Nome legível do tipo de erro.
        status_code (int): Código numérico associado ao erro.
    """

    def __init__(self, msg: Optional[str] = "an unknown error was raised") -> None:
        super().__init__(msg)
        self.msg = msg
        self.name = "unknown error"
        self.status_code = 1


class InvalidFieldValueError(PokedexBaseError):
    """Erro lançado quando um campo contém um valor inválido."""

    def __init__(self, msg: str = "invalid field value provided") -> None:
        super().__init__(msg)
        self.name = "invalid field value"
        self.status_code = 2


class MissingRequiredFieldError(PokedexBaseError):
    """Erro lançado quando um campo obrigatório não é fornecido."""

    def __init__(self, msg: str = "a required field is missing") -> None:
        super().__init__(msg)
        self.name = "missing required field"
        self.status_code = 3


class PokemonNotFoundError(PokedexBaseError):
    """Erro lançado quando o Pokémon solicitado não é encontrado."""

    def __init__(self, msg: str = "pokemon not found in repository") -> None:
        super().__init__(msg)
        self.name = "pokemon not found"
        self.status_code = 4


class DuplicatePokemonError(PokedexBaseError):
    """Erro lançado quando se tenta registrar um Pokémon que já existe."""

    def __init__(self, msg: str = "pokemon already exists in repository") -> None:
        super().__init__(msg)
        self.name = "duplicate pokemon"
        self.status_code = 5
