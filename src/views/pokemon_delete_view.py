"""Interface CLI para remoção de Pokémons da Pokédex.

Este módulo permite ao usuário interagir com o sistema para remover
um Pokémon por ID ou nome, com feedback visual estilizado.
"""

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


class PokemonDeleteView:
    """Classe responsável pela interface visual do processo de exclusão de Pokémon."""

    def pokemon_delete_view(self) -> Dict:
        """Coleta os dados necessários para remover um Pokémon.

        O usuário pode escolher se deseja buscar o Pokémon por `ID` ou `Nome`,
        e deve informar o valor correspondente.

        Returns:
            Dict: Contendo:
                - `by` (str): Tipo de busca ("id" ou "name").
                - `value` (str): Valor a ser utilizado para identificar o Pokémon.
        """
        os.system("cls||clear")

        title = Text("🗑️ Remover Pokémon da Pokédex", style="bold red")

        options = Table.grid(padding=(0, 2))
        options.add_column(justify="right", style="cyan")
        options.add_column(style="white")
        options.add_row("[bold]1[/bold]", "Remover por ID")
        options.add_row("[bold]0[/bold]", "Remover por Nome")

        console.print(Panel.fit(options, title=title, border_style="red"))

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

    def delete_pokemon_success(self, message: Dict) -> None:
        """Exibe uma mensagem de sucesso com os dados do Pokémon removido.

        Args:
            message (Dict): Dicionário contendo os dados do Pokémon removido.
        """
        attrs = message["attributes"]

        os.system("cls||clear")

        is_legendary = "Sim" if attrs.is_legendary == 1 else "Não"

        title = Text("✅ Pokémon Removido com Sucesso", style="bold green")

        details = Table.grid(padding=(0, 2))
        details.add_column(justify="right", style="cyan", no_wrap=True)
        details.add_column(style="white")

        details.add_row("Número", str(attrs.pokemon_id))
        details.add_row("Nome", attrs.pkn_name)
        details.add_row("Tipo Primário", attrs.type_1)
        details.add_row("Tipo Secundário", attrs.type_2 or "-")
        details.add_row("Geração", str(attrs.generation))
        details.add_row("Lendário", is_legendary)

        panel = Panel.fit(details, title=title, border_style="green")
        console.print(panel)

    def delete_pokemon_fail(self, error: Dict) -> None:
        """Exibe uma mensagem de erro estilizada em caso de falha na exclusão.

        Mostra informações como nome do erro, status e detalhes técnicos.

        Args:
            error (Dict): Dicionário contendo os dados do erro ocorrido.
        """
        os.system("cls||clear")

        title_text = Text("❌ Falha ao tentar remover o Pokémon!", style="bold red")

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
