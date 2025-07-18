import pytest
from pytest_mock import MockerFixture

from src.common.exceptions import PokemonNotFoundError
from src.common.pokemon import Pokemon
from src.controllers.pokemon_find_controller import PokemonFindController


@pytest.mark.parametrize(
    "by,value",
    [
        ("id", "1"),
        ("name", "Bulbasaur"),
    ],
)
def test_find(by: str, value: str, mocker: MockerFixture):
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
    mock_repo.select_pokemon = mocker.MagicMock()
    mock_repo.select_pokemon.return_value = expected

    controller = PokemonFindController(mock_repo)
    response = controller.find(by, value)

    mock_repo.select_pokemon.assert_called_once_with(by, value)
    assert response["success"]
    assert response["message"]["count"] == 1
    assert response["message"]["type"] == "Pokemon"
    assert isinstance(response["message"]["attributes"], Pokemon)
    assert response["message"]["attributes"] == expected


@pytest.mark.parametrize(
    "by,value, expected_error",
    [
        (
            "1",
            "Bulbasaur",
            {
                "name": "invalid field value",
                "status_code": 2,
                "details": "Argument 'by' must be one of ['id', 'name'], got '1'",
            },
        ),
        (
            "",
            "Bulbasaur",
            {
                "name": "missing required field",
                "status_code": 3,
                "details": '{"by": ["empty values not allowed"]}',
            },
        ),
    ],
)
def test_find_validate_fields_error(by, value, expected_error, mocker: MockerFixture):
    mock_repo = mocker.patch(
        "src.models.repositories.pokemons_repository.PokemonsRepository"
    )

    controller = PokemonFindController(mock_repo)
    response = controller.find(by, value)

    assert expected_error == response["error"]
    assert not response["success"]


def test_find_error(mocker: MockerFixture):
    mock_repo = mocker.patch(
        "src.models.repositories.pokemons_repository.PokemonsRepository"
    )
    mock_repo.select_pokemon.side_effect = PokemonNotFoundError

    controller = PokemonFindController(mock_repo)
    response = controller.find("name", "Bulbasaur")

    assert not response["success"]
    assert response["error"] == {
        "name": "pokemon not found",
        "status_code": 4,
        "details": "pokemon not found in repository",
    }
