from src.controllers.pokemon_update_controller import PokemonUpdateController
from src.models.repositories.pokemons_repository import PokemonsRepository
from src.views.pokemon_update_view import PokemonUpdateView


def pokemon_update_constructor() -> None:
    pokemons_repository = PokemonsRepository()
    pokemon_update_view = PokemonUpdateView()
    pokemon_update_controller = PokemonUpdateController(pokemons_repository)

    request = pokemon_update_view.pokemon_update_view()
    response = pokemon_update_controller.update(
        request["by"], request["value"], request["pokemon_data"]
    )

    if response["success"]:
        pokemon_update_view.pokemon_update_success(response["message"])
    else:
        pokemon_update_view.pokemon_update_fail(response["error"])
