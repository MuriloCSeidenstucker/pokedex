from pytest_mock import MockerFixture

from src.common.exceptions import PokemonNotFoundError
from src.common.pokemon import Pokemon
from src.controllers.pokemon_find_all_controller import PokemonFindAllController


def test_find_all(mocker: MockerFixture):
    mock_response = [
        Pokemon(
            pokemon_id=1,
            pkn_name="Bulbasaur",
            type_1="Grass",
            type_2="Poison",
            generation=1,
            is_legendary=0,
        ),
        Pokemon(
            pokemon_id=2,
            pkn_name="Ivysaur",
            type_1="Grass",
            type_2="Poison",
            generation=1,
            is_legendary=0,
        ),
    ]
    mock_repo = mocker.patch(
        "src.models.repositories.pokemons_repository.PokemonsRepository"
    )
    mock_repo.select_all_pokemons.return_value = mock_response

    controller = PokemonFindAllController(mock_repo)
    response = controller.find_all()

    assert response["success"]
    assert response["message"]["count"] == 2
    assert response["message"]["type"] == "Pokemon"
    assert isinstance(response["message"]["attributes"][0], Pokemon)
    assert isinstance(response["message"]["attributes"][1], Pokemon)
    assert response["message"]["attributes"][0] == mock_response[0]
    assert response["message"]["attributes"][1] == mock_response[1]


def test_find_all_error(mocker: MockerFixture):
    expected_error = {
        "name": "pokemon not found",
        "status_code": 4,
        "details": "No pokemon found in repository",
    }
    mock_repo = mocker.patch(
        "src.models.repositories.pokemons_repository.PokemonsRepository"
    )
    mock_repo.select_all_pokemons.side_effect = PokemonNotFoundError(
        "No pokemon found in repository"
    )

    controller = PokemonFindAllController(mock_repo)
    response = controller.find_all()

    assert not response["success"]
    assert response["error"] == expected_error
