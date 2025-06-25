import typer

from src.main.process_handle import start

app = typer.Typer()


@app.command()
def run():
    start()
