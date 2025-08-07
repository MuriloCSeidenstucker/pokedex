"""Validador dos dados de entrada para atualização parcial de um Pokémon.

Permite que o usuário atualize apenas os campos desejados.
Trata campos opcionais com valores nulos e coerção de strings vazias.
"""

import json
from typing import Any

from cerberus import Validator

from src.common.exceptions import InvalidFieldValueError
from src.common.pokemon_type import POKEMON_TYPES


def __to_int_or_none(value):
    """Converte o valor para inteiro ou retorna None se for string vazia."""
    if value == "":
        return None
    return int(value)


def pokemon_update_validator(request: Any) -> None:
    """Valida os dados fornecidos para atualização parcial de um Pokémon.

    Diferente do validador de criação, todos os campos aqui são opcionais.
    Permite que o usuário envie apenas os dados que deseja modificar.

    Campos aceitos:
    - `pokemon_id` (int | None): Novo ID do Pokémon.
    - `pkn_name` (str | None): Novo nome, apenas letras e espaços.
    - `type_1` (str | None): Tipo primário, deve estar na lista de tipos válidos.
    - `type_2` (str | None): Tipo secundário, também deve estar na lista.
    - `generation` (int | None): Geração à qual o Pokémon pertence.
    - `is_legendary` (int | None): Indicador se o Pokémon é lendário (0 ou 1).

    Regras aplicadas:
    - Todos os campos são opcionais e aceitam `None` como valor.
    - Strings vazias são convertidas para `None` onde aplicável.
    - Tipos são coeridos automaticamente quando necessário.

    Args:
        request (Any): Dicionário contendo os dados a serem atualizados.

    Raises:
        InvalidFieldValueError: Se algum campo informado for inválido.
    """
    validator = Validator(
        {
            "pokemon_id": {
                "type": "integer",
                "nullable": True,
                "coerce": __to_int_or_none,
            },
            "pkn_name": {"type": "string", "nullable": True, "regex": "^[A-Za-z ]+$"},
            "type_1": {
                "type": "string",
                "nullable": True,
                "allowed": POKEMON_TYPES + [""],
            },
            "type_2": {
                "type": "string",
                "nullable": True,
                "allowed": POKEMON_TYPES + [""],
            },
            "generation": {
                "type": "integer",
                "nullable": True,
                "coerce": __to_int_or_none,
            },
            "is_legendary": {
                "type": "integer",
                "nullable": True,
                "coerce": __to_int_or_none,
            },
        }
    )

    response = validator.validate(request)

    if response is False:
        raise InvalidFieldValueError(json.dumps(validator.errors))
