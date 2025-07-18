import json
from typing import Any

from cerberus import Validator

from src.common.exceptions import InvalidFieldValueError


def pokemon_register_validator(request: Any) -> None:
    validator = Validator(
        {
            "pokemon_id": {
                "type": "integer",
                "coerce": int,
                "required": True,
                "empty": False,
            },
            "pkn_name": {"type": "string", "required": True, "empty": False},
            "type_1": {"type": "string", "required": True, "empty": False},
            "type_2": {"type": "string"},
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
