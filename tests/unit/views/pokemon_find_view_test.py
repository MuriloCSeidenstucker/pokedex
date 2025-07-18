import pytest
from pytest_mock import MockerFixture

from src.common.pokemon import Pokemon
from src.views.pokemon_find_view import PokemonFindView


@pytest.mark.parametrize(
    "by_input,value_input",
    [
        ("1", "9999"),
        ("0", "Pokemon_Spy"),
    ],
)
def test_pokemon_find_view(by_input: str, value_input: str, mocker: MockerFixture):
    mock_os_system = mocker.patch("os.system")
    mock_add_column = mocker.MagicMock()
    mocker.patch("rich.table.Table.add_column", side_effect=mock_add_column)
    mock_add_row = mocker.MagicMock()
    mocker.patch("rich.table.Table.add_row", side_effect=mock_add_row)
    mock_print = mocker.patch("rich.console.Console.print")
    mock_inputs = [by_input, value_input]
    mock_prompt_ask = mocker.patch("rich.prompt.Prompt.ask", side_effect=mock_inputs)

    view = PokemonFindView()
    request = view.pokemon_find_view()

    mock_os_system.assert_called_once_with("cls||clear")
    mock_print.assert_called_once()
    assert mock_prompt_ask.call_count == 2
    assert mock_add_column.call_count == 2
    assert mock_add_row.call_count == 2
    assert request["value"] == value_input


def test_pokemon_find_success(mocker: MockerFixture):
    mock_os_system = mocker.patch("os.system")
    mock_print = mocker.patch("rich.console.Console.print")

    mock_message = {
        "type": "Spy",
        "count": 1,
        "attributes": Pokemon(
            pokemon_id=1,
            pkn_name="Pokemon_Spy",
            type_1="Pkn_Type_1",
            type_2="Pkn_Type_2",
            generation=1,
            is_legendary=0,
        ),
    }

    view = PokemonFindView()
    view.pokemon_find_success(mock_message)

    mock_os_system.assert_called_once_with("cls||clear")
    mock_print.assert_called()


def test_pokemon_find_fail(mocker: MockerFixture):
    mock_error = {"name": "spy error", "status_code": 1, "details": "foo"}
    mock_os_system = mocker.patch("os.system")
    mock_print = mocker.patch("rich.console.Console.print")

    view = PokemonFindView()
    view.pokemon_find_fail(mock_error)

    mock_os_system.assert_called_once_with("cls||clear")
    mock_print.assert_called()
