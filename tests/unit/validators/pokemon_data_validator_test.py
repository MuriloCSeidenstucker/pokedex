from src.common.exceptions import InvalidFieldValueError
from src.common.pokemon_type import PokemonType
from src.validators import pokemon_data_validator


def test_pokemon_data_validator():
    mock_request = {
        "pokemon_id": "1",
        "pkn_name": "Pokemon Spy",
        "type_1": PokemonType.DARK,
        "type_2": "",
        "generation": "1",
        "is_legendary": "1",
    }

    pokemon_data_validator(mock_request)


def test_pokemon_data_validator_error():
    mock_request = {
        "pokemon_id": "foo",
        "pkn_name": "123",
        "type_1": "",
        "type_2": "foo",
        "generation": "foo",
        "is_legendary": "foo",
    }

    try:
        pokemon_data_validator(mock_request)
        assert False, "Expected exception not raised"
    except Exception as e:
        assert isinstance(e, InvalidFieldValueError)
