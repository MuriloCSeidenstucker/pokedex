from typing import Any

from src.models.entities.pokemons_entity import PokemonsEntity
from src.models.settings.connection import DBConnectionHandler


class PokemonsRepository:
    def insert_pokemon(self, pokemon: Any) -> None:
        with DBConnectionHandler() as db:
            try:
                new_registry = PokemonsEntity(
                    pokemon_id=pokemon["pokemon_id"],
                    pkn_name=pokemon["pkn_name"],
                    type_1=pokemon["type_1"],
                    type_2=pokemon["type_2"],
                    generation=pokemon["generation"],
                    is_legendary=pokemon["is_legendary"],
                )
                db.session.add(new_registry)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e
