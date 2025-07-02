from sqlalchemy import Column, Integer, String

from src.models.settings.base import Base


class PokemonsEntity(Base):
    __tablename__ = "pokemons"

    pokemon_id = Column(Integer, primary_key=True, autoincrement=False)
    pkn_name = Column(String(255), nullable=False)
    type_1 = Column(String(255), nullable=False)
    type_2 = Column(String(255), nullable=True)
    generation = Column(Integer, nullable=False)
    is_legendary = Column(Integer, nullable=False)

    def __repr__(self):
        return f"Pokemon [id={self.pokemon_id}, name={self.pkn_name}]"
