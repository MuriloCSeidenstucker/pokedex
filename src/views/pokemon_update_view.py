import os
from typing import Dict

from rich.console import Console

from src.common.by import By

console = Console()


class PokemonUpdateView:
    def pokemon_update_view(self) -> Dict:
        os.system("cls||clear")

        console.print("[bold]Atualizar dados do pokemon[/bold]\n\n")

        by_input: str = console.input("Escolha entre 1(ID) 0(Nome): ")
        by = By.ID if by_input == "1" else By.NAME
        message = (
            "Determine o ID do pokemon: "
            if by_input == "1"
            else "Determine o nome do pokemon: "
        )
        value: str = console.input(message)

        pokemon_id: str = console.input("Determine o id do pokemon: ")
        pkn_name: str = console.input("Determine o nome do pokemon: ")
        type_1: str = console.input("Determine o tipo primário do pokemon: ")
        type_2: str = console.input("Determine o tipo secundário do pokemon: ")
        generation: str = console.input("Determine a geração do pokemon: ")
        is_legendary: str = console.input("Este pokemon é lendário? 1(Sim) 0(Não): ")

        updated_pokemon_info = {
            "pokemon_id": pokemon_id,
            "pkn_name": pkn_name,
            "type_1": type_1,
            "type_2": type_2,
            "generation": generation,
            "is_legendary": is_legendary,
        }

        return {"by": by, "value": value, "pokemon": updated_pokemon_info}

    def pokemon_update_success(self, message: Dict) -> None:
        os.system("cls||clear")

        console.print("[bold]Pokemon atualizado com sucesso[/bold]\n\n")

        is_legendary = "Sim" if message["attributes"].is_legendary == "1" else "Não"
        success_message = f"""
            Tipo: { message["type"] }
            Registros: { message["count"] }
            Infos:
                Número: { message["attributes"].pokemon_id }
                Nome: { message["attributes"].pkn_name }
                Tipo Primário: { message["attributes"].type_1 }
                Tipo Secundário: { message["attributes"].type_2 }
                Geração: { message["attributes"].generation }
                Lendário: { is_legendary }
        """
        console.print(success_message)

    def pokemon_update_fail(self, error: str) -> None:
        os.system("cls||clear")

        fail_message = f"""
            Falha ao tentar buscar o Pokemon!

            Erro: { error }
        """
        console.print(fail_message)
