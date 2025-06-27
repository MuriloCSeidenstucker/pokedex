import os
from typing import Dict

from rich.console import Console

console = Console()


class PokemonRegisterView:
    def registry_pokemon_view(self) -> Dict:
        os.system("cls||clear")

        console.print("[bold]Cadastrar novo pokemon[/bold]\n\n")
        name = console.input("Determine o nome do pokemon: ")
        ptype = console.input("Determine o tipo do pokemon: ")

        new_pokemon_info = {"name": name, "type": ptype}

        return new_pokemon_info

    def registry_pokemon_success(self, message: Dict) -> None:

        self.__validate_fields(message)

        os.system("cls||clear")

        success_message = f"""
            Pokemon cadastrado com sucesso!

            Tipo: { message["type"] }
            Registros: { message["count"] }
            Infos:
                Nome: { message["attributes"]["name"] }
                Tipo Primário: { message["attributes"]["type"] }
        """
        console.print(success_message)

    def registry_pokemon_fail(self, error: str) -> None:

        if not isinstance(error, str):
            raise Exception("Expected type: 'str'")

        os.system("cls||clear")

        fail_message = f"""
            Falha ao cadastrar Pokemon!

            Erro: { error }
        """
        console.print(fail_message)

    def __validate_fields(self, field: Dict) -> None:
        if not isinstance(field, Dict):
            raise Exception("Expected type: 'Dict'")

        if "type" not in field:
            raise Exception("Required key missing: 'type'")

        if "count" not in field:
            raise Exception("Required key missing: 'count'")

        if "attributes" not in field:
            raise Exception("Required key missing: 'attributes'")

        if not isinstance(field["attributes"], Dict):
            raise Exception("Expected value type for 'attributes' key: 'Dict'")

        if "name" not in field["attributes"]:
            raise Exception("Required key missing in attributes dict: 'name'")

        if "type" not in field["attributes"]:
            raise Exception("Required key missing in attributes dict: 'type'")
