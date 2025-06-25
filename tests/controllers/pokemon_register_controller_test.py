from src.controllers.pokemon_register_controller import PokemonRegisterController


def test_register() -> None:
    mock_info = {"name": "Pikachu", "type": "Elétrico"}
    pokemon_register_controller = PokemonRegisterController()
    response = pokemon_register_controller.register(mock_info)

    print(response)
