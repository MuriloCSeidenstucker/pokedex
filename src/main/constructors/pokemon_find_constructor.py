from src.controllers.pokemon_find_controller import PokemonFindController
from src.models.repositories.pokemons_repository import PokemonsRepository
from src.views.pokemon_find_view import PokemonFindView


def pokemon_find_constructor() -> None:
    pokemons_repository = PokemonsRepository()
    pokemon_find_view = PokemonFindView()
    pokemon_find_controller = PokemonFindController(pokemons_repository)

    request = pokemon_find_view.pokemon_find_view()
    response = pokemon_find_controller.find(request["by"], request["value"])

    if response["success"]:
        pokemon_find_view.pokemon_find_success(response["message"])
    else:
        pokemon_find_view.pokemon_find_fail(response["error"])
