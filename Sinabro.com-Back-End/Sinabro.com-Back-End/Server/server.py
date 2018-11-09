import os

from app import create_app

from config.dev import DevConfig

if __name__ == '__main__':
    app = create_app(DevConfig)

    if 'SECRET_KEY' not in os.environ:
        print("SECRET_KEY is not existing")

    app.run(**app.config['RUN_SETTING'])
