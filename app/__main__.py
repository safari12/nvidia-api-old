import os

from app import create_app


def main():
    config_name = os.getenv('FLASK_CONFIG', 'development')
    app = create_app(config_name)
    app.run()


if __name__ == '__main__':
    main()
