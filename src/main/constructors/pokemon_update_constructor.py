"""Construtor do fluxo de atualização de um Pokémon.

Responsável por instanciar e conectar os componentes necessários 
(modelo, controller e view) para executar o processo de atualização 
de um Pokémon já existente na base de dados.
"""

from src.controllers.pokemon_update_controller import PokemonUpdateController
from src.models.repositories.pokemons_repository import PokemonsRepository
from src.views.pokemon_update_view import PokemonUpdateView


def pokemon_update_constructor() -> None:
    """Executa o fluxo de atualização dos dados de um Pokémon.

    Instancia:
    - `PokemonsRepository` para manipulação de dados.
    - `PokemonUpdateController` para aplicar regras de negócio.
    - `PokemonUpdateView` para interações com o usuário via CLI.

    Após coletar o critério de busca e os dados atualizados com a view,
    envia a requisição ao controller e exibe uma mensagem de sucesso
    ou erro de acordo com a resposta.
    """
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
