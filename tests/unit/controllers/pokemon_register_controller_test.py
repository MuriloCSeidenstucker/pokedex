from pytest_mock import MockerFixture

from src.controllers.pokemon_register_controller import PokemonRegisterController


def test_register(mocker: MockerFixture) -> None:
    mock_repo = mocker.patch(
        "src.models.repositories.pokemons_repository.PokemonsRepository"
    )
    mock_repo.insert_pokemon = mocker.MagicMock()
    mock_info = {
        "pokemon_id": "1",
        "pkn_name": "Bulbasaur",
        "type_1": "grass",
        "type_2": "poison",
        "generation": "1",
        "is_legendary": "0",
    }

    pokemon_register_controller = PokemonRegisterController(mock_repo)
    response = pokemon_register_controller.register(mock_info)

    mock_repo.insert_pokemon.assert_called_once()
    assert response["success"]
    assert response["message"]["count"] == 1
    assert response["message"]["type"] == "Pokemon"
    assert response["message"]["attributes"]["pokemon_id"] == mock_info["pokemon_id"]
    assert response["message"]["attributes"]["pkn_name"] == mock_info["pkn_name"]
    assert response["message"]["attributes"]["type_1"] == mock_info["type_1"]
    assert response["message"]["attributes"]["type_2"] == mock_info["type_2"]
    assert response["message"]["attributes"]["generation"] == mock_info["generation"]
    assert (
        response["message"]["attributes"]["is_legendary"] == mock_info["is_legendary"]
    )


def test_register_invalid_arg_type(mocker: MockerFixture) -> None:
    mock_repo = mocker.patch(
        "src.controllers.pokemon_register_controller.PokemonsRepository"
    )
    mock_info = "invalid argument"

    pokemon_register_controller = PokemonRegisterController(mock_repo)
    response = pokemon_register_controller.register(mock_info)

    assert not response["success"]
    assert response["error"] == {
        "name": "invalid field value",
        "status_code": 2,
        "details": "Invalid argument type: <class 'str'>. Must be a dictionary",
    }


def test_register_parse_error(mocker: MockerFixture) -> None:
    mock_repo = mocker.patch(
        "src.controllers.pokemon_register_controller.PokemonsRepository"
    )
    mock_info = {
        "pokemon_id": "1",
        "pkn_name": "Bulbasaur",
        "type_1": "Grasss",
        "type_2": "Poison",
        "generation": "Primeira",
        "is_legendary": "0",
    }

    pokemon_register_controller = PokemonRegisterController(mock_repo)
    response = pokemon_register_controller.register(mock_info)

    assert not response["success"]
    assert response["error"]["name"] == "invalid field value"
    assert response["error"]["status_code"] == 2
