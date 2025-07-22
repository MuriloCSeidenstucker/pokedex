import json
from typing import Any

from cerberus import Validator

from src.common.exceptions import InvalidFieldValueError


class QueryValidator(Validator):
    def _validate_value_type_based_on_by(self, constraint, field, value):
        """Valida o tipo do valor com base na chave auxiliar 'by'.

        Se 'by' for 'id', o valor deve conter apenas dígitos (string numérica).
        Se 'by' for 'name', o valor não deve ser numérico (string textual).

        The rule's arguments are validated against this schema:
        {'type': 'boolean'}
        """
        if not constraint:
            return

        if not isinstance(value, str):
            self._error(
                field, f"The input value must be a string, got {type(value).__name__}"
            )
            return

        by = self.document.get("by")

        if by == "id" and not value.isdigit():
            self._error(field, "Value must be an integer when 'by' is 'id'")

        if by == "name" and value.isdigit():
            self._error(field, "Value must be a string when 'by' is 'name'")


def pokemon_query_validator(request: Any):
    schema = {
        "by": {
            "type": "string",
            "required": True,
            "empty": False,
            "allowed": ["id", "name"],
        },
        "value": {"required": True, "empty": False, "value_type_based_on_by": True},
    }

    v = QueryValidator(schema)

    response = v.validate(request)

    if response is False:
        raise InvalidFieldValueError(json.dumps(v.errors))
