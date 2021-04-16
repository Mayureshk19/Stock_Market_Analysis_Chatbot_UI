""" Configurations """


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True


class ProductionConfig(Config):
    ENV = "production"
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    ENV = "development"
    DEVELOPMENT = True
    DEBUG = True
    TESTING = False
    CSRF_ENABLED = True
