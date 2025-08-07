"""Módulo de entrada principal da Pokédex via CLI.

Utiliza o Typer para definir comandos de linha de comando. 
O comando principal `run` inicia o fluxo da aplicação 
chamando o gerenciador de processos definido em `process_handle.py`.
"""

import typer

from src.main.process_handle import start

app = typer.Typer()


@app.command()
def run():
    """Inicia a Pokédex por linha de comando.

    Executa o processo principal do sistema,
    chamando a função `start()` responsável por orquestrar o fluxo
    de execução da Pokédex.
    """
    start()
