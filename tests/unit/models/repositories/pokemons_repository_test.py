# pylint: disable=C0301:line-too-long

from typing import List

from pytest_mock import MockerFixture

from src.common.by import By
from src.common.exceptions import PokemonNotFoundError
from src.common.pokemon import Pokemon
from src.models.entities.pokemons_entity import PokemonsEntity
from src.models.repositories.pokemons_repository import PokemonsRepository


def test_insert_pokemon(mocker: MockerFixture):
    pokemon = Pokemon(
        pokemon_id=4,
        pkn_name="Charmander",
        type_1="Fire",
        type_2="",
        generation=1,
        is_legendary=0,
    )

    mock_session = mocker.MagicMock()
    mock_sessionmaker = mocker.MagicMock(return_value=mock_session)
    mock_db_handler = mocker.MagicMock()
    mock_db_handler.__enter__.return_value = mock_db_handler
    mock_db_handler.session = mock_session
    mocker.patch(
        "src.models.repositories.pokemons_repository.DBConnectionHandler",
        return_value=mock_db_handler,
    )
    mocker.patch(
        "src.models.repositories.pokemons_repository.DBConnectionHandler.sqlalchemy.orm.sessionmaker",
        return_value=mock_sessionmaker,
    )

    repo = PokemonsRepository()
    repo.insert_pokemon(pokemon)

    assert mock_session.add.called
    called_args = mock_session.add.call_args[0][0]
    assert isinstance(called_args, PokemonsEntity)
    assert called_args.pokemon_id == pokemon.pokemon_id
    assert called_args.pkn_name == pokemon.pkn_name
    assert called_args.type_1 == pokemon.type_1
    assert called_args.type_2 == pokemon.type_2
    assert called_args.generation == pokemon.generation
    assert called_args.is_legendary == pokemon.is_legendary
    mock_session.commit.assert_called_once()
    mock_session.rollback.assert_not_called()


def test_insert_pokemon_error(mocker: MockerFixture):
    mock_session = mocker.MagicMock()
    mock_sessionmaker = mocker.MagicMock(return_value=mock_session)
    mock_db_handler = mocker.MagicMock()
    mock_db_handler.__enter__.return_value = mock_db_handler
    mock_db_handler.session = mock_session
    mocker.patch(
        "src.models.repositories.pokemons_repository.DBConnectionHandler",
        return_value=mock_db_handler,
    )
    mocker.patch(
        "src.models.repositories.pokemons_repository.DBConnectionHandler.sqlalchemy.orm.sessionmaker",
        return_value=mock_sessionmaker,
    )

    repo = PokemonsRepository()
    try:
        repo.insert_pokemon(None)
        assert False, "Expected exception not raised"
    except Exception as e:
        assert str(e) == "'NoneType' object has no attribute 'pokemon_id'"

    assert not mock_session.add.called
    mock_session.commit.assert_not_called()
    mock_session.rollback.assert_called_once()


def test_select_pokemon(mocker: MockerFixture):
    mock_pokemon = Pokemon(
        pokemon_id=1,
        pkn_name="Bulbasaur",
        type_1="Grass",
        type_2="Poison",
        generation=1,
        is_legendary=0,
    )
    mock_filter = mocker.MagicMock()
    mock_filter.first.return_value = mock_pokemon
    mock_query = mocker.MagicMock()
    mock_query.filter.return_value = mock_filter
    mock_session = mocker.MagicMock()
    mock_session.query.return_value = mock_query
    mock_sessionmaker = mocker.MagicMock(return_value=mock_session)
    mock_db_handler = mocker.MagicMock()
    mock_db_handler.__enter__.return_value = mock_db_handler
    mock_db_handler.session = mock_session
    mocker.patch(
        "src.models.repositories.pokemons_repository.DBConnectionHandler",
        return_value=mock_db_handler,
    )
    mocker.patch(
        "src.models.repositories.pokemons_repository.DBConnectionHandler.sqlalchemy.orm.sessionmaker",
        return_value=mock_sessionmaker,
    )

    repo = PokemonsRepository()
    response = repo.select_pokemon(By.NAME, "Bulbasaur")

    mock_session.query.assert_called_once_with(PokemonsEntity)
    mock_query.filter.assert_called_once()
    mock_filter.first.assert_called_once()
    mock_session.rollback.assert_not_called()
    assert isinstance(response, Pokemon)
    assert response == mock_pokemon
    assert response.pkn_name == "Bulbasaur"


def test_select_pokemon_by_error():
    repo = PokemonsRepository()
    try:
        repo.select_pokemon("pkn_name", "Bulbasaur")
        assert False, "Expected exception not raised"
    except Exception as e:
        assert str(e) == "Invalid argument: pkn_name"


def test_select_pokemon_error(mocker: MockerFixture):
    mock_filter = mocker.MagicMock()
    mock_filter.first.return_value = None
    mock_query = mocker.MagicMock()
    mock_query.filter.return_value = mock_filter
    mock_session = mocker.MagicMock()
    mock_session.query.return_value = mock_query
    mock_sessionmaker = mocker.MagicMock(return_value=mock_session)
    mock_db_handler = mocker.MagicMock()
    mock_db_handler.__enter__.return_value = mock_db_handler
    mock_db_handler.session = mock_session
    mocker.patch(
        "src.models.repositories.pokemons_repository.DBConnectionHandler",
        return_value=mock_db_handler,
    )
    mocker.patch(
        "src.models.repositories.pokemons_repository.DBConnectionHandler.sqlalchemy.orm.sessionmaker",
        return_value=mock_sessionmaker,
    )

    repo = PokemonsRepository()
    try:
        repo.select_pokemon("name", "Bulbasaur")
        assert False, "Expected exception not raised"
    except PokemonNotFoundError as e:
        assert str(e) == "pokemon not found in repository"


def test_select_all_pokemons(mocker: MockerFixture):
    mock_pokemon_1 = Pokemon(
        pokemon_id=1,
        pkn_name="Bulbasaur",
        type_1="Grass",
        type_2="Poison",
        generation=1,
        is_legendary=0,
    )
    mock_pokemon_2 = Pokemon(
        pokemon_id=2,
        pkn_name="Ivysaur",
        type_1="Grass",
        type_2="Poison",
        generation=1,
        is_legendary=0,
    )
    expected_pokemons = [mock_pokemon_1, mock_pokemon_2]
    mock_query = mocker.MagicMock()
    mock_query.all.return_value = expected_pokemons
    mock_session = mocker.MagicMock()
    mock_session.query.return_value = mock_query
    mock_sessionmaker = mocker.MagicMock(return_value=mock_session)
    mock_db_handler = mocker.MagicMock()
    mock_db_handler.__enter__.return_value = mock_db_handler
    mock_db_handler.session = mock_session
    mocker.patch(
        "src.models.repositories.pokemons_repository.DBConnectionHandler",
        return_value=mock_db_handler,
    )
    mocker.patch(
        "src.models.repositories.pokemons_repository.DBConnectionHandler.sqlalchemy.orm.sessionmaker",
        return_value=mock_sessionmaker,
    )

    repo = PokemonsRepository()
    response = repo.select_all_pokemons()

    mock_session.query.assert_called_once_with(PokemonsEntity)
    mock_query.all.assert_called_once()
    mock_session.rollback.assert_not_called()
    assert isinstance(response, List)
    assert response == expected_pokemons
    assert len(response) == 2
    assert response[0].pkn_name == "Bulbasaur"
    assert response[1].pkn_name == "Ivysaur"


def test_select_all_pokemons_error(mocker: MockerFixture):
    mock_query = mocker.MagicMock()
    mock_query.all.side_effect = Exception("NotFound")
    mock_session = mocker.MagicMock()
    mock_session.query.return_value = mock_query
    mock_sessionmaker = mocker.MagicMock(return_value=mock_session)
    mock_db_handler = mocker.MagicMock()
    mock_db_handler.__enter__.return_value = mock_db_handler
    mock_db_handler.session = mock_session
    mocker.patch(
        "src.models.repositories.pokemons_repository.DBConnectionHandler",
        return_value=mock_db_handler,
    )
    mocker.patch(
        "src.models.repositories.pokemons_repository.DBConnectionHandler.sqlalchemy.orm.sessionmaker",
        return_value=mock_sessionmaker,
    )

    repo = PokemonsRepository()
    try:
        repo.select_all_pokemons()
        assert False, "Expected exception not raised"
    except Exception as e:
        assert str(e) == "NotFound"

    mock_session.query.assert_called_once_with(PokemonsEntity)
    mock_query.all.assert_called_once()
    mock_session.rollback.assert_called_once()


def test_update_pokemon(mocker: MockerFixture):
    mock_after_pokemon = Pokemon(
        pokemon_id=9999,
        pkn_name="Pokemon_Spy",
        type_1="Eletric",
        type_2="",
        generation=9,
        is_legendary=1,
    )
    expected_result = {
        "pokemon_id": 9999,
        "pkn_name": "Pokemon_Spy",
        "type_1": "Eletric",
        "type_2": "",
        "generation": 9,
        "is_legendary": 1,
    }
    mock_filter = mocker.MagicMock()
    mock_filter.update = mocker.MagicMock()
    mock_filter.one_or_none = mocker.MagicMock()
    mock_filter.one_or_none.return_value = mock_after_pokemon
    mock_query = mocker.MagicMock()
    mock_query.filter.return_value = mock_filter
    mock_session = mocker.MagicMock()
    mock_session.query.return_value = mock_query
    mock_sessionmaker = mocker.MagicMock(return_value=mock_session)
    mock_db_handler = mocker.MagicMock()
    mock_db_handler.__enter__.return_value = mock_db_handler
    mock_db_handler.session = mock_session
    mocker.patch(
        "src.models.repositories.pokemons_repository.DBConnectionHandler",
        return_value=mock_db_handler,
    )
    mocker.patch(
        "src.models.repositories.pokemons_repository.DBConnectionHandler.sqlalchemy.orm.sessionmaker",
        return_value=mock_sessionmaker,
    )

    repo = PokemonsRepository()
    repo.update_pokemon(By.ID, 9999, mock_after_pokemon)

    assert mock_session.query.call_count == 2
    mock_session.query.assert_called_with(PokemonsEntity)
    assert mock_query.filter.call_count == 2
    mock_filter.update.assert_called_once()
    mock_filter.one_or_none.assert_called_once()
    mock_filter.update.assert_called_once_with(expected_result)


def test_update_pokemon_by_error():
    repo = PokemonsRepository()
    try:
        repo.update_pokemon("pkn_name", "Bulbasaur", "mock_pokemon")
        assert False, "Expected exception not raised"
    except Exception as e:
        assert str(e) == "Invalid argument: pkn_name"


def test_update_pokemon_error(mocker: MockerFixture):
    mock_updated_pokemon = Pokemon(
        pokemon_id=9999,
        pkn_name="Pokemon_Spy",
        type_1="Eletric",
        type_2="",
        generation=9,
        is_legendary=1,
    )
    mock_filter = mocker.MagicMock()
    mock_filter.update = mocker.MagicMock()
    mock_filter.one_or_none.return_value = None
    mock_query = mocker.MagicMock()
    mock_query.filter.return_value = mock_filter
    mock_session = mocker.MagicMock()
    mock_session.query.return_value = mock_query
    mock_sessionmaker = mocker.MagicMock(return_value=mock_session)
    mock_db_handler = mocker.MagicMock()
    mock_db_handler.__enter__.return_value = mock_db_handler
    mock_db_handler.session = mock_session
    mocker.patch(
        "src.models.repositories.pokemons_repository.DBConnectionHandler",
        return_value=mock_db_handler,
    )
    mocker.patch(
        "src.models.repositories.pokemons_repository.DBConnectionHandler.sqlalchemy.orm.sessionmaker",
        return_value=mock_sessionmaker,
    )

    repo = PokemonsRepository()
    try:
        repo.update_pokemon(By.ID, 9999, mock_updated_pokemon)
        assert False, "Expected exception not raised"
    except Exception as e:
        assert str(e) == "No Pokemon found with id = 9999"


def test_delete_pokemon(mocker: MockerFixture):
    expected_pokemon = Pokemon(
        pokemon_id=1,
        pkn_name="Bulbasaur",
        type_1="Grass",
        type_2="Poison",
        generation=1,
        is_legendary=0,
    )
    mock_filter = mocker.MagicMock()
    mock_filter.delete = mocker.MagicMock()
    mock_filter.one_or_none = mocker.MagicMock()
    mock_filter.one_or_none.return_value = expected_pokemon
    mock_query = mocker.MagicMock()
    mock_query.filter.return_value = mock_filter
    mock_session = mocker.MagicMock()
    mock_session.query.return_value = mock_query
    mock_sessionmaker = mocker.MagicMock(return_value=mock_session)
    mock_db_handler = mocker.MagicMock()
    mock_db_handler.__enter__.return_value = mock_db_handler
    mock_db_handler.session = mock_session
    mocker.patch(
        "src.models.repositories.pokemons_repository.DBConnectionHandler",
        return_value=mock_db_handler,
    )
    mocker.patch(
        "src.models.repositories.pokemons_repository.DBConnectionHandler.sqlalchemy.orm.sessionmaker",
        return_value=mock_sessionmaker,
    )

    repo = PokemonsRepository()
    result = repo.delete_pokemon(By.ID, 9999)

    assert mock_session.query.call_count == 2
    mock_session.query.assert_called_with(PokemonsEntity)
    assert mock_query.filter.call_count == 2
    mock_filter.delete.assert_called_once()
    mock_filter.one_or_none.assert_called_once()
    assert isinstance(result, Pokemon)
    assert result == expected_pokemon


def test_delete_pokemon_by_error():
    repo = PokemonsRepository()
    try:
        repo.delete_pokemon("pkn_name", "Bulbasaur")
        assert False, "Expected exception not raised"
    except Exception as e:
        assert str(e) == "Invalid argument: pkn_name"


def test_delete_pokemon_error(mocker: MockerFixture):
    mock_filter = mocker.MagicMock()
    mock_filter.one_or_none.return_value = None
    mock_query = mocker.MagicMock()
    mock_query.filter.return_value = mock_filter
    mock_session = mocker.MagicMock()
    mock_session.query.return_value = mock_query
    mock_sessionmaker = mocker.MagicMock(return_value=mock_session)
    mock_db_handler = mocker.MagicMock()
    mock_db_handler.__enter__.return_value = mock_db_handler
    mock_db_handler.session = mock_session
    mocker.patch(
        "src.models.repositories.pokemons_repository.DBConnectionHandler",
        return_value=mock_db_handler,
    )
    mocker.patch(
        "src.models.repositories.pokemons_repository.DBConnectionHandler.sqlalchemy.orm.sessionmaker",
        return_value=mock_sessionmaker,
    )

    repo = PokemonsRepository()
    try:
        repo.delete_pokemon("name", "Bulbasaur")
        assert False, "Expected exception not raised"
    except Exception as e:
        assert str(e) == "No Pokemon found with name = Bulbasaur"
