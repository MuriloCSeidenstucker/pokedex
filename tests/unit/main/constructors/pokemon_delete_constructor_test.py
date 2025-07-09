from pytest_mock import MockerFixture

from src.main.constructors import pokemon_delete_constructor


def test_pokemon_delete_constructor_success(mocker: MockerFixture):
    mocker.patch("src.main.constructors.pokemon_delete_constructor.PokemonsRepository")
    mock_request = {"by": "id", "value": "1"}
    mock_view = mocker.MagicMock()
    mocker.patch(
        "src.main.constructors.pokemon_delete_constructor.PokemonDeleteView",
        return_value=mock_view,
    )
    mock_view.pokemon_delete_view = mocker.MagicMock()
    mock_view.pokemon_delete_view.return_value = mock_request
    mock_view.delete_pokemon_success = mocker.MagicMock()

    mock_response = {"success": True, "message": "Success"}
    mock_controller = mocker.MagicMock()
    mocker.patch(
        "src.main.constructors.pokemon_delete_constructor.PokemonDeleteController",
        return_value=mock_controller,
    )
    mock_controller.delete = mocker.MagicMock()
    mock_controller.delete.return_value = mock_response

    pokemon_delete_constructor()

    mock_controller.delete.assert_called_once_with(
        mock_request["by"], mock_request["value"]
    )
    mock_view.pokemon_delete_view.assert_called_once()
    mock_view.delete_pokemon_success.assert_called_once_with(mock_response["message"])


def test_test_pokemon_delete_constructor_fail(mocker: MockerFixture):
    mocker.patch("src.main.constructors.pokemon_delete_constructor.PokemonsRepository")

    mock_request = {"by": "id", "value": "1"}
    mock_view = mocker.MagicMock()
    mocker.patch(
        "src.main.constructors.pokemon_delete_constructor.PokemonDeleteView",
        return_value=mock_view,
    )
    mock_view.pokemon_delete_view = mocker.MagicMock()
    mock_view.pokemon_delete_view.return_value = mock_request
    mock_view.delete_pokemon_fail = mocker.MagicMock()

    mock_response = {"success": False, "error": "Fail"}
    mock_controller = mocker.MagicMock()
    mocker.patch(
        "src.main.constructors.pokemon_delete_constructor.PokemonDeleteController",
        return_value=mock_controller,
    )
    mock_controller.delete = mocker.MagicMock()
    mock_controller.delete.return_value = mock_response

    pokemon_delete_constructor()

    mock_controller.delete.assert_called_once_with(
        mock_request["by"], mock_request["value"]
    )
    mock_view.pokemon_delete_view.assert_called_once()
    mock_view.delete_pokemon_fail.assert_called_once_with(mock_response["error"])
