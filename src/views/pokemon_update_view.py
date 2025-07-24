# pylint: disable=C0301:line-too-long, R0914:too-many-locals, R0915:too-many-statements

import os
from typing import Dict

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.syntax import Syntax
from rich.table import Table
from rich.text import Text

from src.common.by import By
from src.common.pokemon_type import POKEMON_TYPES
from src.views.utils import render_types_panel

console = Console()


class PokemonUpdateView:
    def pokemon_update_view(self) -> Dict:
        os.system("cls||clear")

        title = Text("Atualizar dados do Pokémon", style="bold yellow")
        console.print(Panel.fit(title, border_style="bold yellow"))

        options_title = Text("Selecione o Pokémon por:", style="bold yellow")
        options = Table.grid(padding=(0, 2))
        options.add_column(justify="right", style="cyan")
        options.add_column(style="white")
        options.add_row("[bold]1[/bold]", "ID")
        options.add_row("[bold]0[/bold]", "Nome")
        console.print(Panel.fit(options, title=options_title, border_style="yellow"))

        by_input = Prompt.ask(
            "[bold yellow]Selecione uma opção[/bold yellow]",
            choices=["1", "0"],
        )
        by = None
        if by_input == "1":
            by = By.ID
        elif by_input == "0":
            by = By.NAME

        field_label = "ID do Pokémon" if by == By.ID else "Nome do Pokémon"
        value: str = Prompt.ask(
            f"[bold green]Informe o {field_label}[/bold green]"
        ).strip()

        selected_update_options = []
        pokemon_id = None
        pkn_name = None
        type_1 = None
        type_2 = None
        generation = None
        is_legendary = None
        update_options_title = Text(
            "Quais dados deseja atualizar?", style="bold yellow"
        )
        update_options = Table.grid(padding=(0, 2))
        update_options.add_column(justify="right", style="cyan")
        update_options.add_column(style="white")
        update_options.add_row("[bold]0[/bold]", "Atualizar ID")
        update_options.add_row("[bold]1[/bold]", "Atualizar Nome")
        update_options.add_row("[bold]2[/bold]", "Atualizar Tipo Primário")
        update_options.add_row("[bold]3[/bold]", "Atualizar Tipo Secundário")
        update_options.add_row("[bold]4[/bold]", "Atualizar Geração")
        update_options.add_row("[bold]5[/bold]", "Atualizar Status Lendário")
        update_options.add_row("[bold]6[/bold]", "Avançar")
        console.print(
            Panel.fit(update_options, title=update_options_title, border_style="yellow")
        )
        while True:
            if len(selected_update_options) == 6:
                break
            selected_option = Prompt.ask(
                "Escolha",
                choices=["0", "1", "2", "3", "4", "5", "6"],
                show_choices=False,
            )
            if selected_option == "6":
                break
            if selected_option not in selected_update_options:
                match selected_option:
                    case "0":
                        pokemon_id = Prompt.ask("🔢 Informe o ID do Pokémon").strip()
                    case "1":
                        pkn_name = Prompt.ask("📛 Nome do Pokémon").strip()
                    case "2":
                        render_types_panel()
                        type_1 = Prompt.ask(
                            "🧬 Tipo Primário",
                            choices=POKEMON_TYPES,
                            show_choices=False,
                        ).strip()
                    case "3":
                        render_types_panel()
                        type_2 = Prompt.ask(
                            "🧬 Tipo Secundário (opcional)",
                            choices=POKEMON_TYPES + [""],
                            show_choices=False,
                        ).strip()
                    case "4":
                        generation = Prompt.ask("🕰️ Geração").strip()
                    case "5":
                        is_legendary = Prompt.ask(
                            "🌟 Este Pokémon é lendário? ([bold cyan]1[/]/Sim | [bold cyan]0[/]/Não)",
                            choices=["1", "0"],
                        ).strip()
                selected_update_options.append(selected_option)
            else:
                console.print(f"Você já selecionou a opção '{selected_option}'")
                console.print("Selecione outra opção ou precione '6' para avançar")

        updated_pokemon_info = {
            "pokemon_id": pokemon_id,
            "pkn_name": pkn_name,
            "type_1": type_1,
            "type_2": type_2,
            "generation": generation,
            "is_legendary": is_legendary,
        }

        return {"by": by, "value": value, "pokemon_data": updated_pokemon_info}

    def pokemon_update_success(self, message: Dict) -> None:
        attrs = message["attributes"]

        os.system("cls||clear")

        is_legendary = "Sim" if attrs.is_legendary == 1 else "Não"

        title = Text("✅ Pokémon Atualizado com Sucesso", style="bold green")

        table = Table.grid(padding=(0, 2))
        table.add_column(justify="right", style="cyan", no_wrap=True)
        table.add_column(style="white")

        table.add_row("Número", str(attrs.pokemon_id))
        table.add_row("Nome", attrs.pkn_name)
        table.add_row("Tipo Primário", attrs.type_1)
        table.add_row("Tipo Secundário", attrs.type_2 or "-")
        table.add_row("Geração", str(attrs.generation))
        table.add_row("Lendário", is_legendary)
        table.add_row("Tipo Registrado", message["type"])
        table.add_row("Total de Registros", str(message["count"]))

        panel = Panel.fit(table, title=title, border_style="green")
        console.print(panel)

    def pokemon_update_fail(self, error: Dict) -> None:
        os.system("cls||clear")

        title_text = Text("❌ Falha ao tentar atualizar o Pokémon!", style="bold red")

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
