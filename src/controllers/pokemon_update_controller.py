# pylint: disable=C0121:singleton-comparison

from typing import Dict

from src.common.error_handler import ErrorHandler
from src.common.exceptions import MissingRequiredFieldError
from src.common.pokemon import Pokemon
from src.models.repositories.pokemons_repository import PokemonsRepository
from src.validators import pokemon_query_validator, pokemon_update_validator


class PokemonUpdateController:
    def __init__(self, pokemons_repository: PokemonsRepository) -> None:
        self.__pokemons_repository = pokemons_repository
        self.error_handler = ErrorHandler()

    def update(self, by: str, value: str, pokemon_data: Dict) -> Dict:
        try:
            self.__validate_fields(by, value, pokemon_data)
            pokemon = self.__update_pokemon(by, value, pokemon_data)
            response = self.__format_response(pokemon)
            return {"success": True, "message": response}
        except Exception as e:
            error = self.error_handler.handle_error(e)
            return {"success": False, "error": error}

    @classmethod
    def __validate_fields(cls, by: str, value: str, pokemon_data: Dict) -> None:
        pokemon_query_validator({"by": by, "value": value})
        if not pokemon_data:
            raise MissingRequiredFieldError("'pokemon_data' is a required field")
        pokemon_update_validator(pokemon_data)

    def __update_pokemon(self, by: str, value: str, pokemon_data: Dict) -> Pokemon:
        pokemon_id = (
            int(pokemon_data["pokemon_id"]) if pokemon_data["pokemon_id"] else None
        )
        type_2 = None if pokemon_data["type_2"] == None else pokemon_data["type_2"]
        generation = (
            int(pokemon_data["generation"]) if pokemon_data["generation"] else None
        )
        is_legendary = (
            int(pokemon_data["is_legendary"])
            if pokemon_data["is_legendary"] in ["0", "1"]
            else None
        )

        pokemon = Pokemon(
            pokemon_id=pokemon_id,
            pkn_name=pokemon_data["pkn_name"] or None,
            type_1=pokemon_data["type_1"] or None,
            type_2=type_2,
            generation=generation,
            is_legendary=is_legendary,
        )

        updated_pokemon = self.__pokemons_repository.update_pokemon(by, value, pokemon)

        return updated_pokemon

    def __format_response(self, pokemon: Pokemon) -> Dict:
        return {"count": 1, "type": "Pokemon", "attributes": pokemon}
