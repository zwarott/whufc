from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from flask_migrate import Migrate

# Import config variable from config.py -> dictonary with keys that refer to configuration modes.
from config import config

# Set up constraints' naming convention.
convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

# Integrates SQLAlchemy with FLask -> create the extension.
# This handles setting up one or more engines, associating tables and models with specific engines, and cleaning up connections and sessions after each request.
# Initialize constraints' naming covention.
db = SQLAlchemy(metadata=MetaData(naming_convention=convention))

# This module enables developers to quickly set up and starts the database schema migrations.
# Migrations allow you to change your database schema, such as adding or removing tables, columns, or constraints, while preserving existing data.
# Without proper migration management, it can become challenging to maintain consistency between the application code and the database schema.
migrate = Migrate()


# Function known as an application factory.
# Anything, that the purspose is to create something using any cofiguration that you want and return that thing.
# Any configuration, registration, and other setup the application needs will happen inside the function, then the application will be returned.
# config_mode refers to CONFIG_MODE constant from .env file
def create_app(config_mode):
    # A Flask Application is an instance of the Flask class -> everything about the app (such as configuration and URL's) will registered with this class.
    # app by convention, Flask class with special variable essentially refers to the name of the current file.
    # We create Flask instance inside the application factory.
    # This is a line of code that says, Flask, turn the current file into an web application, that listen for web browsers' requests.
    app = Flask(__name__)

    # We get the value from the environment variable that we need to set as configuration (development) -> asking for config file.
    # We load the object that we want to set as our configuration -> inside the config file we want the object called DevelopmentConfig.
    # After entering value of CONFIG_MODE from .env file, that imports configuration of particular object.
    app.config.from_object(config[config_mode])

    # Initialize the SQLAlchemy extension class with the application by calling db.init_app(app).
    db.init_app(app)

    migrate.init_app(app, db)

    return app
