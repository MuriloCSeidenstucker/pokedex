from src.controllers.pokemon_find_all_controller import PokemonFindAllController
from src.models.repositories.pokemons_repository import PokemonsRepository
from src.views.pokemon_find_all_view import PokemonFindAllView


def pokemon_find_all_constructor() -> None:
    pokemons_repository = PokemonsRepository()
    pokemon_find_all_view = PokemonFindAllView()
    pokemon_find_all_controller = PokemonFindAllController(pokemons_repository)

    request = pokemon_find_all_view.find_all_pokemon_view()
    response = pokemon_find_all_controller.find_all(request)
    if response["success"]:
        pokemon_find_all_view.find_all_pokemons_success(response["message"])
    else:
        pokemon_find_all_view.find_all_pokemons_fail(response["error"])
