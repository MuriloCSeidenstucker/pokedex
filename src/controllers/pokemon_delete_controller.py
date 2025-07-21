from typing import Dict

from src.common.error_handler import ErrorHandler
from src.common.pokemon import Pokemon
from src.models.repositories.pokemons_repository import PokemonsRepository
from src.validators import pokemon_query_validator


class PokemonDeleteController:
    def __init__(self, pokemons_repository: PokemonsRepository):
        self.__pokemons_repository = pokemons_repository
        self.error_handler = ErrorHandler()

    def delete(self, by: str, value: str) -> Dict:
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
        pokemon_query_validator({"by": by, "value": value})

    def __delete_pokemon(self, by: str, value: str) -> Pokemon:
        pokemon = self.__pokemons_repository.delete_pokemon(by, value)
        return pokemon

    @classmethod
    def __format_response(cls, deleted_pokemon: Pokemon) -> Dict:
        return {"count": 1, "type": "Pokemon", "attributes": deleted_pokemon}
