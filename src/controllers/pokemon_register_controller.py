from typing import Dict


class PokemonRegisterController:
    def register(self, new_pokemon_info: Dict) -> Dict:
        try:
            self.__validate_fields(new_pokemon_info)
            response = self.__format_response(new_pokemon_info)
            return {"success": True, "message": response}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def __validate_fields(self, new_pokemon_info: Dict) -> None:
        if (
            not isinstance(new_pokemon_info["name"], str)
            or not new_pokemon_info["name"]
        ):
            raise Exception("Campo nome incorreto!")

        if (
            not isinstance(new_pokemon_info["type"], str)
            or not new_pokemon_info["type"]
        ):
            raise Exception("Campo tipo incorreto!")

    def __format_response(self, new_pokemon_info: Dict) -> Dict:
        return {"count": 1, "type": "Pokemon", "attributes": new_pokemon_info}
