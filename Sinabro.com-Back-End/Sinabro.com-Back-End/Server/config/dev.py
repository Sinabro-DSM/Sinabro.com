from config import Config


class DevConfig(Config):
    HOST = 'localhost'
    DEBUG = True
    PORT = 5050

    RUN_SETTING = dict(Config.RUN_SETTING, **{
        'host': HOST,
        'port': PORT,
        'debug': DEBUG
    })