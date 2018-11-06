import os
from datetime import timedelta


class Config:
    SERVICE_NAME = "Sinabrodotcom"
    SERVICE_NAME_UPPER = SERVICE_NAME.upper()
    SECRET_KEY = os.getenv('SECRET_KEY', 'qwerdagkjliouqrwe')

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=30)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=365)
    JWT_HEADER_TYPE = 'JWT'

    RUN_SETTING = {
        'threaded': True
    }

    MONGODB_SETTINGS = {
        'host': None,
        'port': None,
        'username': None,
        'db': SERVICE_NAME_UPPER,
        'password': os.getenv('MONGO_PW_SINABRODOTCOM')
    }