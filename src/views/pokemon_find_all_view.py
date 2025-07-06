import os
from typing import Dict

from rich.align import Align
from rich.console import Console
from rich.table import Table

console = Console()


class PokemonFindAllView:
    def find_all_pokemons_success(self, message: Dict) -> None:
        table = Table(show_header=True, header_style="bold magenta", leading=1)
        table.add_column(
            "N°", style="dim", width=12, justify="center", vertical="middle"
        )
        table.add_column("Nome", justify="center", vertical="middle")
        table.add_column("Tipo", justify="center", vertical="middle")
        table.add_column("Geração", justify="center", vertical="middle")
        table.add_column("Lendário", justify="center", vertical="middle")
        for pkn in message["attributes"]:
            table.add_row(
                Align(str(pkn.pokemon_id), align="center", vertical="middle"),
                Align(pkn.pkn_name, align="center", vertical="middle"),
                Align(f"{pkn.type_1}\n{pkn.type_2}", align="center", vertical="middle"),
                Align(f"{pkn.generation}ª", align="center", vertical="middle"),
                Align(
                    "Sim" if pkn.is_legendary == 1 else "Não",
                    align="center",
                    vertical="middle",
                ),
            )

        console.print(table)

    def find_all_pokemons_fail(self, error: str) -> None:
        os.system("cls||clear")

        fail_message = f"""
            Nenhum pokemon encontrado ou cadastrado!

            Erro: { error }
        """
        console.print(fail_message)
