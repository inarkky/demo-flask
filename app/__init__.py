"""Initialize Flask app."""
from flask import Flask


def create_app():
    """Construct core Flask app."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():

        return app