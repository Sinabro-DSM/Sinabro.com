from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flasgger import Swagger
from app.views import *
from mongoengine import connect

from config import Config


def create_app(*config_cls):
    """
    Creates Flask instance & initialize
    """
    print('[INFO] Flask application initialized with {}'.format([config.__name__ for config in config_cls]))

    app_ = Flask(__name__)

    for config in config_cls:
        app_.config.from_object(config)

    CORS().init_app(app_)
    JWTManager().init_app(app_)
    Router().init_app(app_)
    Swagger(template=app_.config['SWAGGER_TAMPLATE']).init_app(app_)

    connect(**app_.config['MONGODB_SETTINGS'])

    return app_
