"""Módulo responsável por buscar um Pokémon específico na Pokédex.

Valida os dados de busca e utiliza o repositório para recuperar o Pokémon.
Retorna uma resposta estruturada de sucesso ou erro.
"""

from typing import Dict

from src.common.error_handler import ErrorHandler
from src.common.pokemon import Pokemon
from src.models.repositories.pokemons_repository import PokemonsRepository
from src.validators.pokemon_query_validator import pokemon_query_validator


class PokemonFindController:
    """Gerencia o processo de busca de um Pokémon por ID ou nome."""

    def __init__(self, pokemons_repository: PokemonsRepository) -> None:
        """
        Inicializa o controller com um repositório de Pokémon.

        Args:
            pokemons_repository (PokemonsRepository): Instância do repositório de dados.
        """
        self.__pokemons_repository = pokemons_repository
        self.error_handler = ErrorHandler()

    def find(self, by: str, value: str) -> Dict:
        """
        Executa o fluxo de busca de um Pokémon por ID ou nome.

        Etapas:
        - Validação dos dados de entrada.
        - Busca no banco de dados.
        - Formatação da resposta.

        Args:
            by (str): Tipo de busca ("id" ou "name").
            value (str): Valor a ser buscado.

        Returns:
            Dict: Um dicionário com a chave `success`:
                - `True` e os dados do Pokémon em caso de sucesso.
                - `False` e detalhes do erro em caso de falha.
        """
        try:
            self.__validate_fields(by, value)
            pokemon = self.__fetch(by, value)
            response = self.__format_response(pokemon)
            return {"success": True, "message": response}
        except Exception as e:
            error = self.error_handler.handle_error(e)
            return {"success": False, "error": error}

    @classmethod
    def __validate_fields(cls, by: str, value: str) -> None:
        """
        Valida os parâmetros de busca utilizando um validador customizado.

        Args:
            by (str): Tipo de busca.
            value (str): Valor fornecido.

        Raises:
            InvalidFieldValueError: Se os dados forem inválidos conforme regras do validador.
        """
        pokemon_query_validator({"by": by, "value": value})

    def __fetch(self, by: str, value: str) -> Pokemon:
        """
        Recupera o Pokémon do repositório com base nos critérios de busca.

        Args:
            by (str): Tipo de busca.
            value (str): Valor fornecido.

        Returns:
            Pokemon: Instância do Pokémon encontrado.
        """
        pokemon = self.__pokemons_repository.select_pokemon(by, value)
        return pokemon

    def __format_response(self, pokemon: Pokemon) -> Dict:
        """
        Formata os dados do Pokémon em uma estrutura de resposta padrão.

        Args:
            pokemon (Pokemon): Instância do Pokémon encontrado.

        Returns:
            Dict: Dicionário com informações sobre o Pokémon.
        """
        return {"count": 1, "type": "Pokemon", "attributes": pokemon}
