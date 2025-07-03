# pylint: disable=W0622:redefined-builtin

from typing import List

import pytest
from sqlalchemy import text

from src.models.repositories.pokemons_repository import PokemonsRepository
from src.models.settings.connection import DBConnectionHandler

db_connection_handler = DBConnectionHandler()
connection = db_connection_handler.get_engine().connect()


@pytest.mark.skip(reason="sensitive test")
def test_insert_pokemon_with_real_mysql():
    request = {
        "pokemon_id": "1",
        "pkn_name": "Bulbasaur",
        "type_1": "Grass",
        "type_2": "Poison",
        "generation": "1",
        "is_legendary": "0",
    }

    repo = PokemonsRepository()
    repo.insert_pokemon(request)

    sql = f"""
        SELECT * FROM pokemons
        WHERE pokemon_id = "{request['pokemon_id']}"
    """
    response = connection.execute(text(sql))
    registry = response.fetchall()[0]

    assert registry.pokemon_id == int(request["pokemon_id"])

    __data_reset(registry)


@pytest.mark.skip(reason="sensitive test")
def test_select_all_pokemons_with_real_mysql():
    repo = PokemonsRepository()
    ids = []
    for id in range(5):
        request = {
            "pokemon_id": str(id),
            "pkn_name": "Bulbasaur",
            "type_1": "Grass",
            "type_2": "Poison",
            "generation": "1",
            "is_legendary": "0",
        }
        repo.insert_pokemon(request)
        ids.append(id)

    response = repo.select_all_pokemons()

    assert isinstance(response, List)
    assert len(response) == len(ids)
    for id in ids:
        assert response[id].pokemon_id == id
        assert response[id].pkn_name == request["pkn_name"]
        assert response[id].type_1 == request["type_1"]
        assert response[id].type_2 == request["type_2"]
        assert response[id].generation == int(request["generation"])
        assert response[id].is_legendary == int(request["is_legendary"])

    __data_reset(ids)


def __data_reset(ids):
    query = text("DELETE FROM pokemons WHERE pokemon_id IN :ids")
    connection.execute(query, {"ids": tuple(ids)})
    connection.commit()
