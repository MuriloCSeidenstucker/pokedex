import os
from typing import Dict

from rich.console import Console

console = Console()


class PokemonRegisterView:
    def registry_pokemon_view(self) -> Dict:
        os.system("cls||clear")

        console.print("[bold]Cadastrar novo pokemon[/bold]\n\n")

        pokemon_id: str = console.input("Determine o id do pokemon: ")
        pkn_name: str = console.input("Determine o nome do pokemon: ")
        type_1: str = console.input("Determine o tipo primário do pokemon: ")
        type_2: str = console.input("Determine o tipo secundário do pokemon: ")
        generation: str = console.input("Determine a geração do pokemon: ")
        is_legendary: str = console.input("Este pokemon é lendário? 1(Sim) 0(Não): ")

        new_pokemon_info = {
            "pokemon_id": pokemon_id,
            "pkn_name": pkn_name,
            "type_1": type_1,
            "type_2": type_2,
            "generation": generation,
            "is_legendary": is_legendary,
        }

        return new_pokemon_info

    def registry_pokemon_success(self, message: Dict) -> None:

        self.__validate_fields(message)

        os.system("cls||clear")

        is_legendary = "Sim" if message["attributes"]["is_legendary"] == "1" else "Não"
        success_message = f"""
            Pokemon cadastrado com sucesso!

            Tipo: { message["type"] }
            Registros: { message["count"] }
            Infos:
                Número: { message["attributes"]["pokemon_id"] }
                Nome: { message["attributes"]["pkn_name"] }
                Tipo Primário: { message["attributes"]["type_1"] }
                Tipo Secundário: { message["attributes"]["type_2"] }
                Geração: { message["attributes"]["generation"] }
                Lendário: { is_legendary }
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

        if "pokemon_id" not in field["attributes"]:
            raise Exception("Required key missing in attributes dict: 'pokemon_id'")

        if "pkn_name" not in field["attributes"]:
            raise Exception("Required key missing in attributes dict: 'pkn_name'")

        if "type_1" not in field["attributes"]:
            raise Exception("Required key missing in attributes dict: 'type_1'")

        if "type_2" not in field["attributes"]:
            raise Exception("Required key missing in attributes dict: 'type_2'")

        if "generation" not in field["attributes"]:
            raise Exception("Required key missing in attributes dict: 'generation'")

        if "is_legendary" not in field["attributes"]:
            raise Exception("Required key missing in attributes dict: 'is_legendary'")
