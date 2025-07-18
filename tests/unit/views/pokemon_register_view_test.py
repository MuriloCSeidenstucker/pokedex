from typing import Dict

from pytest_mock import MockerFixture

from src.views.pokemon_register_view import PokemonRegisterView


def test_registry_pokemon_view(mocker: MockerFixture):
    mock_os_system = mocker.patch("os.system")
    mock_print = mocker.patch("rich.console.Console.print")
    mock_inputs = ["1", "Bulbasaur", "Grass", "Poison", "1", "0"]
    mock_prompt_ask = mocker.patch("rich.prompt.Prompt.ask", side_effect=mock_inputs)
    mock_panel_fit = mocker.patch("rich.panel.Panel.fit")

    view = PokemonRegisterView()
    request = view.registry_pokemon_view()

    mock_os_system.assert_called_once_with("cls||clear")
    mock_print.assert_called_once()
    mock_panel_fit.assert_called_once()
    assert mock_prompt_ask.call_count == 6
    assert isinstance(request, Dict)
    assert request["pkn_name"] == mock_inputs[1]


def test_registry_pokemon_success(mocker: MockerFixture):
    mock_response = {
        "type": "Spy",
        "count": "1",
        "attributes": {
            "pokemon_id": "1",
            "pkn_name": "Bulbasaur",
            "type_1": "Grass",
            "type_2": "Poison",
            "generation": "1",
            "is_legendary": "0",
        },
    }
    mock_os_system = mocker.patch("os.system")
    mock_add_column = mocker.MagicMock()
    mocker.patch("rich.table.Table.add_column", side_effect=mock_add_column)
    mock_add_row = mocker.MagicMock()
    mocker.patch("rich.table.Table.add_row", side_effect=mock_add_row)
    mock_panel_fit = mocker.patch("rich.panel.Panel.fit")
    mock_print = mocker.patch("rich.console.Console.print")

    view = PokemonRegisterView()
    view.registry_pokemon_success(mock_response)

    mock_os_system.assert_called_once_with("cls||clear")
    mock_panel_fit.assert_called_once()
    mock_print.assert_called_once()
    assert mock_add_column.call_count == 2
    assert mock_add_row.call_count == 8


def test_registry_pokemon_fail(mocker: MockerFixture):
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

    view = PokemonRegisterView()
    view.registry_pokemon_fail(mock_error)

    mock_os_system.assert_called_once_with("cls||clear")
    mock_panel_fit.assert_called_once()
    assert mock_add_row.call_count == 2
    assert mock_print.call_count == 3
