from typing import Dict

from src.common.error_handler import ErrorHandler
from src.common.pokemon import Pokemon
from src.models.repositories.pokemons_repository import PokemonsRepository
from src.validators.pokemon_query_validator import pokemon_query_validator


class PokemonFindController:
    def __init__(self, pokemons_repository: PokemonsRepository) -> None:
        self.__pokemons_repository = pokemons_repository
        self.error_handler = ErrorHandler()

    def find(self, by: str, value: str) -> Dict:
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
        pokemon_query_validator({"by": by, "value": value})

    def __fetch(self, by: str, value: str) -> Pokemon:
        pokemon = self.__pokemons_repository.select_pokemon(by, value)
        return pokemon

    def __format_response(self, pokemon: Pokemon) -> Dict:
        return {"count": 1, "type": "Pokemon", "attributes": pokemon}
