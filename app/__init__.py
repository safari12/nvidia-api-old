import logging as log
import os
import sys

from flask import Flask

from config import app_config


def setup_logging():
    if os.environ.get('NVIDIA_API_DEBUG', False):
        log.basicConfig(level=log.DEBUG)
    else:
        log.basicConfig(
            level=log.INFO,
            stream=sys.stdout,
            format="%(levelname)s:%(name)s:%(funcName)s:%(message)s"
        )


def create_app(config_name):
    setup_logging()

    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.url_map.strict_slashes = False

    from .gpu import gpu as gpu_blueprint
    app.register_blueprint(gpu_blueprint, url_prefix='/gpu')

    return app
