from typing import Dict, List

import pytest
from pytest_mock import MockerFixture

from src.common.pokemon import Pokemon
from src.views.pokemon_find_all_view import PokemonFindAllView


@pytest.mark.parametrize(
    "mock_inputs,key_to_index_map,expected_calls",
    [
        (
            ["0", "fire", "1", "", "2", "1", "3", "0"],
            {"type_1": 1, "type_2": 3, "generation": 5, "is_legendary": 7},
            {
                "mock_panel_calls": 6,
                "os_system_calls": 5,
                "prompt_calls": 8,
                "print_calls": 14,
            },
        ),
        (
            ["0", "fire", "1", "grass", "0", "4"],
            {"type_1": 1, "type_2": 3},
            {
                "mock_panel_calls": 5,
                "os_system_calls": 4,
                "prompt_calls": 6,
                "print_calls": 14,
            },
        ),
    ],
)
def test_find_all_pokemon_view(
    mock_inputs: List,
    key_to_index_map: Dict,
    expected_calls: Dict,
    mocker: MockerFixture,
):
    mock_os_system = mocker.patch("os.system")
    mock_print = mocker.patch("rich.console.Console.print")
    mock_panel = mocker.patch("rich.panel.Panel.fit")
    mock_prompt = mocker.patch("rich.prompt.Prompt.ask", side_effect=mock_inputs)
    mock_add_column = mocker.patch("rich.table.Table.add_column")
    mock_add_row = mocker.patch("rich.table.Table.add_row")

    view = PokemonFindAllView()
    response = view.find_all_pokemon_view()

    assert mock_os_system.call_count == expected_calls.get("os_system_calls")
    assert mock_print.call_count == expected_calls.get("print_calls")
    assert mock_panel.call_count == expected_calls.get("mock_panel_calls")
    assert mock_prompt.call_count == expected_calls.get("prompt_calls")
    assert mock_add_column.call_count == 2
    assert mock_add_row.call_count == 5
    assert all(
        response.get(key) == mock_inputs[index]
        for key, index in key_to_index_map.items()
    )


def test_find_all_pokemons_success(mocker: MockerFixture):
    mock_message = {
        "attributes": [
            Pokemon(
                pokemon_id=1,
                pkn_name="Bulbasaur",
                type_1="Grass",
                type_2="Poison",
                generation=1,
                is_legendary=0,
            ),
            Pokemon(
                pokemon_id=2,
                pkn_name="Ivysaur",
                type_1="Grass",
                type_2="Poison",
                generation=1,
                is_legendary=0,
            ),
        ]
    }

    mock_os_system = mocker.patch("os.system")
    mock_add_column = mocker.MagicMock()
    mocker.patch("rich.table.Table.add_column", side_effect=mock_add_column)
    mock_add_row = mocker.MagicMock()
    mocker.patch("rich.table.Table.add_row", side_effect=mock_add_row)
    mock_print = mocker.MagicMock()
    mocker.patch("rich.console.Console.print", side_effect=mock_print)

    view = PokemonFindAllView()
    view.find_all_pokemons_success(mock_message)

    mock_os_system.assert_called_once_with("cls||clear")
    mock_add_column.assert_called()
    mock_add_row.assert_called()
    mock_print.assert_called_once()


def test_find_all_pokemons_fail(mocker: MockerFixture):
    mock_error = {
        "name": "spy error",
        "status_code": -1,
        "details": "foo",
    }
    mock_os_system = mocker.patch("os.system")
    mock_add_row = mocker.MagicMock()
    mocker.patch("rich.table.Table.add_row", side_effect=mock_add_row)
    mock_print = mocker.patch("rich.console.Console.print")
    mock_panel_fit = mocker.patch("rich.panel.Panel.fit")

    view = PokemonFindAllView()
    view.find_all_pokemons_fail(mock_error)

    mock_os_system.assert_called_once_with("cls||clear")
    mock_panel_fit.assert_called_once()
    assert mock_add_row.call_count == 2
    assert mock_print.call_count == 3
