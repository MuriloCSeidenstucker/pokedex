"""Estrutura de dados que representa um Pokémon no domínio da aplicação.

Esta classe é usada para transporte de dados entre camadas (ex: controller, view),
sem dependência de ORM. Representa um Pokémon de forma simples e serializável.
"""

from dataclasses import dataclass


@dataclass
class Pokemon:
    """Objeto de transporte de dados (DTO) para um Pokémon.

    Attributes:
        pokemon_id (int): ID único do Pokémon.
        pkn_name (str): Nome do Pokémon.
        type_1 (str): Tipo primário do Pokémon.
        type_2 (str): Tipo secundário do Pokémon.
        generation (int): Geração à qual o Pokémon pertence.
        is_legendary (int): Indica se o Pokémon é lendário (0 ou 1).
    """

    pokemon_id: int
    pkn_name: str
    type_1: str
    type_2: str
    generation: int
    is_legendary: int
