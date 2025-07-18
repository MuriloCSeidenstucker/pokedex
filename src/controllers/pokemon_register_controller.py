from typing import Dict

from src.common.error_handler import ErrorHandler
from src.common.exceptions import InvalidFieldValueError
from src.common.pokemon import Pokemon
from src.models.repositories.pokemons_repository import PokemonsRepository
from src.validators.pokemon_register_validator import pokemon_register_validator


class PokemonRegisterController:
    def __init__(self, pokemon_repository: PokemonsRepository) -> None:
        self.__pokemon_repository = pokemon_repository
        self.error_handler = ErrorHandler()

    def register(self, new_pokemon_info: Dict) -> Dict:
        try:
            self.__validate_fields(new_pokemon_info)
            self.__insert_pokemon(new_pokemon_info)
            response = self.__format_response(new_pokemon_info)
            return {"success": True, "message": response}
        except Exception as e:
            error = self.error_handler.handle_error(e)
            return {"success": False, "error": error}

    def __validate_fields(self, new_pokemon_info: Dict) -> None:
        if not isinstance(new_pokemon_info, Dict):
            raise InvalidFieldValueError(
                f"Invalid argument type: {type(new_pokemon_info)}. Must be a dictionary"
            )

        pokemon_register_validator(new_pokemon_info)

    def __insert_pokemon(self, new_pokemon_info: Dict) -> None:
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
        return {"count": 1, "type": "Pokemon", "attributes": new_pokemon_info}
