# pylint: disable=W0613:unused-argument

from typing import Dict

from pytest_mock import MockerFixture

from src.main.constructors.pokemon_register_constructor import (
    pokemon_register_constructor,
)


def fake_registry_pokemon_view() -> Dict:
    return {"name": "Pokemon_Spy", "type": "PTipo_Spy"}


def fake_registry_pokemon_success(message: Dict) -> None: ...


def fake_registry_pokemon_fail(error: str) -> None: ...


def fake_register(new_pokemon_info: Dict) -> Dict:
    response = {"count": 1, "type": "Pokemon", "attributes": new_pokemon_info}
    return {"success": True, "message": response}


def fake_register_fail(new_pokemon_info: Dict) -> Dict:
    response = {"count": 1, "type": "Pokemon", "attributes": new_pokemon_info}
    return {"success": False, "error": response}


def test_pokemon_register_constructor(mocker: MockerFixture):
    spy_view_register = mocker.patch(
        "src.views.pokemon_register_view.PokemonRegisterView.registry_pokemon_view",
        side_effect=fake_registry_pokemon_view,
    )
    spy_view_success = mocker.patch(
        "src.views.pokemon_register_view.PokemonRegisterView.registry_pokemon_success",
        side_effect=fake_registry_pokemon_success,
    )
    spy_controller = mocker.patch(
        "src.controllers.pokemon_register_controller.PokemonRegisterController.register",
        side_effect=fake_register,
    )

    pokemon_register_constructor()

    assert (
        spy_view_register.called and spy_controller.called and spy_view_success.called
    )


def test_pokemon_register_constructor_fail(mocker: MockerFixture):
    spy_view_register = mocker.patch(
        "src.views.pokemon_register_view.PokemonRegisterView.registry_pokemon_view",
        side_effect=fake_registry_pokemon_view,
    )
    spy_view_register_fail = mocker.patch(
        "src.views.pokemon_register_view.PokemonRegisterView.registry_pokemon_fail",
        side_effect=fake_registry_pokemon_fail,
    )
    spy_controller = mocker.patch(
        "src.controllers.pokemon_register_controller.PokemonRegisterController.register",
        side_effect=fake_register_fail,
    )

    pokemon_register_constructor()

    assert (
        spy_view_register.called
        and spy_controller.called
        and spy_view_register_fail.called
    )
