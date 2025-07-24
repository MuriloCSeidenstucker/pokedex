from rich.columns import Columns
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

from src.common.pokemon_type import POKEMON_TYPES, TYPE_COLORS, TYPE_ICONS

console = Console()


def render_types_panel():
    console.print("\n[bold magenta]Tipos Disponíveis:[/bold magenta]")
    panels = []
    for type_name in POKEMON_TYPES:
        color = TYPE_COLORS.get(type_name, "white")
        icon = TYPE_ICONS.get(type_name, "")
        text = Text(f"{icon} {type_name}", style=f"bold {color}")
        panels.append(Panel(text, expand=True, border_style=color))
    console.print(Columns(panels, equal=True, expand=True))
