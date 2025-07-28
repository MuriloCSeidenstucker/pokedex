from typing import Dict, List

from src.common.error_handler import ErrorHandler
from src.common.pokemon import Pokemon
from src.models.repositories.pokemons_repository import PokemonsRepository


class PokemonFindAllController:
    def __init__(self, pokemons_repository: PokemonsRepository):
        self.__pokemons_repository = pokemons_repository
        self.error_handler = ErrorHandler()

    def find_all(self, request: Dict) -> Dict:
        try:
            pokemons = self.__fetch_all(request)
            response = self.__format_response(pokemons)
            return {"success": True, "message": response}
        except Exception as e:
            error = self.error_handler.handle_error(e)
            return {"success": False, "error": error}

    def __fetch_all(self, request: Dict) -> List[Pokemon]:
        if all(value is None for value in request.values()):
            request = None
        pokemons = self.__pokemons_repository.select_all_pokemons(request)
        return pokemons

    def __format_response(self, pokemons: List[Pokemon]) -> Dict:
        return {"count": len(pokemons), "type": "Pokemon", "attributes": pokemons}
