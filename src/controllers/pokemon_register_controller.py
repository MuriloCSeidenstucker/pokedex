"""Módulo responsável pelo fluxo de registro de novos Pokémon na Pokédex.

Valida os dados fornecidos, insere o novo Pokémon no repositório e retorna
uma resposta estruturada de sucesso ou erro.
"""

from typing import Dict

from src.common.error_handler import ErrorHandler
from src.common.exceptions import InvalidFieldValueError
from src.common.pokemon import Pokemon
from src.models.repositories.pokemons_repository import PokemonsRepository
from src.validators.pokemon_data_validator import pokemon_data_validator


class PokemonRegisterController:
    """Gerencia o processo de cadastro de novos Pokémon."""

    def __init__(self, pokemon_repository: PokemonsRepository) -> None:
        """
        Inicializa o controller com um repositório de Pokémon.

        Args:
            pokemon_repository (PokemonsRepository): Instância do repositório.
        """
        self.__pokemon_repository = pokemon_repository
        self.error_handler = ErrorHandler()

    def register(self, new_pokemon_info: Dict) -> Dict:
        """
        Executa o fluxo de cadastro de um novo Pokémon.

        Etapas:
        - Validação dos dados recebidos.
        - Inserção no banco de dados.
        - Formatação da resposta.

        Args:
            new_pokemon_info (Dict): Dicionário com os dados do novo Pokémon.

        Returns:
            Dict: Um dicionário com a chave `success`:
                - `True` e os dados do Pokémon em caso de sucesso.
                - `False` e detalhes do erro em caso de falha.
        """
        try:
            self.__validate_fields(new_pokemon_info)
            self.__insert_pokemon(new_pokemon_info)
            response = self.__format_response(new_pokemon_info)
            return {"success": True, "message": response}
        except Exception as e:
            error = self.error_handler.handle_error(e)
            return {"success": False, "error": error}

    def __validate_fields(self, new_pokemon_info: Dict) -> None:
        """
        Valida os dados de entrada do Pokémon.

        Args:
            new_pokemon_info (Dict): Dados informados via CLI.

        Raises:
            InvalidFieldValueError: Se os dados forem inválidos ou ausentes.
        """
        if not isinstance(new_pokemon_info, Dict):
            raise InvalidFieldValueError(
                f"Invalid argument type: {type(new_pokemon_info)}. Must be a dictionary"
            )

        pokemon_data_validator(new_pokemon_info)

    def __insert_pokemon(self, new_pokemon_info: Dict) -> None:
        """
        Insere o novo Pokémon no repositório.

        Args:
            new_pokemon_info (Dict): Dados validados do Pokémon.
        """
        pokemon = Pokemon(
            pokemon_id=int(new_pokemon_info["pokemon_id"]),
            pkn_name=new_pokemon_info["pkn_name"],
            type_1=new_pokemon_info["type_1"],
            type_2=new_pokemon_info["type_2"],
            generation=int(new_pokemon_info["generation"]),
            is_legendary=int(new_pokemon_info["is_legendary"]),
        )

        self.__pokemon_repository.insert_pokemon(pokemon)

    def __format_response(self, new_pokemon_info: Dict) -> Dict:
        """
        Formata a resposta de sucesso do cadastro.

        Args:
            new_pokemon_info (Dict): Dados do Pokémon inserido.

        Returns:
            Dict: Informações formatadas do Pokémon.
        """
        return {"count": 1, "type": "Pokemon", "attributes": new_pokemon_info}
