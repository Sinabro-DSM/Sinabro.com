import os
from datetime import timedelta


class Config:
    SERVICE_NAME = "Sinabrodotcom"
    SERVICE_NAME_UPPER = SERVICE_NAME.upper()
    SECRET_KEY = os.getenv('SECRET_KEY', 'qwerdagkjliouqrwe')

    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
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
    SWAGGER = {
        'title': SERVICE_NAME,
        'specs_route': '/docs',
        'uiversion': 3,

        'info': {
            'title': SERVICE_NAME + ' API',
            'version': '1.0',
            'description': ''
        },
        'basePath': '/docs'
    }

    SWAGGER_TEMPLATE = {
        'schemes': [
            'http'
        ],
        'tags': [
            {
                'name': '계정',
                'description': '계정관리 api'
            },
            {
                'name': '게시글',
                'description': '게시글 관련 api'
            },
            {
                'name': '답글',
                'description': '답글 관련 api'
            }
        ]
    }
