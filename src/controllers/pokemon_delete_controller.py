"""Módulo responsável pelo fluxo de exclusão de Pokémon da Pokédex.

Valida os dados fornecidos, remove o Pokémon do repositório e retorna
uma resposta estruturada de sucesso ou erro.
"""

from typing import Dict

from src.common.error_handler import ErrorHandler
from src.common.pokemon import Pokemon
from src.models.repositories.pokemons_repository import PokemonsRepository
from src.validators import pokemon_query_validator


class PokemonDeleteController:
    """Gerencia o processo de exclusão de Pokémon."""

    def __init__(self, pokemons_repository: PokemonsRepository):
        """
        Inicializa o controller com um repositório de Pokémon.

        Args:
            pokemons_repository (PokemonsRepository): Instância do repositório.
        """
        self.__pokemons_repository = pokemons_repository
        self.error_handler = ErrorHandler()

    def delete(self, by: str, value: str) -> Dict:
        """
        Executa o fluxo de exclusão de um Pokémon.

        Etapas:
        - Validação do identificador (`by` e `value`).
        - Exclusão do Pokémon no repositório.
        - Formatação da resposta.

        Args:
            by (str): Tipo de identificação (ex: "id" ou "name").
            value (str): Valor da identificação (ex: "25" ou "pikachu").

        Returns:
            Dict: Um dicionário com a chave `success`:
                - `True` e os dados do Pokémon removido em caso de sucesso.
                - `False` e detalhes do erro em caso de falha.
        """
        try:
            self.__validate_fields(by, value)
            deleted_pokemon = self.__delete_pokemon(by, value)
            response = self.__format_response(deleted_pokemon)
            return {"success": True, "message": response}
        except Exception as e:
            error = self.error_handler.handle_error(e)
            return {"success": False, "error": error}

    @classmethod
    def __validate_fields(cls, by: str, value: str) -> None:
        """
        Valida os dados utilizados para identificar o Pokémon a ser excluído.

        Args:
            by (str): Tipo de identificação.
            value (str): Valor da identificação.

        Raises:
            InvalidFieldValueError: Se os campos forem inválidos.
        """
        pokemon_query_validator({"by": by, "value": value})

    def __delete_pokemon(self, by: str, value: str) -> Pokemon:
        """
        Remove o Pokémon do repositório.

        Args:
            by (str): Tipo de identificação.
            value (str): Valor da identificação.
        """
        pokemon = self.__pokemons_repository.delete_pokemon(by, value)
        return pokemon

    @classmethod
    def __format_response(cls, deleted_pokemon: Pokemon) -> Dict:
        """
        Formata a resposta de sucesso da exclusão.

        Args:
            deleted_pokemon (Pokemon): Instância do Pokémon removido.

        Returns:
            Dict: Informações formatadas do Pokémon excluído.
        """
        return {"count": 1, "type": "Pokemon", "attributes": deleted_pokemon}
