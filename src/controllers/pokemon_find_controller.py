from typing import Dict

from src.common.by import By
from src.common.pokemon import Pokemon
from src.models.repositories.pokemons_repository import PokemonsRepository


class PokemonFindController:
    def __init__(self, pokemons_repository: PokemonsRepository) -> None:
        self.__pokemons_repository = pokemons_repository

    def find(self, by: str, value: str) -> Dict:
        try:
            self.__validate_fields(by, value)
            pokemon = self.__fetch(by, value)
            response = self.__format_response(pokemon)
            return {"success": True, "message": response}
        except Exception as e:
            return {"success": False, "error": str(e)}

    @classmethod
    def __validate_fields(cls, by: str, value: str) -> None:
        if by not in By.ByType:
            raise Exception(f"Argument 'by' must be one of {By.ByType}, got '{by}'")

        if not isinstance(value, str):
            raise Exception(
                f"Invalid type for 'value' argument: expected str, got '{type(value).__name__}'"
            )

    def __fetch(self, by: str, value: str) -> Pokemon:
        pokemon = self.__pokemons_repository.select_pokemon(by, value)

        if not pokemon:
            raise Exception("No pokemon found")

        return pokemon

    def __format_response(self, pokemon: Pokemon) -> Dict:
        return {"count": "1", "type": "Pokemon", "attributes": pokemon}
