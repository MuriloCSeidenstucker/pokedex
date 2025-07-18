import os
from typing import Dict

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.syntax import Syntax
from rich.table import Table
from rich.text import Text

from src.common.by import By

console = Console()


class PokemonFindView:
    def pokemon_find_view(self) -> Dict:
        os.system("cls||clear")

        title = Text("🔎 Buscar Pokémon na Pokédex", style="bold blue")

        options_table = Table.grid(padding=(0, 2))
        options_table.add_column(justify="right", style="cyan", no_wrap=True)
        options_table.add_column(style="white")

        options_table.add_row("[bold]1[/bold]", "Buscar por ID")
        options_table.add_row("[bold]0[/bold]", "Buscar por Nome")

        console.print(Panel.fit(options_table, title=title, border_style="blue"))

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

        return {"by": by, "value": value}

    def pokemon_find_success(self, message: Dict) -> None:
        os.system("cls||clear")

        attr = message["attributes"]
        is_legendary = "Sim" if attr.is_legendary == "1" else "Não"

        title = Text("✅ Pokémon Encontrado com Sucesso!", style="bold green")

        table = Table(
            title="📋 Informações do Pokémon",
            title_style="bold cyan",
            box=None,
            padding=(0, 1),
        )
        table.add_row("🔢 Número:", str(attr.pokemon_id))
        table.add_row("📛 Nome:", attr.pkn_name)
        table.add_row("🧬 Tipo Primário:", attr.type_1)
        table.add_row("🧬 Tipo Secundário:", attr.type_2 if attr.type_2 else "—")
        table.add_row("🕰️ Geração:", str(attr.generation))
        table.add_row("🌟 Lendário:", is_legendary)

        meta_table = Table(show_header=False, box=None, padding=(0, 1))
        meta_table.add_row("📌 Tipo de busca:", message.get("type", "N/A"))
        meta_table.add_row(
            "🔎 Registros encontrados:", str(message.get("count", "N/A"))
        )

        console.print(Panel.fit(title, border_style="green"))
        console.print(meta_table)
        console.print(table)

    def pokemon_find_fail(self, error: Dict) -> None:
        os.system("cls||clear")

        title_text = Text("❌ Falha ao tentar buscar o Pokémon!", style="bold red")

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
