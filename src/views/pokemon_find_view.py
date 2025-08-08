"""Interface CLI para o fluxo de busca de um Pokémon individual.

Este módulo exibe prompts para o usuário informar os critérios de busca 
e apresenta os resultados ou mensagens de erro com formatação visual.
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


class PokemonFindView:
    """Classe responsável pela interface visual de busca individual de Pokémon."""

    def pokemon_find_view(self) -> Dict:
        """Coleta os critérios de busca (ID ou nome) fornecidos pelo usuário.

        O usuário pode optar por buscar um Pokémon usando seu ID ou nome.
        A função exibe opções visuais e solicita o valor correspondente.

        Returns:
            Dict: Dicionário com os campos:
                - "by": tipo de busca ("id" ou "name").
                - "value": valor a ser buscado.
        """
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
        """Exibe os dados do Pokémon encontrado.

        Mostra os atributos do Pokémon (ID, nome, tipos, geração, etc.)
        e detalhes da busca realizada, incluindo número de registros
        e tipo de busca utilizada.

        Args:
            message (Dict): Dicionário com os dados do Pokémon e metainformações.
        """
        os.system("cls||clear")

        attrs = message["attributes"]
        is_legendary = "Sim" if attrs.is_legendary == 1 else "Não"

        title = Text("✅ Pokémon Encontrado com Sucesso!", style="bold green")

        table = Table(
            title="📋 Informações do Pokémon",
            title_style="bold cyan",
            box=None,
            padding=(0, 1),
        )
        table.add_row("🔢 Número:", str(attrs.pokemon_id))
        table.add_row("📛 Nome:", attrs.pkn_name)
        table.add_row("🧬 Tipo Primário:", attrs.type_1)
        table.add_row("🧬 Tipo Secundário:", attrs.type_2 if attrs.type_2 else "—")
        table.add_row("🕰️ Geração:", str(attrs.generation))
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
        """Exibe mensagem visual de erro quando a busca falha.

        Mostra código de status, nome do erro e detalhes técnicos.

        Args:
            error (Dict): Dicionário contendo nome, código e detalhes do erro.
        """
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
