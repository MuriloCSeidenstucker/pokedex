"""Módulo responsável por tratar exceções lançadas durante a execução da Pokédex.

Converte exceções conhecidas e desconhecidas em dicionários padronizados,
facilitando a exibição de mensagens ao usuário.
"""

from typing import Dict

from src.common.exceptions import PokedexBaseError


class ErrorHandler:
    """Classe que encapsula a lógica de tratamento de erros da Pokédex."""

    def handle_error(self, error: Exception) -> Dict:
        """Processa uma exceção e retorna um dicionário com os detalhes.

        Se a exceção for uma instância de `PokedexBaseError`, retorna seus
        atributos (`name`, `status_code`, `msg`). Caso contrário, retorna
        uma resposta genérica para erro desconhecido.

        Args:
            error (Exception): Exceção capturada durante a execução.

        Returns:
            Dict: Dicionário contendo `name`, `status_code` e `details`.
        """
        if not isinstance(error, PokedexBaseError):
            return {
                "name": "unknown error",
                "status_code": 1,
                "details": f"an unknown error was raised:\n{str(error)}",
            }

        return {
            "name": error.name,
            "status_code": error.status_code,
            "details": error.msg,
        }
