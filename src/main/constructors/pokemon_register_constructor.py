"""Construtor do fluxo de registro de Pokémon.

Este módulo instancia as camadas necessárias (repositório, view e controller)
para executar o processo completo de registro de um novo Pokémon.
"""

from src.controllers.pokemon_register_controller import PokemonRegisterController
from src.models.repositories.pokemons_repository import PokemonsRepository
from src.views.pokemon_register_view import PokemonRegisterView


def pokemon_register_constructor():
    """Executa o fluxo de registro de um novo Pokémon.

    Instancia:
    - `PokemonsRepository` para manipulação de dados.
    - `PokemonRegisterController` para aplicar regras de negócio.
    - `PokemonRegisterView` para interações com o usuário via CLI.

    Após coletar os dados com a view, envia os dados ao controller e
    exibe uma mensagem de sucesso ou erro de acordo com a resposta.
    """
    pokemon_repository = PokemonsRepository()
    pokemon_register_view = PokemonRegisterView()
    pokemon_register_controller = PokemonRegisterController(pokemon_repository)

    new_pokemon_info = pokemon_register_view.registry_pokemon_view()
    response = pokemon_register_controller.register(new_pokemon_info)

    if response["success"]:
        pokemon_register_view.registry_pokemon_success(response["message"])
    else:
        pokemon_register_view.registry_pokemon_fail(response["error"])
