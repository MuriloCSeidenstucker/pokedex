"""Exibe o menu principal da Pokédex com opções de comandos via CLI.

Este módulo usa a biblioteca `rich` para renderizar uma interface colorida
e organizada para o usuário interagir com o sistema.
"""

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

console = Console()


def introduction_page():
    """Renderiza o menu inicial da Pokédex e solicita a escolha do usuário.

    Exibe as opções disponíveis (cadastrar, buscar, listar, atualizar,
    deletar Pokémon ou sair), numeradas de 1 a 6. O usuário deve escolher
    uma das opções para dar continuidade ao fluxo do sistema.

    Returns:
        str: O comando selecionado pelo usuário (valores esperados: "1" a "6").
    """
    title = Text("📘 Menu da Pokédex", style="bold magenta")

    table = Table.grid(padding=(0, 2))
    table.add_column(justify="center", style="bold yellow", width=5)
    table.add_column(style="white")

    table.add_row("1", "[bold]Cadastrar Pokémon[/bold]")
    table.add_row("2", "[bold]Buscar Pokémon[/bold]")
    table.add_row("3", "[bold]Mostrar Todos os Pokémons[/bold]")
    table.add_row("4", "[bold]Atualizar Pokémon[/bold]")
    table.add_row("5", "[bold red]Deletar Pokémon[/bold red]")
    table.add_row("6", "[bold]Sair do Sistema[/bold]")

    panel = Panel.fit(
        table,
        title=title,
        border_style="magenta",
        padding=(1, 4),
    )

    console.print(panel)

    command = console.input("\n[bold blue]▶️  Opção Selecionada:[/bold blue] ").strip()
    return command
