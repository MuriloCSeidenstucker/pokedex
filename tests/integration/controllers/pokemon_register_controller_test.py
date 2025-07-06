import pytest

from src.controllers.pokemon_register_controller import PokemonRegisterController
from src.models.repositories.pokemons_repository import PokemonsRepository


@pytest.mark.skip(reason="sensitive test")
def test_register_controller_repository():
    mock_info = {
        "pokemon_id": "9999",
        "pkn_name": "Pokemon_Spy",
        "type_1": "Grasss",
        "type_2": "Poison",
        "generation": "1",
        "is_legendary": "0",
    }

    repo = PokemonsRepository()
    controller = PokemonRegisterController(repo)
    response = controller.register(mock_info)

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

    repo.delete_pokemon("id", mock_info["pokemon_id"])
