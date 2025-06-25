from rich.console import Console
from rich.markdown import Markdown


def introduction_page():
    console = Console()
    with open(r"src\resources\introduction.md", encoding="utf-8") as f:
        markdown = Markdown(f.read())
    console.print(markdown)
    command = console.input("\n[bold blue]Opção Selecionada: [/bold blue]")

    return command
