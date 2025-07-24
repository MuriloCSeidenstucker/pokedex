# pylint: disable=C0301:line-too-long

import pytest
from pytest_mock import MockerFixture

from src.common.pokemon import Pokemon
from src.controllers.pokemon_update_controller import PokemonUpdateController


def test_update(mocker: MockerFixture):
    mock_pokemon = Pokemon(
        pokemon_id=1,
        pkn_name="Bulbasaur",
        type_1="grass",
        type_2="poison",
        generation=1,
        is_legendary=0,
    )
    mock_data = {
        "pokemon_id": "1",
        "pkn_name": "Bulbasaur",
        "type_1": "grass",
        "type_2": "poison",
        "generation": "1",
        "is_legendary": "0",
    }
    mock_repo = mocker.patch(
        "src.models.repositories.pokemons_repository.PokemonsRepository"
    )
    mock_repo.update_pokemon = mocker.MagicMock()
    mock_repo.update_pokemon.return_value = mock_pokemon

    controller = PokemonUpdateController(mock_repo)
    response = controller.update("id", "1", mock_data)

    mock_repo.update_pokemon.assert_called_once_with("id", "1", mock_pokemon)
    assert response["success"]
    assert response["message"]["count"] == 1
    assert response["message"]["type"] == "Pokemon"
    assert isinstance(response["message"]["attributes"], Pokemon)
    assert response["message"]["attributes"].pkn_name == mock_data["pkn_name"]


@pytest.mark.parametrize(
    "by,value,pokemon_data,expected_error",
    [
        (
            "id",
            "Bulbasaur",
            {},
            "{\"value\": [\"Value must be an integer when 'by' is 'id'\"]}",
        ),
        (
            "name",
            "1",
            {},
            "{\"value\": [\"Value must be a string when 'by' is 'name'\"]}",
        ),
        (
            "id",
            "1",
            {},
            "'pokemon_data' is a required field",
        ),
        (
            "id",
            "1",
            {"pokemon_id": "abc"},
            '{"pokemon_id": ["field \'pokemon_id\' cannot be coerced: invalid literal for int() with base 10: \'abc\'", "must be of integer type"]}',
        ),
    ],
)
def test_update_validate_fields_error(
    by, value, pokemon_data, expected_error, mocker: MockerFixture
):
    mock_repo = mocker.patch(
        "src.models.repositories.pokemons_repository.PokemonsRepository"
    )

    controller = PokemonUpdateController(mock_repo)
    response = controller.update(by, value, pokemon_data)

    assert expected_error == response["error"]["details"]
    assert not response["success"]
