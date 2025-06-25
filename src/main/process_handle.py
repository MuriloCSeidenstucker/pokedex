import sys

from rich.console import Console

from src.main.constructor.pokemon_register_constructor import (
    pokemon_register_constructor,
)

from .constructor.introduction_process import introduction_process

console = Console()


def start() -> None:
    while True:
        command = introduction_process()

        if command == "1":
            pokemon_register_constructor()
        elif command == "2":
            console.print("Buscar Pokemon!")
        elif command == "3":
            console.print("Mostrar todos Pokemons!")
        elif command == "5":
            sys.exit()
        else:
            console.print(f"O comando: {command} não foi encontrado!")
