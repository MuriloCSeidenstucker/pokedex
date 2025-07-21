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
