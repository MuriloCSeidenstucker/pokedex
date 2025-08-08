"""Módulo responsável por buscar todos os Pokémons na Pokédex.

Permite aplicar filtros opcionais durante a busca (tipo, geração, status lendário).
"""

from typing import Dict, List

from src.common.error_handler import ErrorHandler
from src.common.pokemon import Pokemon
from src.models.repositories.pokemons_repository import PokemonsRepository


class PokemonFindAllController:
    """Gerencia o processo de listagem de Pokémons com ou sem filtros."""

    def __init__(self, pokemons_repository: PokemonsRepository):
        """
        Inicializa o controller com uma instância do repositório de Pokémons.

        Args:
            pokemons_repository (PokemonsRepository): Repositório para manipulação de dados.
        """
        self.__pokemons_repository = pokemons_repository
        self.error_handler = ErrorHandler()

    def find_all(self, request: Dict) -> Dict:
        """
        Executa o fluxo de busca de múltiplos Pokémons, com base em filtros opcionais.

        Etapas:
        - Verifica se há filtros ativos.
        - Busca os Pokémons no repositório.
        - Formata os dados encontrados.

        Args:
            request (Dict): Filtros opcionais como tipo, geração, ou status lendário.

        Returns:
            Dict: Um dicionário com a chave `success`:
                - `True` e a lista de Pokémons encontrados.
                - `False` e detalhes do erro, se houver.
        """
        try:
            pokemons = self.__fetch_all(request)
            response = self.__format_response(pokemons)
            return {"success": True, "message": response}
        except Exception as e:
            error = self.error_handler.handle_error(e)
            return {"success": False, "error": error}

    def __fetch_all(self, request: Dict) -> List[Pokemon]:
        """
        Busca todos os Pokémons no repositório com base nos filtros informados.

        Se todos os valores forem `None`, busca sem aplicar filtros.

        Args:
            request (Dict): Dicionário contendo os filtros de busca.

        Returns:
            List[Pokemon]: Lista de instâncias de Pokémons encontrados.
        """
        if all(value is None for value in request.values()):
            request = None
        pokemons = self.__pokemons_repository.select_all_pokemons(request)
        return pokemons

    def __format_response(self, pokemons: List[Pokemon]) -> Dict:
        """
        Formata a resposta contendo a lista de Pokémons encontrados.

        Args:
            pokemons (List[Pokemon]): Lista de Pokémons encontrados.

        Returns:
            Dict: Dicionário com a contagem e os dados dos Pokémons.
        """
        return {"count": len(pokemons), "type": "Pokemon", "attributes": pokemons}
