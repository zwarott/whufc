import os

from __init__ import create_app

# App Initialization
# os.getenv() method in Python returns the value of the environment variable
# key if it exists otherwise returns the default value
app = create_app(os.getenv("CONFIG_MODE"))


if __name__ == "__main__":
    app.run()
