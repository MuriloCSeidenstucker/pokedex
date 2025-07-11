import pytest
from pytest_mock import MockerFixture

from src.common.by import By
from src.common.pokemon import Pokemon
from src.controllers.pokemon_update_controller import PokemonUpdateController


def test_update(mocker: MockerFixture):
    mock_pokemon = Pokemon(
        pokemon_id=1,
        pkn_name="Bulbasaur",
        type_1="Grass",
        type_2="Poison",
        generation=1,
        is_legendary=0,
    )
    mock_data = {
        "pokemon_id": "1",
        "pkn_name": "Bulbasaur",
        "type_1": "Grass",
        "type_2": "Poison",
        "generation": "1",
        "is_legendary": "0",
    }
    mock_repo = mocker.patch(
        "src.models.repositories.pokemons_repository.PokemonsRepository"
    )
    mock_repo.update_pokemon = mocker.MagicMock()

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
            1,
            "Bulbasaur",
            {},
            f"Argument 'by' must be one of {By.ByType}, got '1'",
        ),
        (
            "name",
            1,
            {},
            "Invalid type for 'value' argument: expected str, got 'int'",
        ),
        (
            "id",
            "1",
            None,
            "Invalid argument type: NoneType. Must be a dictionary",
        ),
        (
            "id",
            "1",
            {"pokemon_id": "abc"},
            "invalid literal for int() with base 10: 'abc'",
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

    assert expected_error == response["error"]
    assert not response["success"]


def test_update_error(mocker: MockerFixture):
    mock_repo = mocker.patch(
        "src.models.repositories.pokemons_repository.PokemonsRepository"
    )
    mock_repo.update_pokemon.return_value = None

    controller = PokemonUpdateController(mock_repo)
    response = controller.update("name", "Bulbasaur", {})

    assert not response["success"]
    assert response["error"] == "'pokemon_id'"
