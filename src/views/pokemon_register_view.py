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
        os.system("cls||clear")

        success_message = f"""
            Pokemon cadastrado com sucesso!

            Tipo: { message["type"] }
            Registros: { message["count"] }
            Infos:
                Nome: { message["attributes"]["name"] }
                Tipo 1: { message["attributes"]["type"] }
        """
        console.print(success_message)

    def registry_pokemon_fail(self, error: str) -> None:
        os.system("cls||clear")

        fail_message = f"""
            Falha ao cadastrar Pokemon!

            Erro: { error }
        """
        console.print(fail_message)
