from src.controllers.pokemon_register_controller import PokemonRegisterController


def test_register() -> None:
    mock_info = {"name": "Pikachu", "type": "Elétrico"}
    pokemon_register_controller = PokemonRegisterController()
    response = pokemon_register_controller.register(mock_info)

    assert response["success"]
    assert response["message"]["count"] == 1
    assert response["message"]["type"] == "Pokemon"
    assert response["message"]["attributes"]["name"] == mock_info["name"]
    assert response["message"]["attributes"]["type"] == mock_info["type"]


def test_register_name_error() -> None:
    mock_info = {"name": "", "type": "Elétrico"}
    pokemon_register_controller = PokemonRegisterController()
    response = pokemon_register_controller.register(mock_info)

    assert not response["success"]
    assert response["error"] == "Campo nome incorreto!"


def test_register_type_error() -> None:
    mock_info = {"name": "Pikachu", "type": 123}
    pokemon_register_controller = PokemonRegisterController()
    response = pokemon_register_controller.register(mock_info)

    assert not response["success"]
    assert response["error"] == "Campo tipo incorreto!"
