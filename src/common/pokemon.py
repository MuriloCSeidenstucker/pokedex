from dataclasses import dataclass


@dataclass
class Pokemon:
    pokemon_id: int
    pkn_name: str
    type_1: str
    type_2: str
    generation: int
    is_legendary: int
