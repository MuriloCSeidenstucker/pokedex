import pytest
from pytest_mock import MockerFixture

from src.main.process_handle import __display_menu_and_get_command, __execute_command


def test_display_menu_and_get_command(mocker: MockerFixture):
    mock_process = mocker.patch("src.main.process_handle.introduction_process")

    __display_menu_and_get_command()

    mock_process.assert_called_once()


@pytest.mark.parametrize(
    "command,expected_mock_idx,not_expected_mock_idx",
    [
        ("1", 0, [1, 2]),
        ("2", 2, [0, 1]),
        ("3", 1, [0, 2]),
        ("4", 2, [0, 1]),
        ("5", 2, [0, 1]),
        ("A", 2, [0, 1]),
    ],
)
def test_execute_command(
    command: str,
    expected_mock_idx: int,
    not_expected_mock_idx: int,
    mocker: MockerFixture,
):
    mock_register = mocker.patch("src.main.process_handle.pokemon_register_constructor")
    mock_find_all = mocker.patch("src.main.process_handle.pokemon_find_all_constructor")
    mock_print = mocker.patch("rich.console.Console.print")
    mocks = [mock_register, mock_find_all, mock_print]
    expected_mock = mocks[expected_mock_idx]
    not_expected_mocks = [mocks[i] for i in not_expected_mock_idx]

    __execute_command(command)

    expected_mock.assert_called_once()
    for mock in not_expected_mocks:
        mock.assert_not_called()
