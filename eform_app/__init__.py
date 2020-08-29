"""Initialize app."""
from flask import Flask
from flask_wtf.csrf import CSRFProtect

def create_app():
    """Construct the core flask_wtforms_tutorial."""
    app = Flask(__name__, instance_relative_config=False)
    CSRFProtect(app)
    app.config.from_object('config.Config')

    with app.app_context():
        # Import parts of our flask_wtforms_tutorial
        from . import routes

        return app
