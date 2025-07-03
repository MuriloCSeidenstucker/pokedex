# pylint: disable=W0613:unused-argument

from typing import Any
from unittest.mock import MagicMock

from pytest import mark

from src.views.pokemon_register_view import PokemonRegisterView

view = PokemonRegisterView()


def fake_io_system(command: str) -> int:
    return -1


def fake_print(*objects: Any):
    pass


def fake_input(prompt: str) -> str:
    return "Pokemon_Spy" if prompt == "Determine o nome do pokemon: " else "PTipo_Spy"


def test_registry_pokemon_view(mocker):

    mocker.patch("os.system", side_effect=fake_io_system)
    mocker.patch("rich.console.Console.print", side_effect=fake_print)
    spy: MagicMock = mocker.patch("rich.console.Console.input", side_effect=fake_input)

    result = view.registry_pokemon_view()

    return_values = [fake_input(call.args[0]) for call in spy.mock_calls]

    assert spy.called
    assert spy.mock_calls == [
        mocker.call("Determine o nome do pokemon: "),
        mocker.call("Determine o tipo do pokemon: "),
    ]
    assert result == {"name": return_values[0], "type": return_values[1]}


def test_registry_pokemon_success(mocker):
    mocker.patch("os.system", side_effect=fake_io_system)
    spy: MagicMock = mocker.patch("rich.console.Console.print", side_effect=fake_print)

    message = {
        "type": "Spy",
        "count": 1,
        "attributes": {"name": "Pokemon_Spy", "type": "PTipo_Spy"},
    }
    view.registry_pokemon_success(message)

    assert spy.called


@mark.parametrize(
    "message,expected",
    [
        ("message", "Expected type: 'Dict'"),
        (
            {
                "error_type": "Spy",
                "count": 1,
                "attributes": {"name": "Pokemon_Spy", "type": "PTipo_Spy"},
            },
            "Required key missing: 'type'",
        ),
        (
            {
                "type": "Spy",
                "error_count": 1,
                "attributes": {"name": "Pokemon_Spy", "type": "PTipo_Spy"},
            },
            "Required key missing: 'count'",
        ),
        (
            {
                "type": "Spy",
                "count": 1,
                "error_attributes": {"name": "Pokemon_Spy", "type": "PTipo_Spy"},
            },
            "Required key missing: 'attributes'",
        ),
        (
            {"type": "Spy", "count": 1, "attributes": "string"},
            "Expected value type for 'attributes' key: 'Dict'",
        ),
        (
            {
                "type": "Spy",
                "count": 1,
                "attributes": {"error_name": "Pokemon_Spy", "type": "PTipo_Spy"},
            },
            "Required key missing in attributes dict: 'name'",
        ),
        (
            {
                "type": "Spy",
                "count": 1,
                "attributes": {"name": "Pokemon_Spy", "error_type": "PTipo_Spy"},
            },
            "Required key missing in attributes dict: 'type'",
        ),
    ],
)
def test_registry_pokemon_success_validate_errors(message, expected):

    try:
        view.registry_pokemon_success(message)
    except Exception as e:
        assert str(e) == expected


def test_registry_pokemon_fail(mocker):
    mocker.patch("os.system", side_effect=fake_io_system)
    spy: MagicMock = mocker.patch("rich.console.Console.print", side_effect=fake_print)

    view.registry_pokemon_fail("test")

    assert spy.called


def test_registry_pokemon_fail_validate_errors():

    try:
        view.registry_pokemon_fail(None)
    except Exception as e:
        assert str(e) == "Expected type: 'str'"
