from typing import List

from src.common.pokemon import Pokemon
from src.models.entities.pokemons_entity import PokemonsEntity
from src.models.settings.connection import DBConnectionHandler

column_map = {
    "id": PokemonsEntity.pokemon_id,
    "name": PokemonsEntity.pkn_name,
}


class PokemonsRepository:
    def insert_pokemon(self, pokemon: Pokemon) -> None:
        with DBConnectionHandler() as db:
            try:
                new_registry = PokemonsEntity(
                    pokemon_id=pokemon.pokemon_id,
                    pkn_name=pokemon.pkn_name,
                    type_1=pokemon.type_1,
                    type_2=pokemon.type_2,
                    generation=pokemon.generation,
                    is_legendary=pokemon.is_legendary,
                )
                db.session.add(new_registry)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e

    def select_pokemon(self, by: str, value: str) -> Pokemon:
        if by not in column_map:
            raise ValueError(f"Invalid argument: {by}")

        with DBConnectionHandler() as db:
            try:
                pokemon = (
                    db.session.query(PokemonsEntity)
                    .filter(column_map[by] == value)
                    .first()
                )
                return Pokemon(
                    pokemon_id=pokemon.pokemon_id,
                    pkn_name=pokemon.pkn_name,
                    type_1=pokemon.type_1,
                    type_2=pokemon.type_2,
                    generation=pokemon.generation,
                    is_legendary=pokemon.is_legendary,
                )
            except Exception as e:
                db.session.rollback()
                raise e

    def select_all_pokemons(self) -> List[Pokemon]:
        with DBConnectionHandler() as db:
            try:
                pokemons = db.session.query(PokemonsEntity).all()
                return pokemons
            except Exception as e:
                db.session.rollback()
                raise e

    def delete_pokemon(self, by: str, value: str) -> None:
        if by not in column_map:
            raise ValueError(f"Invalid argument: {by}")

        with DBConnectionHandler() as db:
            try:
                (
                    db.session.query(PokemonsEntity)
                    .filter(column_map[by] == value)
                    .delete()
                )
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e
