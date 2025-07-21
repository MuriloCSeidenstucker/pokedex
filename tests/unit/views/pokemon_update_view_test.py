from pytest_mock import MockerFixture

from src.common.pokemon import Pokemon
from src.views.pokemon_update_view import PokemonUpdateView


def test_pokemon_update_view(mocker: MockerFixture):
    mock_inputs = [
        "1",
        "9999",
        "9999",
        "Pokemon_Spy",
        "Grass",
        "Poison",
        "1",
        "0",
    ]
    expected_pokemon = {
        "pokemon_id": mock_inputs[2],
        "pkn_name": mock_inputs[3],
        "type_1": mock_inputs[4],
        "type_2": mock_inputs[5],
        "generation": mock_inputs[6],
        "is_legendary": mock_inputs[7],
    }
    mock_os_system = mocker.patch("os.system")
    mock_print = mocker.patch("rich.console.Console.print")
    mock_input = mocker.patch("rich.console.Console.input", side_effect=mock_inputs)

    view = PokemonUpdateView()
    request = view.pokemon_update_view()

    mock_os_system.assert_called_once_with("cls||clear")
    mock_print.assert_called_once()
    assert mock_input.call_count == 8
    assert request["by"] == "id"
    assert request["value"] == mock_inputs[1]
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
