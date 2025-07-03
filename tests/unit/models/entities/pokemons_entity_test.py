from src.models.entities.pokemons_entity import PokemonsEntity


def test_create_pokemon_entity():
    request = {
        "pokemon_id": "1",
        "pkn_name": "Bulbasaur",
        "type_1": "Grass",
        "type_2": "Poison",
        "generation": "1",
        "is_legendary": "0",
    }

    pkn_entity = PokemonsEntity(
        pokemon_id=request["pokemon_id"],
        pkn_name=request["pkn_name"],
        type_1=request["type_1"],
        type_2=request["type_2"],
        generation=request["generation"],
        is_legendary=request["is_legendary"],
    )

    assert pkn_entity.pokemon_id == request["pokemon_id"]
    assert pkn_entity.pkn_name == request["pkn_name"]
    assert pkn_entity.type_1 == request["type_1"]
    assert pkn_entity.type_2 == request["type_2"]
    assert pkn_entity.generation == request["generation"]
    assert pkn_entity.is_legendary == request["is_legendary"]

    expected = f"Pokemon [id={request["generation"]}, name={request["pkn_name"]}]"
    result = repr(pkn_entity)
    assert result == expected
