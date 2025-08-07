"""Construtor do fluxo de exclusão de Pokémon.

Este módulo coordena a execução da funcionalidade de remoção,
instanciando os componentes MVC necessários.
"""

from src.controllers.pokemon_delete_controller import PokemonDeleteController
from src.models.repositories.pokemons_repository import PokemonsRepository
from src.views.pokemon_delete_view import PokemonDeleteView


def pokemon_delete_constructor() -> None:
    """Executa o fluxo de exclusão de um Pokémon existente.

    Instancia:
    - `PokemonsRepository` para manipulação de dados.
    - `PokemonDeleteController` para aplicar regras de negócio.
    - `PokemonDeleteView` para interações com o usuário via CLI.

    Após coletar o critério de busca com a view, envia a requisição
    ao controller e exibe uma mensagem de sucesso ou erro de acordo
    com a resposta.
    """
    pokemons_repository = PokemonsRepository()
    pokemon_delete_view = PokemonDeleteView()
    pokemon_delete_controller = PokemonDeleteController(pokemons_repository)

    request = pokemon_delete_view.pokemon_delete_view()
    response = pokemon_delete_controller.delete(request["by"], request["value"])

    if response["success"]:
        pokemon_delete_view.delete_pokemon_success(response["message"])
    else:
        pokemon_delete_view.delete_pokemon_fail(response["error"])
