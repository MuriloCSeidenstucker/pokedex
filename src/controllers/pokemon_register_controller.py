from typing import Dict


class PokemonRegisterController:
    def register(self, new_pokemon_info: Dict) -> Dict:
        try:
            response = self.__format_response(new_pokemon_info)
            return {"success": True, "message": response}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def __format_response(self, new_pokemon_info: Dict) -> Dict:
        return {"count": 1, "type": "Pokemon", "attributes": new_pokemon_info}
