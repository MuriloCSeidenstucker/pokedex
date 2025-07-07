from pytest_mock import MockerFixture

from src.main.constructors.pokemon_find_all_constructor import (
    pokemon_find_all_constructor,
)


def test_pokemon_find_all_constructor_success(mocker: MockerFixture):
    response_result = {"success": True, "message": "Success"}
    mock_controller = mocker.MagicMock()
    mocker.patch(
        "src.main.constructors.pokemon_find_all_constructor.PokemonFindAllController",
        return_value=mock_controller,
    )
    mock_controller.find_all = mocker.MagicMock()
    mock_controller.find_all.return_value = response_result
    mock_view = mocker.MagicMock()
    mocker.patch(
        "src.main.constructors.pokemon_find_all_constructor.PokemonFindAllView",
        return_value=mock_view,
    )
    mock_view.find_all_pokemons_success = mocker.MagicMock()

    pokemon_find_all_constructor()

    mock_controller.find_all.assert_called_once()
    mock_view.find_all_pokemons_success.assert_called_once_with(
        response_result["message"]
    )


def test_pokemon_find_all_constructor_fail(mocker: MockerFixture):
    response_result = {"success": False, "error": "Fail"}
    mock_controller = mocker.MagicMock()
    mocker.patch(
        "src.main.constructors.pokemon_find_all_constructor.PokemonFindAllController",
        return_value=mock_controller,
    )
    mock_controller.find_all = mocker.MagicMock()
    mock_controller.find_all.return_value = response_result
    mock_view = mocker.MagicMock()
    mocker.patch(
        "src.main.constructors.pokemon_find_all_constructor.PokemonFindAllView",
        return_value=mock_view,
    )
    mock_view.find_all_pokemons_fail = mocker.MagicMock()

    pokemon_find_all_constructor()

    mock_controller.find_all.assert_called_once()
    mock_view.find_all_pokemons_fail.assert_called_once_with(response_result["error"])
