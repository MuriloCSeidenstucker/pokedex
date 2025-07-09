from enum import Enum
from typing import Optional

from rich.console import Console

from src.main.constructors import (
    pokemon_delete_constructor,
    pokemon_find_all_constructor,
    pokemon_register_constructor,
)

from .constructors.introduction_process import introduction_process


class Command(Enum):
    REGISTER_POKEMON = "1"
    SEARCH_POKEMON = "2"
    LIST_ALL_POKEMON = "3"
    UPDATE_POKEMON = "4"
    DELETE_POKEMON = "5"
    EXIT = "6"


console = Console()


def start() -> None:
    while True:
        command = __display_menu_and_get_command()
        if not __execute_command(command):
            break


def __display_menu_and_get_command() -> Optional[str]:
    return introduction_process()


def __execute_command(command: Optional[str]) -> bool:
    command_map = {
        Command.REGISTER_POKEMON.value: pokemon_register_constructor,
        Command.SEARCH_POKEMON.value: lambda: console.print("Buscar Pokemon"),
        Command.LIST_ALL_POKEMON.value: pokemon_find_all_constructor,
        Command.UPDATE_POKEMON.value: lambda: console.print("Atualizar pokemon"),
        Command.DELETE_POKEMON.value: pokemon_delete_constructor,
        Command.EXIT.value: lambda: False,
    }

    if command in command_map:
        result = command_map[command]()
        return result if isinstance(result, bool) else True

    console.print(f"O comando: {command} não foi encontrado!")
    return True
