from flask import Flask

from config import app_config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.url_map.strict_slashes = False

    from .hello import hello as hello_blueprint
    app.register_blueprint(hello_blueprint, url_prefix='/hello')

    from .gpu import gpu as gpu_blueprint
    app.register_blueprint(gpu_blueprint, url_prefix='/gpu')

    return app
