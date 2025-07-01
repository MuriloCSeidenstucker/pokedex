import pytest

from src.models.settings.connection import DBConnectionHandler


@pytest.mark.skip(reason="sensitive test")
def test_db_connection_handler_with_sqlite_memory():
    """Teste de integração da conexão usando SQLite em memória"""
    handler = DBConnectionHandler(connection_string="sqlite:///:memory:")

    engine = handler.get_engine()
    assert engine is not None
    assert "sqlite" in str(engine.url)

    with handler as db:
        assert db.session is not None
        assert db.session.is_active
