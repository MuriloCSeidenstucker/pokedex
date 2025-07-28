# pylint: disable=C0301:line-too-long

import os
from typing import Dict

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.syntax import Syntax
from rich.table import Table
from rich.text import Text

from src.common.pokemon_type import POKEMON_TYPES, TYPE_COLORS
from src.views.utils import render_types_panel

console = Console()


class PokemonFindAllView:
    def find_all_pokemon_view(self) -> Dict:
        os.system("cls||clear")

        title = Text("Buscar por Pokémons", style="bold yellow")
        console.print(Panel.fit(title, border_style="bold yellow"))

        selected_update_options = []
        type_1 = None
        type_2 = None
        generation = None
        is_legendary = None
        update_options_title = Text(
            "Deseja buscar por algo específico?", style="bold yellow"
        )
        update_options = Table.grid(padding=(0, 2))
        update_options.add_column(justify="right", style="cyan")
        update_options.add_column(style="white")
        update_options.add_row("[bold]0[/bold]", "Tipo Primário")
        update_options.add_row("[bold]1[/bold]", "Tipo Secundário")
        update_options.add_row("[bold]2[/bold]", "Geração")
        update_options.add_row("[bold]3[/bold]", "Status Lendário")
        update_options.add_row("[bold]4[/bold]", "Avançar")
        console.print(
            Panel.fit(update_options, title=update_options_title, border_style="yellow")
        )
        while True:
            if len(selected_update_options) == 4:
                break
            selected_option = Prompt.ask(
                "Escolha",
                choices=["0", "1", "2", "3", "4"],
                show_choices=False,
            )
            if selected_option == "4":
                break
            if selected_option not in selected_update_options:
                match selected_option:
                    case "0":
                        render_types_panel()
                        type_1 = Prompt.ask(
                            "🧬 Tipo Primário",
                            choices=POKEMON_TYPES,
                            show_choices=False,
                        ).strip()
                    case "1":
                        render_types_panel()
                        type_2 = Prompt.ask(
                            "🧬 Tipo Secundário (opcional)",
                            choices=POKEMON_TYPES + [""],
                            show_choices=False,
                        ).strip()
                    case "2":
                        generation = Prompt.ask("🕰️ Geração").strip()
                    case "3":
                        is_legendary = Prompt.ask(
                            "🌟 Este Pokémon é lendário? ([bold cyan]1[/]/Sim | [bold cyan]0[/]/Não)",
                            choices=["1", "0"],
                        ).strip()
                selected_update_options.append(selected_option)
            else:
                console.print(f"Você já selecionou a opção '{selected_option}'")
                console.print("Selecione outra opção ou precione '4' para avançar")

        request_filter = {
            "type_1": type_1,
            "type_2": type_2,
            "generation": generation,
            "is_legendary": is_legendary,
        }

        return request_filter

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
