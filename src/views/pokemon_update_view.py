import os
from typing import Dict

from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.syntax import Syntax
from rich.table import Table
from rich.text import Text

from src.common.by import By
from src.common.pokemon_type import POKEMON_TYPES, TYPE_COLORS, TYPE_ICONS

console = Console()


class PokemonUpdateView:
    def pokemon_update_view(self) -> Dict:
        os.system("cls||clear")

        title = Text("🛠️ Atualizar dados do Pokémon", style="bold yellow")

        options = Table.grid(padding=(0, 2))
        options.add_column(justify="right", style="cyan")
        options.add_column(style="white")
        options.add_row("[bold]1[/bold]", "Atualizar por ID")
        options.add_row("[bold]0[/bold]", "Atualizar por Nome")

        console.print(Panel.fit(options, title=title, border_style="yellow"))

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

        pokemon_id = Prompt.ask("🔢 Informe o ID do Pokémon")
        pkn_name = Prompt.ask("📛 Nome do Pokémon")
        console.print("\n[bold magenta]Tipos Disponíveis:[/bold magenta]")
        console.print(self.__render_types_panel())
        type_1 = Prompt.ask(
            "🧬 Tipo Primário", choices=POKEMON_TYPES, show_choices=False
        )
        type_2 = Prompt.ask(
            "🧬 Tipo Secundário (opcional)", default="", show_default=False
        )
        generation = Prompt.ask("🕰️ Geração")

        is_legendary = Prompt.ask(
            "🌟 Este Pokémon é lendário? ([bold cyan]1[/]/Sim | [bold cyan]0[/]/Não)",
            choices=["1", "0"],
        )

        updated_pokemon_info = {
            "pokemon_id": pokemon_id.strip(),
            "pkn_name": pkn_name.strip(),
            "type_1": type_1.strip(),
            "type_2": type_2.strip(),
            "generation": generation.strip(),
            "is_legendary": is_legendary.strip(),
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

    def __render_types_panel(self):
        panels = []
        for type_name in POKEMON_TYPES:
            color = TYPE_COLORS.get(type_name, "white")
            icon = TYPE_ICONS.get(type_name, "")
            text = Text(f"{icon} {type_name}", style=f"bold {color}")
            panels.append(Panel(text, expand=True, border_style=color))
        return Columns(panels, equal=True, expand=True)
