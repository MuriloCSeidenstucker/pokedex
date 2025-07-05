# pylint: disable=W0622:redefined-builtin

from typing import List

import pytest
from sqlalchemy import text

from src.common.by import By
from src.common.pokemon import Pokemon
from src.models.repositories.pokemons_repository import PokemonsRepository
from src.models.settings.connection import DBConnectionHandler

db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get_engine().connect()


@pytest.mark.skip(reason="sensitive test")
def test_insert_pokemon_with_real_mysql():
    pokemon = Pokemon(
        pokemon_id=9999,
        pkn_name="Pokemon_Spy_1",
        type_1="Grass",
        type_2="Poison",
        generation=1,
        is_legendary=0,
    )

    repo = PokemonsRepository()
    repo.insert_pokemon(pokemon)

    sql = f"""
        SELECT * FROM pokemons
        WHERE pokemon_id = "{pokemon.pokemon_id}"
    """
    response = connection.execute(text(sql))
    registry = response.fetchall()[0]

    assert registry.pokemon_id == int(pokemon.pokemon_id)

    __data_reset(registry)


@pytest.mark.skip(reason="sensitive test")
def test_select_pokemon_with_real_mysql():
    repo = PokemonsRepository()
    mock_pokemon_1 = Pokemon(
        pokemon_id=9998,
        pkn_name="Pokemon_Spy_1",
        type_1="Grass",
        type_2="Poison",
        generation=1,
        is_legendary=0,
    )
    mock_pokemon_2 = Pokemon(
        pokemon_id=9999,
        pkn_name="Pokemon_Spy_2",
        type_1="Grass",
        type_2="Poison",
        generation=1,
        is_legendary=0,
    )
    repo.insert_pokemon(mock_pokemon_1)
    repo.insert_pokemon(mock_pokemon_2)

    pkn_id_1 = repo.select_pokemon("id", "9998")
    pkn_name_1 = repo.select_pokemon("name", "Pokemon_Spy_1")
    pkn_id_2 = repo.select_pokemon(By.ID, "9999")
    pkn_name_2 = repo.select_pokemon(By.NAME, "Pokemon_Spy_2")

    assert isinstance(pkn_id_1, Pokemon)
    assert isinstance(pkn_name_1, Pokemon)
    assert isinstance(pkn_id_2, Pokemon)
    assert isinstance(pkn_name_2, Pokemon)
    assert pkn_id_1.pokemon_id == pkn_name_1.pokemon_id
    assert pkn_id_2.pokemon_id == pkn_name_2.pokemon_id
    assert pkn_id_1.pkn_name == pkn_name_1.pkn_name
    assert pkn_id_2.pkn_name == pkn_name_2.pkn_name

    delete_ids = [mock_pokemon_1.pokemon_id, mock_pokemon_2.pokemon_id]
    __data_reset(delete_ids)


@pytest.mark.skip(reason="sensitive test")
def test_select_all_pokemons_with_real_mysql():
    repo = PokemonsRepository()
    ids = []
    for id in range(5):
        pokemon = Pokemon(
            pokemon_id=id + 9000,
            pkn_name=f"Pokemon_Spy_{id}",
            type_1="Grass",
            type_2="Poison",
            generation=1,
            is_legendary=0,
        )
        repo.insert_pokemon(pokemon)
        ids.append(id + 9000)

    response = repo.select_all_pokemons()

    assert isinstance(response, List)
    assert len(response) == len(ids)
    for id in ids:
        assert response[id - 9000].pokemon_id == id
        assert response[id - 9000].pkn_name == f"Pokemon_Spy_{id - 9000}"
        assert response[id - 9000].type_1 == pokemon.type_1
        assert response[id - 9000].type_2 == pokemon.type_2
        assert response[id - 9000].generation == int(pokemon.generation)
        assert response[id - 9000].is_legendary == int(pokemon.is_legendary)

    __data_reset(ids)


@pytest.mark.skip(reason="sensitive test")
def test_delete_pokemon():
    mock_pokemon = Pokemon(
        pokemon_id=9999,
        pkn_name="Pokemon_Spy",
        type_1="Grass",
        type_2="Poison",
        generation=1,
        is_legendary=0,
    )
    repo = PokemonsRepository()
    repo.insert_pokemon(mock_pokemon)
    repo.delete_pokemon(By.ID, mock_pokemon.pokemon_id)

    try:
        repo.select_pokemon(By.ID, mock_pokemon.pokemon_id)
        assert False, "Expected exception no raised"
    except Exception as e:
        assert str(e) == "'NoneType' object has no attribute 'pokemon_id'"


def __data_reset(ids):
    query = text("DELETE FROM pokemons WHERE pokemon_id IN :ids")
    connection.execute(query, {"ids": tuple(ids)})
    connection.commit()
