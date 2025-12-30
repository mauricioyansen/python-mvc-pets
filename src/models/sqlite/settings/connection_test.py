from sqlalchemy.engine import Engine
from .connection import db_connection_handler


def test_connect_to_db():
    assert db_connection_handler.get_engine() is None
    db_connection_handler.connect_to_db()
    engine = db_connection_handler.get_engine()
    assert engine is not None
    assert isinstance(engine, Engine)
    assert str(engine.url) == "sqlite:///storage.db"
