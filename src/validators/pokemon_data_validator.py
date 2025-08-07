"""Validador dos dados de entrada para registro de um novo Pokémon.

Valida campos como nome, tipos, geração e se o Pokémon é lendário,
utilizando regras do Cerberus.
"""

import json
from typing import Any

from cerberus import Validator

from src.common.exceptions import InvalidFieldValueError
from src.common.pokemon_type import POKEMON_TYPES


def pokemon_data_validator(request: Any) -> None:
    """Valida os dados fornecidos para registro de um novo Pokémon.

    Espera um dicionário com os seguintes campos obrigatórios:
    - `pokemon_id` (int): ID numérico único do Pokémon.
    - `pkn_name` (str): Nome do Pokémon, apenas letras e espaços.
    - `type_1` (str): Tipo primário, deve estar na lista de tipos válidos.
    - `type_2` (str, opcional): Tipo secundário, também deve estar na lista ou string vazia.
    - `generation` (int): Geração à qual o Pokémon pertence.
    - `is_legendary` (int): Indicador se o Pokémon é lendário (0 ou 1).

    Regras adicionais:
    - `type_1` e `type_2` são validados com base na lista `POKEMON_TYPES`.
    - Coerção de strings para inteiros onde aplicável.
    - Nome deve conter apenas letras e espaços (regex).

    Args:
        request (Any): Dicionário contendo os dados do Pokémon.

    Raises:
        InvalidFieldValueError: Se qualquer campo for inválido segundo o schema.
    """
    validator = Validator(
        {
            "pokemon_id": {
                "type": "integer",
                "coerce": int,
                "required": True,
                "empty": False,
            },
            "pkn_name": {
                "type": "string",
                "required": True,
                "empty": False,
                "regex": "^[A-Za-z ]+$",
            },
            "type_1": {
                "type": "string",
                "required": True,
                "empty": False,
                "allowed": POKEMON_TYPES,
            },
            "type_2": {"type": "string", "allowed": POKEMON_TYPES + [""]},
            "generation": {
                "type": "integer",
                "coerce": int,
                "required": True,
                "empty": False,
            },
            "is_legendary": {
                "type": "integer",
                "coerce": int,
                "required": True,
                "empty": False,
            },
        }
    )

    response = validator.validate(request)

    if response is False:
        raise InvalidFieldValueError(json.dumps(validator.errors))
