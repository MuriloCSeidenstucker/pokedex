"""Modelo ORM do SQLAlchemy que representa a tabela 'pokemons'.

Esta classe é usada para interagir diretamente com o banco de dados.
"""

from sqlalchemy import Column, Integer, String

from src.models.settings.base import Base


class PokemonsEntity(Base):
    """Entidade persistente mapeada para a tabela 'pokemons'.

    Atributos:
        pokemon_id (int): Chave primária (não autoincrementável).
        pkn_name (str): Nome do Pokémon.
        type_1 (str): Tipo primário do Pokémon.
        type_2 (str): Tipo secundário do Pokémon (opcional).
        generation (int): Geração à qual o Pokémon pertence.
        is_legendary (int): Flag indicando se é lendário (0 ou 1).
    """

    __tablename__ = "pokemons"

    pokemon_id = Column(Integer, primary_key=True, autoincrement=False)
    pkn_name = Column(String(255), nullable=False)
    type_1 = Column(String(255), nullable=False)
    type_2 = Column(String(255), nullable=True)
    generation = Column(Integer, nullable=False)
    is_legendary = Column(Integer, nullable=False)

    def __repr__(self):
        return f"Pokemon [id={self.pokemon_id}, name={self.pkn_name}]"
