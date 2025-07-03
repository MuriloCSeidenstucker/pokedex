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


def __data_reset(ids):
    query = text("DELETE FROM pokemons WHERE pokemon_id IN :ids")
    connection.execute(query, {"ids": tuple(ids)})
    connection.commit()
