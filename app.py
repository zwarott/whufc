import os

from __init__ import create_app
from src.general.models import Country, Competition, Position, Place, Result
from src.season_22_23.models import (
    Player,
    Match,
    Goal,
    Assist,
    YellowCard,
    RedCard,
    Team,
    player_match,
)


# App Initialization
# os.getenv() method in Python returns the value of the environment variable
# key if it exists otherwise returns the default value
app = create_app(os.getenv("CONFIG_MODE"))


if __name__ == "__main__":
    app.run()
