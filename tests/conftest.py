from pathlib import Path

import pytest

from grocery_portal import create_app
from grocery_portal.db import get_db


@pytest.fixture()
def app(tmp_path):
    """
    Create a Flask application connected to a temporary test database.

    tmp_path is supplied by pytest and is unique for each test run.
    """

    test_database = tmp_path / "test_grocery.sqlite"

    app = create_app()

    app.config.update(
        TESTING=True,
        SECRET_KEY="test-secret-key",
        DATABASE=str(test_database),
    )

    schema_path = (
        Path(__file__).resolve().parents[1]
        / "database"
        / "schema.sql"
    )

    with app.app_context():
        db = get_db()

        with schema_path.open("r", encoding="utf-8") as schema_file:
            db.executescript(schema_file.read())

        db.commit()

    yield app


@pytest.fixture()
def client(app):
    """
    Return Flask's test client for sending simulated HTTP requests.
    """

    return app.test_client()


@pytest.fixture()
def authenticated_client(client):
    """
    Return a test client with a simulated authenticated session.

    B031 is testing order execution, not the login process, so directly
    setting the session keeps these tests focused on order behavior.
    """

    with client.session_transaction() as session:
        session["user_id"] = 1
        session["username"] = "test_manager"
        session["role"] = "manager"

    return client
