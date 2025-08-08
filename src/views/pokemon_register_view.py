"""Interface CLI para o fluxo de cadastro de Pokémons.

Este módulo é responsável por interações com o usuário durante o processo
de registro de um novo Pokémon, exibindo prompts e mensagens estilizadas
com a biblioteca `rich`.
"""

import os
from typing import Dict

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.syntax import Syntax
from rich.table import Table
from rich.text import Text

from src.common.pokemon_type import POKEMON_TYPES
from src.views.utils import render_types_panel

console = Console()


class PokemonRegisterView:
    """Classe responsável pela interface visual do cadastro de Pokémons."""

    def registry_pokemon_view(self) -> Dict:
        """Exibe prompts para o usuário informar os dados do novo Pokémon.

        Retorna um dicionário com os dados informados pelo usuário, prontos
        para validação e persistência. Os campos incluem ID, nome, tipos,
        geração e flag de lendário.

        Returns:
            Dict: Dados do Pokémon preenchidos via input do usuário.
        """
        os.system("cls||clear")

        title = Text("🐣 Cadastro de Novo Pokémon", style="bold green")
        console.print(Panel.fit(title, border_style="green"))

        pokemon_id = Prompt.ask("🔢 Informe o ID do Pokémon")
        pkn_name = Prompt.ask("📛 Nome do Pokémon")
        render_types_panel()
        type_1 = Prompt.ask(
            "🧬 Tipo Primário", choices=POKEMON_TYPES, show_choices=False
        )
        type_2 = Prompt.ask(
            "🧬 Tipo Secundário (opcional)",
            choices=POKEMON_TYPES + [""],
            show_choices=False,
        )
        generation = Prompt.ask("🕰️ Geração")

        is_legendary = Prompt.ask(
            "🌟 Este Pokémon é lendário? ([bold cyan]1[/]/Sim | [bold cyan]0[/]/Não)",
            choices=["1", "0"],
        )

        new_pokemon_info = {
            "pokemon_id": pokemon_id.strip(),
            "pkn_name": pkn_name.strip(),
            "type_1": type_1.strip(),
            "type_2": type_2.strip(),
            "generation": generation.strip(),
            "is_legendary": is_legendary.strip(),
        }

        return new_pokemon_info

    def registry_pokemon_success(self, message: Dict) -> None:
        """Exibe mensagem visual de sucesso após o cadastro do Pokémon.

        Apresenta os dados do Pokémon recém-cadastrado e informações
        adicionais como tipo de registro.

        Args:
            message (Dict): Mensagem de sucesso contendo os atributos e metadados.
        """
        attrs = message["attributes"]

        os.system("cls||clear")

        is_legendary = "Sim" if attrs["is_legendary"] == "1" else "Não"

        title = Text("✅ Pokémon Cadastrado com Sucesso!", style="bold green")

        table = Table.grid(padding=(0, 2))
        table.add_column(justify="right", style="cyan", no_wrap=True)
        table.add_column(style="white")

        table.add_row("Número", attrs["pokemon_id"])
        table.add_row("Nome", attrs["pkn_name"])
        table.add_row("Tipo Primário", attrs["type_1"])
        table.add_row("Tipo Secundário", attrs["type_2"] or "-")
        table.add_row("Geração", attrs["generation"])
        table.add_row("Lendário", is_legendary)
        table.add_row("Tipo Registrado", message["type"])
        table.add_row("Total de Registros", str(message["count"]))

        panel = Panel.fit(table, title=title, border_style="green")

        console.print(panel)

    def registry_pokemon_fail(self, error: Dict) -> None:
        """Exibe mensagem de erro estilizada caso o cadastro falhe.

        Mostra código de status, nome do erro e detalhes técnicos.

        Args:
            error (Dict): Dicionário contendo nome, código e detalhes do erro.
        """
        os.system("cls||clear")

        title_text = Text("❌ Falha ao Cadastrar Pokémon!", style="bold red")

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
