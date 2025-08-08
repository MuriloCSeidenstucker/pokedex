"""Funções utilitárias para exibição de informações na interface CLI da Pokédex.

Este módulo fornece utilitários para renderizar elementos visuais personalizados,
como os tipos de Pokémon disponíveis, com cores e ícones.
"""

from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from src.common.pokemon_type import POKEMON_TYPES, TYPE_COLORS, TYPE_ICONS

console = Console()


def render_types_panel():
    """Renderiza os tipos de Pokémon disponíveis no terminal.

    Exibe todos os tipos definidos no projeto, cada um com:
    - Uma cor personalizada (`TYPE_COLORS`),
    - Um ícone visual (`TYPE_ICONS`).

    O conteúdo é exibido em colunas para facilitar a leitura pelo usuário.
    Essa função é usada durante o registro e atualização de Pokémon para guiar a escolha do tipo.
    """
    console.print("\n[bold magenta]Tipos Disponíveis:[/bold magenta]")
    panels = []
    for type_name in POKEMON_TYPES:
        color = TYPE_COLORS.get(type_name, "white")
        icon = TYPE_ICONS.get(type_name, "")
        text = Text(f"{icon} {type_name}", style=f"bold {color}")
        panels.append(Panel(text, expand=True, border_style=color))
    console.print(Columns(panels, equal=True, expand=True))
