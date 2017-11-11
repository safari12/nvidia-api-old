from flask import Flask

from config import app_config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    from .hello import hello as hello_blueprint
    app.register_blueprint(hello_blueprint, url_prefix='/hello')

    return app
