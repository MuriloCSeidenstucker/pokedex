from pytest_mock import MockerFixture

from src.common.pokemon import Pokemon
from src.views.pokemon_find_all_view import PokemonFindAllView


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

    mock_add_column = mocker.MagicMock()
    mocker.patch("rich.table.Table.add_column", side_effect=mock_add_column)
    mock_add_row = mocker.MagicMock()
    mocker.patch("rich.table.Table.add_row", side_effect=mock_add_row)
    mock_print = mocker.MagicMock()
    mocker.patch("rich.console.Console.print", side_effect=mock_print)

    view = PokemonFindAllView()
    view.find_all_pokemons_success(mock_message)

    mock_add_column.assert_called()
    mock_add_row.assert_called()
    mock_print.assert_called_once()


def test_find_all_pokemons_fail(mocker: MockerFixture):
    mock_system = mocker.MagicMock()
    mocker.patch("os.system", side_effect=mock_system)
    mock_print = mocker.MagicMock()
    mocker.patch("rich.console.Console.print", side_effect=mock_print)

    view = PokemonFindAllView()
    view.find_all_pokemons_fail("")

    mock_system.assert_called_once()
    mock_print.assert_called()
