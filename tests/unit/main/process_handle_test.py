import pytest
from pytest_mock import MockerFixture

from src.main.process_handle import (
    __display_menu_and_get_command,
    __execute_command,
    start,
)


def test_start(mocker: MockerFixture):
    mock_display_menu = mocker.patch(
        "src.main.process_handle.__display_menu_and_get_command", return_value="6"
    )
    mock_execute_command = mocker.patch(
        "src.main.process_handle.__execute_command", return_value=False
    )

    start()

    mock_display_menu.assert_called_once()
    mock_execute_command.assert_called_once_with("6")


def test_display_menu_and_get_command(mocker: MockerFixture):
    mock_process = mocker.patch("src.main.process_handle.introduction_process")

    __display_menu_and_get_command()

    mock_process.assert_called_once()


@pytest.mark.parametrize(
    "command,expected_mock_idx,not_expected_mock_idx",
    [
        ("1", 0, [1, 2, 3, 4, 5]),
        ("2", 1, [0, 2, 3, 4, 5]),
        ("3", 2, [0, 1, 3, 4, 5]),
        ("4", 3, [0, 1, 2, 4, 5]),
        ("5", 4, [0, 1, 2, 3, 5]),
        ("A", 5, [0, 1, 2, 3, 4]),
    ],
)
def test_execute_command(
    command: str,
    expected_mock_idx: int,
    not_expected_mock_idx: int,
    mocker: MockerFixture,
):
    mock_register = mocker.patch("src.main.process_handle.pokemon_register_constructor")
    mock_find = mocker.patch("src.main.process_handle.pokemon_find_constructor")
    mock_find_all = mocker.patch("src.main.process_handle.pokemon_find_all_constructor")
    mock_update = mocker.patch("src.main.process_handle.pokemon_update_constructor")
    mock_delete = mocker.patch("src.main.process_handle.pokemon_delete_constructor")
    mock_print = mocker.patch("rich.console.Console.print")
    mocks = [
        mock_register,
        mock_find,
        mock_find_all,
        mock_update,
        mock_delete,
        mock_print,
    ]
    expected_mock = mocks[expected_mock_idx]
    not_expected_mocks = [mocks[i] for i in not_expected_mock_idx]

    __execute_command(command)

    expected_mock.assert_called_once()
    for mock in not_expected_mocks:
        mock.assert_not_called()
