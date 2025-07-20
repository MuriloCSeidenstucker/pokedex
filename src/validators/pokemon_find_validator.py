import json
from typing import Any

from cerberus import Validator

from src.common.exceptions import InvalidFieldValueError


class QueryValidator(Validator):
    def _validate_value_type_based_on_by(
        self, constraint: bool, field: str, value: str
    ):
        if not constraint:
            return

        by = self.document.get("by")

        if by == "id" and not value.isdigit():
            self._error(field, "Value must be an integer when 'by' is 'id'")

        if by == "name" and value.isdigit():
            self._error(field, "Value must be a string when 'by' is 'name'")


def pokemon_query_validator(request: Any):
    custom_schema = {
        "by": {
            "type": "string",
            "required": True,
            "empty": False,
            "allowed": ["id", "name"],
        },
        "value": {"required": True, "empty": False, "value_type_based_on_by": True},
    }

    v = QueryValidator(custom_schema)

    response = v.validate(request)

    if response is False:
        raise InvalidFieldValueError(json.dumps(v.errors))
