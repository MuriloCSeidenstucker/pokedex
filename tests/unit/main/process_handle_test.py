# pylint: disable=W0613:unused-argument

from typing import Any
from unittest.mock import MagicMock

from pytest_mock import MockerFixture

from src.main.process_handle import start


def fake_print(*objects: Any):
    pass


def test_start(mocker: MockerFixture):
    spy: MagicMock = mocker.patch(
        "src.main.process_handle.introduction_process",
        side_effect=["1", "2", "3", "", "5"],
    )
    constructor_mock = mocker.patch(
        "src.main.process_handle.pokemon_register_constructor",
        side_effect=None,
    )
    mocker.patch("sys.exit", side_effect=SystemExit)
    print_mock = mocker.patch("rich.console.Console.print", side_effect=fake_print)

    try:
        start()
    except SystemExit:
        ...

    assert spy.call_count == 5
    constructor_mock.assert_called_once()
    print_mock.assert_any_call("Buscar Pokemon!")
    print_mock.assert_any_call("Mostrar todos Pokemons!")
    print_mock.assert_any_call("O comando:  não foi encontrado!")
