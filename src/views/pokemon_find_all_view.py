import os
from typing import Dict

from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.table import Table
from rich.text import Text

from src.common.pokemon_type import TYPE_COLORS

console = Console()


class PokemonFindAllView:
    def find_all_pokemons_success(self, message: Dict) -> None:
        os.system("cls||clear")

        title = Text("📋 Lista de Pokémons Registrados", style="bold green")

        table = Table(
            show_header=True,
            header_style="bold magenta",
            border_style="green",
            box=None,
            title=title,
        )

        table.add_column("N°", style="dim", justify="center", width=8)
        table.add_column("Nome", justify="center")
        table.add_column("Tipo", justify="center")
        table.add_column("Geração", justify="center")
        table.add_column("Lendário", justify="center")

        for pkn in message["attributes"]:
            type_1_color = TYPE_COLORS.get(pkn.type_1.lower(), "white")
            type_2_color = (
                TYPE_COLORS.get(pkn.type_2.lower(), "white") if pkn.type_2 else "grey30"
            )

            type_1_styled = f"[{type_1_color}]{pkn.type_1}[/]"
            type_2_styled = (
                f"[{type_2_color}]{pkn.type_2}[/]" if pkn.type_2 else "[grey30]-[/]"
            )

            types_formatted = f"{type_1_styled}\n{type_2_styled}"

            is_legendary = (
                "[bold green]Sim[/bold green]"
                if pkn.is_legendary == 1
                else "[dim]Não[/dim]"
            )

            table.add_row(
                str(pkn.pokemon_id),
                pkn.pkn_name,
                types_formatted,
                f"{pkn.generation}ª",
                is_legendary,
            )

        panel = Panel.fit(table, border_style="green")
        console.print(panel)

    def find_all_pokemons_fail(self, error: Dict) -> None:
        os.system("cls||clear")

        title_text = Text("⚠️ Nenhum Pokémon Encontrado", style="bold red")

        table = Table(show_header=False, box=None, padding=(0, 1))
        table.add_row("🆔 Código de Status:", str(error.get("status_code", "N/A")))
        table.add_row("📛 Nome:", error.get("name", "N/A"))

        detail = error.get("details", "")
        syntax = Syntax(detail, "python", theme="monokai", word_wrap=True)

        console.print(Panel.fit(title_text, border_style="red"))
        console.print(table)
        console.print(
            Panel(syntax, title="📋 Detalhes Técnicos", border_style="grey50")
        )
