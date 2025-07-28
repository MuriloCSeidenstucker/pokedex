from typing import Dict, List

from sqlalchemy.exc import IntegrityError

from src.common.exceptions import DuplicatePokemonError, PokemonNotFoundError
from src.common.pokemon import Pokemon
from src.models.entities.pokemons_entity import PokemonsEntity
from src.models.settings.connection import DBConnectionHandler

column_map = {
    "id": PokemonsEntity.pokemon_id,
    "name": PokemonsEntity.pkn_name,
    "type_1": PokemonsEntity.type_1,
    "type_2": PokemonsEntity.type_2,
    "generation": PokemonsEntity.generation,
    "is_legendary": PokemonsEntity.is_legendary,
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
            except IntegrityError as e:
                db.session.rollback()
                msg = ""
                if "pokemons.PRIMARY" in str(e.orig.args[1]):
                    pokemon_id = e.params.get("pokemon_id")
                    msg = f"pokemon with id '{pokemon_id}' already exists in repository"
                if "pokemons.pkn_name" in str(e.orig.args[1]):
                    name = e.params.get("pkn_name")
                    msg = f"pokemon with name '{name}' already exists in repository"
                raise DuplicatePokemonError(msg) from e
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

                if not pokemon:
                    raise PokemonNotFoundError(
                        f"'{value}' pokemon not found in repository"
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

    def select_all_pokemons(self, request: Dict) -> List[Pokemon]:
        with DBConnectionHandler() as db:
            try:
                query = db.session.query(PokemonsEntity)

                if request:
                    if request.get("type_1") is not None:
                        query = query.filter_by(type_1=request["type_1"])
                    if request.get("type_2") is not None:
                        query = query.filter_by(type_2=request["type_2"])
                    if request.get("generation") is not None:
                        query = query.filter_by(generation=request["generation"])
                    if request.get("is_legendary") is not None:
                        query = query.filter_by(is_legendary=request["is_legendary"])

                pokemons = query.order_by(PokemonsEntity.pokemon_id).all()

                if not pokemons:
                    raise PokemonNotFoundError("No pokemon found in repository")
                return pokemons
            except Exception as e:
                db.session.rollback()
                raise e

    def update_pokemon(self, by: str, value: str, pokemon: Pokemon) -> Pokemon:
        if by not in column_map:
            raise ValueError(f"Invalid argument: {by}")

        with DBConnectionHandler() as db:
            try:

                pokemon_check = (
                    db.session.query(PokemonsEntity)
                    .filter(column_map[by] == value)
                    .one_or_none()
                )

                if pokemon_check is None:
                    raise PokemonNotFoundError(f"No Pokemon found with {by} = {value}")

                type_2 = (
                    pokemon_check.type_2 if pokemon.type_2 is None else pokemon.type_2
                )
                is_legendary = (
                    pokemon.is_legendary
                    if pokemon.is_legendary in [0, 1]
                    else pokemon_check.is_legendary
                )
                updated_data = {
                    "pokemon_id": pokemon.pokemon_id or pokemon_check.pokemon_id,
                    "pkn_name": pokemon.pkn_name or pokemon_check.pkn_name,
                    "type_1": pokemon.type_1 or pokemon_check.type_1,
                    "type_2": type_2,
                    "generation": pokemon.generation or pokemon_check.generation,
                    "is_legendary": is_legendary,
                }

                (
                    db.session.query(PokemonsEntity)
                    .filter(column_map[by] == value)
                    .update(updated_data)
                )
                db.session.commit()
                return Pokemon(
                    pokemon_id=updated_data["pokemon_id"],
                    pkn_name=updated_data["pkn_name"],
                    type_1=updated_data["type_1"],
                    type_2=updated_data["type_2"],
                    generation=updated_data["generation"],
                    is_legendary=updated_data["is_legendary"],
                )
            except Exception as e:
                db.session.rollback()
                raise e

    def delete_pokemon(self, by: str, value: str) -> Pokemon:
        if by not in column_map:
            raise ValueError(f"Invalid argument: {by}")

        with DBConnectionHandler() as db:
            try:
                pokemon = (
                    db.session.query(PokemonsEntity)
                    .filter(column_map[by] == value)
                    .one_or_none()
                )

                if pokemon is None:
                    raise PokemonNotFoundError(f"No Pokemon found with {by} = {value}")

                pkn_data = Pokemon(
                    pokemon_id=pokemon.pokemon_id,
                    pkn_name=pokemon.pkn_name,
                    type_1=pokemon.type_1,
                    type_2=pokemon.type_2,
                    generation=pokemon.generation,
                    is_legendary=pokemon.is_legendary,
                )

                (
                    db.session.query(PokemonsEntity)
                    .filter(column_map[by] == value)
                    .delete()
                )
                db.session.commit()
                return pkn_data
            except Exception as e:
                db.session.rollback()
                raise e
