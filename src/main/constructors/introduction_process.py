"""Processo de introdução da Pokédex.

Este módulo é responsável por iniciar a interação com o usuário,
exibindo a página de introdução e coletando o comando inicial.
"""

from src.views.introduction_view import introduction_page


def introduction_process() -> str:
    """Executa o processo de introdução da Pokédex.

    Chama a view responsável por exibir o menu principal
    e retorna o comando selecionado pelo usuário.

    Returns:
        str: Comando selecionado pelo usuário.
    """
    command = introduction_page()
    return command
