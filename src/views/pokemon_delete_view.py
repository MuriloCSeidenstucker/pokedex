import os
from typing import Dict

from rich.console import Console

from src.common.by import By

console = Console()


class PokemonDeleteView:
    def pokemon_delete_view(self) -> Dict:
        os.system("cls||clear")

        console.print("[bold]Remover pokemon da Pokedex[/bold]\n\n")

        by_input: str = console.input("Escolha entre 1(ID) 0(Nome): ")
        by = By.ID if by_input == "1" else By.NAME
        message = (
            "Determine o ID do pokemon: "
            if by_input == "1"
            else "Determine o nome do pokemon: "
        )
        value: str = console.input(message)

        return {"by": by, "value": value}

    def delete_pokemon_success(self, message: Dict) -> None:
        os.system("cls||clear")

        is_legendary = "Sim" if message["attributes"]["is_legendary"] == "1" else "Não"
        success_message = f"""
            Pokemon removido com sucesso!

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

    def delete_pokemon_fail(self, error: str) -> None:
        os.system("cls||clear")

        fail_message = f"""
            Falha ao tentar remover Pokemon!

            Erro: { error }
        """
        console.print(fail_message)
