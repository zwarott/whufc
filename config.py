import os


# The base configuration class (object).
# Turn off the Flask-SQLAlchemy event system and warning.
class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    # Enable debug mode, that will refresh the page when you make changes.
    DEBUG = True
    # Import database URL from .env file (environment configuration -> this file allows you tu put your environment variables inside a file).
    SQLALCHEMY_DATABASE_URI = os.getenv("DEVELOPMENT_DATABASE_URL")


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv("TEST_DATABASE_URL")


class StagingConfig(Config):
    DEVELOPMENT = True
    # Enable debug mode, that will refresh the page when you make changes.
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("STAGING_DATABASE_URL")


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv("PRODUCTION_DATABASE_URL")


# Dictonary with keys that refer to each configuration modes -> objects.
# Key: variable included within CONFIG_MODE | value: object with specific configuration.
config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "production": ProductionConfig,
}
