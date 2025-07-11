from typing import Dict

from src.common.by import By
from src.common.pokemon import Pokemon
from src.models.repositories.pokemons_repository import PokemonsRepository


class PokemonUpdateController:
    def __init__(self, pokemons_repository: PokemonsRepository) -> None:
        self.__pokemons_repository = pokemons_repository

    def update(self, by: str, value: str, pokemon_data: Dict) -> Dict:
        try:
            self.__validate_fields(by, value, pokemon_data)
            pokemon = self.__update_pokemon(by, value, pokemon_data)
            response = self.__format_response(pokemon)
            return {"success": True, "message": response}
        except Exception as e:
            return {"success": False, "error": str(e)}

    @classmethod
    def __validate_fields(cls, by: str, value: str, pokemon_data: Dict) -> None:
        if by not in By.ByType:
            raise Exception(f"Argument 'by' must be one of {By.ByType}, got '{by}'")

        if not isinstance(value, str):
            raise Exception(
                f"Invalid type for 'value' argument: expected str, got '{type(value).__name__}'"
            )

        if not isinstance(pokemon_data, Dict):
            raise Exception(
                f"Invalid argument type: {type(pokemon_data).__name__}. Must be a dictionary"
            )

        try:
            int(pokemon_data["pokemon_id"])
            int(pokemon_data["generation"])
            int(pokemon_data["is_legendary"])
        except Exception as e:
            raise e

    def __update_pokemon(self, by: str, value: str, pokemon_data: Dict) -> Pokemon:
        pokemon = Pokemon(
            pokemon_id=int(pokemon_data["pokemon_id"]),
            pkn_name=pokemon_data["pkn_name"],
            type_1=pokemon_data["type_1"],
            type_2=pokemon_data["type_2"],
            generation=int(pokemon_data["generation"]),
            is_legendary=int(pokemon_data["is_legendary"]),
        )

        self.__pokemons_repository.update_pokemon(by, value, pokemon)

        return pokemon

    def __format_response(self, pokemon: Pokemon) -> Dict:
        return {"count": 1, "type": "Pokemon", "attributes": pokemon}
