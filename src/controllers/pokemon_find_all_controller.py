from typing import Dict, List

from src.common.pokemon import Pokemon
from src.models.repositories.pokemons_repository import PokemonsRepository


class PokemonFindAllController:
    def __init__(self, pokemons_repository: PokemonsRepository):
        self.__pokemons_repository = pokemons_repository

    def find_all(self) -> Dict:
        try:
            pokemons = self.__fetch_all()
            response = self.__format_response(pokemons)
            return {"success": True, "message": response}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def __fetch_all(self) -> List[Pokemon]:
        pokemons = self.__pokemons_repository.select_all_pokemons()

        if not pokemons:
            raise Exception("No pokemon found")

        return pokemons

    def __format_response(self, pokemons: List[Pokemon]) -> Dict:
        return {"count": len(pokemons), "type": "Pokemon", "attributes": pokemons}
