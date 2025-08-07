"""Define os critérios válidos para buscas de Pokémon.

Esta classe é usada para padronizar o uso de campos como 'id' e 'name'
em operações de consulta ou validação.
"""

# pylint: disable=C0103:invalid-name

from dataclasses import dataclass


@dataclass
class By:
    """Representa os tipos de busca disponíveis (por ID ou nome).

    Atributos:
        ID (str): Critério 'id'.
        NAME (str): Critério 'name'.
        ByType (list[str]): Lista contendo todos os critérios válidos.
    """

    ID: str = "id"
    NAME: str = "name"

    ByType = ["id", "name"]

    def __contains__(self, value):
        """Verifica se um valor está entre os critérios de busca válidos.

        Args:
            value (str): Valor a ser verificado.

        Returns:
            bool: True se o valor for 'id' ou 'name'; False caso contrário.
        """
        return value in self.ByType
