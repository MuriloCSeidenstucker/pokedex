"""Construtor do fluxo de busca individual de Pokémon.

Este módulo é responsável por coordenar a instância das camadas MVC
necessárias para realizar a busca de um Pokémon específico.
"""

from src.controllers.pokemon_find_controller import PokemonFindController
from src.models.repositories.pokemons_repository import PokemonsRepository
from src.views.pokemon_find_view import PokemonFindView


def pokemon_find_constructor() -> None:
    """Executa o fluxo de busca de um Pokémon específico.

    Instancia:
    - `PokemonsRepository` para acesso ao banco de dados.
    - `PokemonFindController` para aplicar a lógica de busca.
    - `PokemonFindView` para interagir com o usuário.

    O fluxo coleta os critérios de busca via view, solicita os dados
    ao controller e exibe os resultados na interface CLI.
    """
    pokemons_repository = PokemonsRepository()
    pokemon_find_view = PokemonFindView()
    pokemon_find_controller = PokemonFindController(pokemons_repository)

    request = pokemon_find_view.pokemon_find_view()
    response = pokemon_find_controller.find(request["by"], request["value"])

    if response["success"]:
        pokemon_find_view.pokemon_find_success(response["message"])
    else:
        pokemon_find_view.pokemon_find_fail(response["error"])
