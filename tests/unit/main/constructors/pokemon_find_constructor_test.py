from pytest_mock import MockerFixture

from src.main.constructors import pokemon_find_constructor


def test_pokemon_find_constructor_success(mocker: MockerFixture):
    mocker.patch("src.main.constructors.pokemon_find_constructor.PokemonsRepository")
    mock_request = {"by": "id", "value": "1"}
    mock_view = mocker.MagicMock()
    mocker.patch(
        "src.main.constructors.pokemon_find_constructor.PokemonFindView",
        return_value=mock_view,
    )
    mock_view.pokemon_find_view = mocker.MagicMock()
    mock_view.pokemon_find_view.return_value = mock_request
    mock_view.pokemon_find_success = mocker.MagicMock()

    mock_response = {"success": True, "message": "Success"}
    mock_controller = mocker.MagicMock()
    mocker.patch(
        "src.main.constructors.pokemon_find_constructor.PokemonFindController",
        return_value=mock_controller,
    )
    mock_controller.find = mocker.MagicMock()
    mock_controller.find.return_value = mock_response

    pokemon_find_constructor()

    mock_controller.find.assert_called_once_with(
        mock_request["by"], mock_request["value"]
    )
    mock_view.pokemon_find_view.assert_called_once()
    mock_view.pokemon_find_success.assert_called_once_with(mock_response["message"])


def test_pokemon_find_constructor_fail(mocker: MockerFixture):
    mocker.patch("src.main.constructors.pokemon_find_constructor.PokemonsRepository")

    mock_request = {"by": "id", "value": "1"}
    mock_view = mocker.MagicMock()
    mocker.patch(
        "src.main.constructors.pokemon_find_constructor.PokemonFindView",
        return_value=mock_view,
    )
    mock_view.pokemon_find_view = mocker.MagicMock()
    mock_view.pokemon_find_view.return_value = mock_request
    mock_view.pokemon_find_fail = mocker.MagicMock()

    mock_response = {"success": False, "error": "Fail"}
    mock_controller = mocker.MagicMock()
    mocker.patch(
        "src.main.constructors.pokemon_find_constructor.PokemonFindController",
        return_value=mock_controller,
    )
    mock_controller.find = mocker.MagicMock()
    mock_controller.find.return_value = mock_response

    pokemon_find_constructor()

    mock_controller.find.assert_called_once_with(
        mock_request["by"], mock_request["value"]
    )
    mock_view.pokemon_find_view.assert_called_once()
    mock_view.pokemon_find_fail.assert_called_once_with(mock_response["error"])
