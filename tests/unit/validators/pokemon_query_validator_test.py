import pytest

from src.common.exceptions import InvalidFieldValueError
from src.validators import pokemon_query_validator


@pytest.mark.parametrize("by,value", [("id", "1"), ("name", "spy")])
def test_pokemon_query_validator(by: str, value: str):
    mock_request = {"by": by, "value": value}

    pokemon_query_validator(mock_request)


def test_pokemon_query_validator_error():
    try:
        pokemon_query_validator({"by": 1, "value": 1})
    except Exception as e:
        assert isinstance(e, InvalidFieldValueError)
