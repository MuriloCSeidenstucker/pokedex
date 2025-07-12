from pytest_mock import MockerFixture

from src.main.constructors import pokemon_update_constructor


def test_pokemon_update_constructor_success(mocker: MockerFixture):
    mocker.patch("src.main.constructors.pokemon_update_constructor.PokemonsRepository")
    mock_request = {"by": "id", "value": "1", "pokemon_data": "Pokemon_Spy"}
    mock_view = mocker.MagicMock()
    mocker.patch(
        "src.main.constructors.pokemon_update_constructor.PokemonUpdateView",
        return_value=mock_view,
    )
    mock_view.pokemon_update_view = mocker.MagicMock()
    mock_view.pokemon_update_view.return_value = mock_request
    mock_view.pokemon_update_success = mocker.MagicMock()

    mock_response = {"success": True, "message": "Success"}
    mock_controller = mocker.MagicMock()
    mocker.patch(
        "src.main.constructors.pokemon_update_constructor.PokemonUpdateController",
        return_value=mock_controller,
    )
    mock_controller.update = mocker.MagicMock()
    mock_controller.update.return_value = mock_response

    pokemon_update_constructor()

    mock_controller.update.assert_called_once_with(
        mock_request["by"], mock_request["value"], mock_request["pokemon_data"]
    )
    mock_view.pokemon_update_view.assert_called_once()
    mock_view.pokemon_update_success.assert_called_once_with(mock_response["message"])


def test_pokemon_update_constructor_fail(mocker: MockerFixture):
    mocker.patch("src.main.constructors.pokemon_update_constructor.PokemonsRepository")
    mock_request = {"by": "id", "value": "1", "pokemon_data": "Pokemon_Spy"}
    mock_view = mocker.MagicMock()
    mocker.patch(
        "src.main.constructors.pokemon_update_constructor.PokemonUpdateView",
        return_value=mock_view,
    )
    mock_view.pokemon_update_view = mocker.MagicMock()
    mock_view.pokemon_update_view.return_value = mock_request
    mock_view.pokemon_update_fail = mocker.MagicMock()

    mock_response = {"success": False, "error": "Fail"}
    mock_controller = mocker.MagicMock()
    mocker.patch(
        "src.main.constructors.pokemon_update_constructor.PokemonUpdateController",
        return_value=mock_controller,
    )
    mock_controller.update = mocker.MagicMock()
    mock_controller.update.return_value = mock_response

    pokemon_update_constructor()

    mock_controller.update.assert_called_once_with(
        mock_request["by"], mock_request["value"], mock_request["pokemon_data"]
    )
    mock_view.pokemon_update_view.assert_called_once()
    mock_view.pokemon_update_fail.assert_called_once_with(mock_response["error"])
