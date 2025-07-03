# pylint: disable=C0301:line-too-long

from pytest_mock import MockerFixture

from src.models.entities.pokemons_entity import PokemonsEntity
from src.models.repositories.pokemons_repository import PokemonsRepository


def test_insert_pokemon(mocker: MockerFixture):
    request = {
        "pokemon_id": "1",
        "pkn_name": "Bulbasaur",
        "type_1": "Grass",
        "type_2": "Poison",
        "generation": "1",
        "is_legendary": "0",
    }

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
    repo.insert_pokemon(request)

    assert mock_session.add.called
    called_args = mock_session.add.call_args[0][0]
    assert isinstance(called_args, PokemonsEntity)
    assert called_args.pokemon_id == request["pokemon_id"]
    assert called_args.pkn_name == request["pkn_name"]
    assert called_args.type_1 == request["type_1"]
    assert called_args.type_2 == request["type_2"]
    assert called_args.generation == request["generation"]
    assert called_args.is_legendary == request["is_legendary"]
    mock_session.commit.assert_called_once()
    mock_session.rollback.assert_not_called()


def test_insert_pokemon_error(mocker: MockerFixture):
    request = {}

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
        repo.insert_pokemon(request)
        assert False, "Expected exception not raised"
    except Exception as e:
        assert str(e) == "'pokemon_id'"

    assert not mock_session.add.called
    mock_session.commit.assert_not_called()
    mock_session.rollback.assert_called_once()
