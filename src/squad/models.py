from datetime import datetime

from src.premier_league.models import player_match
from __init__ import db


class Player(db.Model):
    __tablename__ = "player"
    __table_args__ = {"schema": "squad"}

    number = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    first_name = db.Column(db.Text, nullable=True)
    last_name = db.Column(db.Text, nullable=False)
    born = db.Column(db.Date, nullable=False)
    country = db.Column(
        db.Text, db.ForeignKey("country.country", ondelete="CASCADE"), nullable=False
    )
    position = db.Column(
        db.Text, db.ForeignKey("position.position", ondelete="CASCADE"), nullable=False
    )
    created = db.Column(db.DateTime(timezone=True), default=datetime.today())
    updated = db.Column(
        db.DateTime(timezone=True), nullable=True, onupdate=datetime.today()
    )
    goals = db.relationship(
        "Goal", foreign_keys="Goal.id_player", backref="player_g", cascade="all, delete"
    )
    assists = db.relationship(
        "Assist",
        foreign_keys="Assist.id_player",
        backref="player_a",
        cascade="all, delete",
    )
    yellow_cards = db.relationship(
        "YellowCard",
        foreign_keys="YellowCard.id_player",
        backref="player_y",
        cascade="all, delete",
    )
    red_cards = db.relationship(
        "RedCard",
        foreign_keys="RedCard.id_player",
        backref="player_r",
        cascade="all, delete",
    )
    matches_started = db.relationship(
        "Match", secondary=player_match, backref="started_lineup", cascade="all, delete"
    )

    def __repr__(self) -> str:
        return f"{self.number} {self.last_name}"


class Country(db.Model):
    __tablename__ = "country"
    __table_args__ = {"schema": "squad"}

    id_country = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    country = db.Column(db.Text, unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"Country: {self.country}"


class Position(db.Model):
    __tablename__ = "position"
    __table_args__ = {"schema": "squad"}

    id_position = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    position = db.Column(db.Text, unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"Position: {self.position}"
