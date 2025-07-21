import json
from typing import Any

from cerberus import Validator

from src.common.exceptions import InvalidFieldValueError
from src.common.pokemon_type import POKEMON_TYPES


def pokemon_data_validator(request: Any) -> None:
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
