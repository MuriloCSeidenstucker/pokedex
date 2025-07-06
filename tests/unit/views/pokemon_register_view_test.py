# pylint: disable=W0613:unused-argument

from typing import Any
from unittest.mock import MagicMock

from pytest_mock import MockerFixture

from src.views.pokemon_register_view import PokemonRegisterView

view = PokemonRegisterView()


def fake_io_system(command: str) -> int:
    return -1


def fake_print(*objects: Any):
    pass


def fake_input(prompt: str) -> str:
    return_value = ""
    if prompt == "Determine o id do pokemon: ":
        return_value = "9999"
    elif prompt == "Determine o nome do pokemon: ":
        return_value = "Pokemon_Spy"
    elif prompt == "Determine o tipo primário do pokemon: ":
        return_value = "Pkn_Type_1"
    elif prompt == "Determine o tipo secundário do pokemon: ":
        return_value = "Pkn_Type_2"
    elif prompt == "Determine a geração do pokemon: ":
        return_value = "1"
    elif prompt == "Este pokemon é lendário? 1(Sim) 0(Não): ":
        return_value = "0"

    return return_value


def test_registry_pokemon_view(mocker: MockerFixture):
    mocker.patch("os.system", side_effect=fake_io_system)
    mocker.patch("rich.console.Console.print", side_effect=fake_print)
    spy: MagicMock = mocker.patch("rich.console.Console.input", side_effect=fake_input)

    result = view.registry_pokemon_view()

    return_values = [fake_input(call.args[0]) for call in spy.mock_calls]

    assert spy.called
    assert spy.mock_calls == [
        mocker.call("Determine o id do pokemon: "),
        mocker.call("Determine o nome do pokemon: "),
        mocker.call("Determine o tipo primário do pokemon: "),
        mocker.call("Determine o tipo secundário do pokemon: "),
        mocker.call("Determine a geração do pokemon: "),
        mocker.call("Este pokemon é lendário? 1(Sim) 0(Não): "),
    ]
    expected = {
        "pokemon_id": return_values[0],
        "pkn_name": return_values[1],
        "type_1": return_values[2],
        "type_2": return_values[3],
        "generation": return_values[4],
        "is_legendary": return_values[5],
    }
    assert result == expected


def test_registry_pokemon_success(mocker):
    mocker.patch("os.system", side_effect=fake_io_system)
    spy: MagicMock = mocker.patch("rich.console.Console.print", side_effect=fake_print)

    message = {
        "type": "Spy",
        "count": 1,
        "attributes": {
            "pokemon_id": "1",
            "pkn_name": "Pokemon_Spy",
            "type_1": "Pkn_Type_1",
            "type_2": "Pkn_Type_2",
            "generation": "1",
            "is_legendary": "0",
        },
    }
    view.registry_pokemon_success(message)

    assert spy.called


def test_registry_pokemon_fail(mocker):
    mocker.patch("os.system", side_effect=fake_io_system)
    spy: MagicMock = mocker.patch("rich.console.Console.print", side_effect=fake_print)

    view.registry_pokemon_fail("test")

    assert spy.called
