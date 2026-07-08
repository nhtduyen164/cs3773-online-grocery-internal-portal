from pathlib import Path

from flask import Flask


def create_app():
    project_root = Path(__file__).resolve().parents[2]
    instance_path = project_root / "instance"

    app = Flask(
        __name__,
        instance_relative_config=True,
        instance_path=str(instance_path)
    )

    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=str(instance_path / "grocery.sqlite"),
    )

    instance_path.mkdir(exist_ok=True)

    from grocery_portal import db
    db.init_app(app)

    from grocery_portal.main.routes import main_bp
    app.register_blueprint(main_bp)

    return app
