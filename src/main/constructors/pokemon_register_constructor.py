from src.controllers.pokemon_register_controller import PokemonRegisterController
from src.models.repositories.pokemons_repository import PokemonsRepository
from src.views.pokemon_register_view import PokemonRegisterView


def pokemon_register_constructor():
    pokemon_repository = PokemonsRepository()
    pokemon_register_view = PokemonRegisterView()
    pokemon_register_controller = PokemonRegisterController(pokemon_repository)

    new_pokemon_info = pokemon_register_view.registry_pokemon_view()
    response = pokemon_register_controller.register(new_pokemon_info)

    if response["success"]:
        pokemon_register_view.registry_pokemon_success(response["message"])
    else:
        pokemon_register_view.registry_pokemon_fail(response["error"])
