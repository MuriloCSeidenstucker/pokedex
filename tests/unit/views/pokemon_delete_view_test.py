import pytest
from pytest_mock import MockerFixture

from src.views.pokemon_delete_view import PokemonDeleteView


@pytest.mark.parametrize(
    "by_input,value_input",
    [
        ("1", "9999"),
        ("0", "Pokemon_Spy"),
    ],
)
def test_pokemon_delete_view(by_input: str, value_input: str, mocker: MockerFixture):
    mock_os_system = mocker.patch("os.system")
    mock_print = mocker.patch("rich.console.Console.print")
    mock_input = mocker.patch(
        "rich.console.Console.input", side_effect=[by_input, value_input]
    )

    view = PokemonDeleteView()
    request = view.pokemon_delete_view()

    mock_os_system.assert_called_once_with("cls||clear")
    mock_print.assert_called_once()
    assert mock_input.call_count == 2
    assert request["value"] == value_input


def test_delete_pokemon_success(mocker: MockerFixture):
    mock_os_system = mocker.patch("os.system")
    mock_print = mocker.patch("rich.console.Console.print")

    mock_message = {
        "type": "Spy",
        "count": 1,
        "attributes": {
            "pokemon_id": "1",
            "pkn_name": "Pokemon_Spy",
            "type_1": "Pkn_Type_1",
            "type_2": "Pkn_Type_2",
            "generation": "1",
            "is_legendary": "0",
        },
    }

    view = PokemonDeleteView()
    view.delete_pokemon_success(mock_message)

    mock_os_system.assert_called_once_with("cls||clear")
    mock_print.assert_called_once()


def test_delete_pokemon_fail(mocker: MockerFixture):
    mock_os_system = mocker.patch("os.system")
    mock_print = mocker.patch("rich.console.Console.print")

    view = PokemonDeleteView()
    view.delete_pokemon_fail("Test")

    mock_os_system.assert_called_once_with("cls||clear")
    mock_print.assert_called_once()
