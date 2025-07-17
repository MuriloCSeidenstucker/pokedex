import os
from typing import Dict

from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.table import Table
from rich.text import Text

from src.common.by import By

console = Console()


class PokemonFindView:
    def pokemon_find_view(self) -> Dict:
        os.system("cls||clear")

        console.print("[bold]Buscar pokemon na Pokedex[/bold]\n\n")

        by_input: str = console.input("Escolha entre 1(ID) 0(Nome): ")
        by = None
        if by_input == "1":
            by = By.ID
        elif by_input == "0":
            by = By.NAME

        message = (
            "Determine o ID do pokemon: "
            if by_input == "1"
            else "Determine o nome do pokemon: "
        )
        value: str = console.input(message)

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
