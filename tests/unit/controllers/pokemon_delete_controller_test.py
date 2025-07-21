import pytest
from pytest_mock import MockerFixture

from src.common.pokemon import Pokemon
from src.controllers.pokemon_delete_controller import PokemonDeleteController


@pytest.mark.parametrize(
    "by,value",
    [
        ("id", "1"),
        ("name", "Bulbasaur"),
    ],
)
def test_delete(by: str, value: str, mocker: MockerFixture):
    expected = Pokemon(
        pokemon_id=1,
        pkn_name="Bulbasaur",
        type_1="Grass",
        type_2="Poison",
        generation=1,
        is_legendary=0,
    )
    mock_repo = mocker.patch(
        "src.models.repositories.pokemons_repository.PokemonsRepository"
    )
    mock_repo.delete_pokemon = mocker.MagicMock()
    mock_repo.delete_pokemon.return_value = expected

    controller = PokemonDeleteController(mock_repo)
    response = controller.delete(by, value)

    mock_repo.delete_pokemon.assert_called_once_with(by, value)
    assert response["success"]
    assert response["message"]["count"] == 1
    assert response["message"]["type"] == "Pokemon"
    assert isinstance(response["message"]["attributes"], Pokemon)
    assert response["message"]["attributes"] == expected


@pytest.mark.parametrize(
    "by,value,expected_error",
    [
        (
            "id",
            "Bulbasaur",
            "{\"value\": [\"Value must be an integer when 'by' is 'id'\"]}",
        ),
        (
            "name",
            "1",
            "{\"value\": [\"Value must be a string when 'by' is 'name'\"]}",
        ),
    ],
)
def test_delete_validate_fields_error(by, value, expected_error, mocker: MockerFixture):
    mock_repo = mocker.patch(
        "src.models.repositories.pokemons_repository.PokemonsRepository"
    )

    controller = PokemonDeleteController(mock_repo)
    response = controller.delete(by, value)

    assert expected_error == response["error"]["details"]
    assert not response["success"]
