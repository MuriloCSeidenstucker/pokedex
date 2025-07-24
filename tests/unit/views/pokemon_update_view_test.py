from typing import List

import pytest
from pytest_mock import MockerFixture

from src.common.pokemon import Pokemon
from src.views.pokemon_update_view import PokemonUpdateView


@pytest.mark.parametrize(
    "inputs",
    [
        (
            [
                "1",
                "9999",
                "0",
                "9999",
                "1",
                "Pokemon_Spy",
                "2",
                "grass",
                "3",
                "poison",
                "4",
                "1",
                "5",
                "0",
            ]
        ),
        (
            [
                "0",
                "Pokemon_Spy",
                "0",
                "9999",
                "1",
                "Pokemon_Spy",
                "2",
                "grass",
                "3",
                "poison",
                "4",
                "1",
                "5",
                "0",
            ]
        ),
    ],
)
def test_pokemon_update_view(inputs: List[str], mocker: MockerFixture):
    expected_pokemon = {
        "pokemon_id": inputs[3],
        "pkn_name": inputs[5],
        "type_1": inputs[7],
        "type_2": inputs[9],
        "generation": inputs[11],
        "is_legendary": inputs[13],
    }
    mock_os_system = mocker.patch("os.system")
    mock_print = mocker.patch("rich.console.Console.print")
    mock_prompt_ask = mocker.patch("rich.prompt.Prompt.ask", side_effect=inputs)

    view = PokemonUpdateView()
    request = view.pokemon_update_view()

    mock_os_system.assert_called_once_with("cls||clear")
    assert mock_print.call_count == 7
    assert mock_prompt_ask.call_count == 14
    assert request["value"] == inputs[1]
    assert request["pokemon_data"] == expected_pokemon


def test_pokemon_update_success(mocker: MockerFixture):
    mock_os_system = mocker.patch("os.system")
    mock_print = mocker.patch("rich.console.Console.print")
    mock_add_column = mocker.MagicMock()
    mocker.patch("rich.table.Table.add_column", side_effect=mock_add_column)
    mock_add_row = mocker.MagicMock()
    mocker.patch("rich.table.Table.add_row", side_effect=mock_add_row)
    mock_panel_fit = mocker.patch("rich.panel.Panel.fit")

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

    view = PokemonUpdateView()
    view.pokemon_update_success(mock_message)

    mock_os_system.assert_called_once_with("cls||clear")
    mock_print.assert_called_once()
    mock_panel_fit.assert_called_once()
    assert mock_add_column.call_count == 2
    assert mock_add_row.call_count == 8


def test_pokemon_update_fail(mocker: MockerFixture):
    mock_error = {"name": "spy test", "status_code": -1, "details": "foo"}
    mock_os_system = mocker.patch("os.system")
    mock_add_row = mocker.MagicMock()
    mocker.patch("rich.table.Table.add_row", side_effect=mock_add_row)
    mock_print = mocker.patch("rich.console.Console.print")
    mock_panel_fit = mocker.patch("rich.panel.Panel.fit")

    view = PokemonUpdateView()
    view.pokemon_update_fail(mock_error)

    mock_os_system.assert_called_once_with("cls||clear")
    mock_panel_fit.assert_called_once()
    assert mock_add_row.call_count == 2
    assert mock_print.call_count == 3
