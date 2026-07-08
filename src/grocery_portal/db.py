import sqlite3
from pathlib import Path

import click
from flask import current_app, g


def get_db():
    """
    Open a database connection for the current request if one does not
    already exist.
    """
    if "db" not in g:
        g.db = sqlite3.connect(current_app.config["DATABASE"])
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(error=None):
    """
    Close the database connection at the end of the request.
    """
    db = g.pop("db", None)

    if db is not None:
        db.close()


def init_db():
    """
    Initialize the SQLite database using schema.sql and seed_data.sql.
    """
    db = get_db()

    project_root = Path(__file__).resolve().parents[2]
    schema_path = project_root / "database" / "schema.sql"
    seed_data_path = project_root / "database" / "seed_data.sql"

    with open(schema_path, "r", encoding="utf-8") as schema_file:
        db.executescript(schema_file.read())

    if seed_data_path.exists():
        with open(seed_data_path, "r", encoding="utf-8") as seed_file:
            db.executescript(seed_file.read())

    db.commit()


@click.command("init-db")
def init_db_command():
    """
    Flask CLI command to initialize the database.
    """
    init_db()
    click.echo("Initialized the SQLite database.")


def init_app(app):
    """
    Register database functions with the Flask app.
    """
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
