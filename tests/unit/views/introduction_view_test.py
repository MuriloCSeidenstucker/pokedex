# pylint: disable=W0613:unused-argument

from typing import Any
from unittest.mock import MagicMock

from pytest_mock import MockerFixture

from src.views.introduction_view import introduction_page


def fake_print(*objects: Any):
    pass


def fake_input(prompt: str) -> str:
    return "5"


def test_introduction_page(mocker: MockerFixture):
    spy_print = mocker.patch("rich.console.Console.print", side_effect=fake_print)
    spy_input: MagicMock = mocker.patch(
        "rich.console.Console.input", side_effect=fake_input
    )
    m = mocker.patch("builtins.open", mocker.mock_open())

    introduction_page()

    return_values = [fake_input(call.args[0]) for call in spy_input.mock_calls]

    assert spy_print.called
    assert spy_input.called
    assert return_values[0] == "5"
    m.assert_called_once_with(r"src\resources\introduction.md", encoding="utf-8")
