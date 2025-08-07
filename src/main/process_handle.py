"""Módulo principal responsável por gerenciar o fluxo da Pokédex CLI.

Este módulo apresenta o menu inicial e direciona as chamadas para as
diferentes funcionalidades de acordo com o comando selecionado pelo usuário.
"""

import os
from enum import Enum
from typing import Optional

from rich.console import Console

from src.main.constructors import (
    pokemon_delete_constructor,
    pokemon_find_all_constructor,
    pokemon_find_constructor,
    pokemon_register_constructor,
    pokemon_update_constructor,
)

from .constructors.introduction_process import introduction_process


class Command(Enum):
    """Enumeração de comandos disponíveis na Pokédex."""

    REGISTER_POKEMON = "1"
    SEARCH_POKEMON = "2"
    LIST_ALL_POKEMON = "3"
    UPDATE_POKEMON = "4"
    DELETE_POKEMON = "5"
    EXIT = "6"


console = Console()


def start() -> None:
    """Inicia o fluxo principal da Pokédex.

    Exibe o menu de comandos e executa os fluxos associados,
    até que o usuário escolha sair.
    """
    while True:
        command = __display_menu_and_get_command()
        if not __execute_command(command):
            break


def __display_menu_and_get_command() -> Optional[str]:
    """Exibe o menu inicial da Pokédex e lê a escolha do usuário.

    Returns:
        Optional[str]: Comando selecionado pelo usuário.
    """
    return introduction_process()


def __execute_command(command: Optional[str]) -> bool:
    """Executa o processo correspondente ao comando informado.

    Mapeia o comando para seu respectivo construtor e o executa.

    Args:
        command (Optional[str]): Comando digitado pelo usuário.

    Returns:
        bool: `True` para continuar no app, `False` para encerrar.
    """
    command_map = {
        Command.REGISTER_POKEMON.value: pokemon_register_constructor,
        Command.SEARCH_POKEMON.value: pokemon_find_constructor,
        Command.LIST_ALL_POKEMON.value: pokemon_find_all_constructor,
        Command.UPDATE_POKEMON.value: pokemon_update_constructor,
        Command.DELETE_POKEMON.value: pokemon_delete_constructor,
        Command.EXIT.value: lambda: False,
    }

    if command in command_map:
        result = command_map[command]()
        return result if isinstance(result, bool) else True

    os.system("cls||clear")
    console.print(f"O comando: {command} não foi encontrado!\n")
    return True
