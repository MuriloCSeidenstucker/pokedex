"""Define os tipos de Pokémon aceitos e suas representações visuais.

Contém listas, ícones e cores para uso nas validações, exibição no terminal
e padronização de entradas no sistema.
"""

from dataclasses import dataclass

TYPE_COLORS = {
    "normal": "white",
    "fire": "red",
    "water": "blue",
    "grass": "green",
    "electric": "yellow",
    "ice": "cyan",
    "fighting": "dark_red",
    "poison": "magenta",
    "ground": "tan",
    "flying": "light_sky_blue1",
    "psychic": "medium_purple",
    "bug": "chartreuse3",
    "rock": "orange3",
    "ghost": "purple",
    "dark": "grey37",
    "dragon": "blue_violet",
    "steel": "grey66",
    "fairy": "pink1",
}

TYPE_ICONS = {
    "normal": "🔘",
    "fire": "🔥",
    "water": "💧",
    "grass": "🌿",
    "electric": "⚡",
    "ice": "❄️",
    "fighting": "🥊",
    "poison": "☠️",
    "ground": "🌍",
    "flying": "🕊️",
    "psychic": "🔮",
    "bug": "🐛",
    "rock": "🗿",
    "ghost": "👻",
    "dark": "🌑",
    "dragon": "🐉",
    "steel": "🔩",
    "fairy": "🧚",
}

POKEMON_TYPES = [
    "normal",
    "fire",
    "water",
    "grass",
    "electric",
    "ice",
    "fighting",
    "poison",
    "ground",
    "flying",
    "psychic",
    "bug",
    "rock",
    "ghost",
    "dark",
    "dragon",
    "steel",
    "fairy",
]


@dataclass
class PokemonType:
    """Enumeração dos tipos de Pokémon disponíveis.

    Esta classe fornece constantes reutilizáveis que representam os tipos
    reconhecidos pelo sistema. É útil para evitar o uso de strings soltas
    ao longo do código.
    """

    NORMAL = "normal"
    FIRE = "fire"
    WATER = "water"
    GRASS = "grass"
    ELETRIC = "electric"
    ICE = "ice"
    FIGHTING = "fighting"
    POISON = "poison"
    GROUND = "ground"
    FLYING = "flying"
    PSYCHIC = "psychic"
    BUG = "bug"
    ROCK = "rock"
    GHOST = "ghost"
    DARK = "dark"
    DRAGON = "dragon"
    STEEL = "steel"
    FAIRY = "fairy"
