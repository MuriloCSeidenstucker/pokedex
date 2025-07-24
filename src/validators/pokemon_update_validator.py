import json
from typing import Any

from cerberus import Validator

from src.common.exceptions import InvalidFieldValueError
from src.common.pokemon_type import POKEMON_TYPES


def to_int_or_none(value):
    if value == "":
        return None
    return int(value)


def pokemon_update_validator(request: Any) -> None:
    validator = Validator(
        {
            "pokemon_id": {
                "type": "integer",
                "nullable": True,
                "coerce": to_int_or_none,
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
                "coerce": to_int_or_none,
            },
            "is_legendary": {
                "type": "integer",
                "nullable": True,
                "coerce": to_int_or_none,
            },
        }
    )

    response = validator.validate(request)

    if response is False:
        raise InvalidFieldValueError(json.dumps(validator.errors))
