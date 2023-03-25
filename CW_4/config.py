class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False
    RESTX_JSON = {'ensure_ascii': False, 'indent': 2}

    ITEMS_PER_PAGE = 12


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
