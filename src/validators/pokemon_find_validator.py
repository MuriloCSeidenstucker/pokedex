import json
from typing import Any

from cerberus import Validator

from src.common.exceptions import MissingRequiredFieldError


def pokemon_find_validator(request: Any):
    validator = Validator(
        {
            "by": {
                "type": "string",
                "required": True,
                "empty": False,
            },
            "value": {
                "required": True,
                "empty": False,
            },
        }
    )

    response = validator.validate(request)

    if response is False:
        raise MissingRequiredFieldError(json.dumps(validator.errors))
