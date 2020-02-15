from logging.config import dictConfig
from .logging import logger_dict

# load logging configuration
dictConfig(logger_dict)


class Config(object):
    """Base config, uses staging database server."""
    DEBUG = False
    TESTING = False
    JSONIFY_MIMETYPE = 'application/json'
    # TEMPLATES_AUTO_RELOAD = None
    # MAX_COOKIE_SIZE = 10485760
    # MAX_CONTENT_LENGTH=None
    DB_SERVER = '192.168.1.56'

    @property
    def DATABASE_URI(self):  # Note: all caps
        return 'mysql://user@{}/foo'.format(self.DB_SERVER)


class ProductionConfig(Config):
    """Uses production database server."""
    ENV = 'prod'
    DB_SERVER = '192.168.19.32'
    SECRET_KEY = b'\xfd\xdec\xf4+\r\xef\x81#Qe\xc2\xad5\x89\xa2'


class DevelopmentConfig(Config):
    ENV = 'dev'
    DEBUG = True
    DB_SERVER = 'localhost'


class TestingConfig(Config):
    ENV = 'test'
    TESTING = True
    DB_SERVER = 'localhost'
    DATABASE_URI = 'sqlite:///:memory:'
