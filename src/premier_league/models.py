from datetime import datetime

from __init__ import db


player_match = db.Table(
    "player_match",
    db.Column(
        "player_number",
        db.Integer,
        db.ForeignKey("player.number", ondelete="CASCADE"),
    ),
    db.Column("match_id", db.Integer, db.ForeignKey("match.id", ondelete="CASCADE")),
)


class Match(db.Model):
    __tablename__ = "match"
    __table_args__ = {"schema": "premier_league"}

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    game_date = db.Column(db.Date, unique=True, nullable=False)
    opponent = db.Column(
        db.Text, db.ForeignKey("team.team", ondelete="CASCADE"), nullable=False
    )
    place = db.Column(
        db.Text, db.ForeignKey("place.place", ondelete="CASCADE"), nullable=False
    )
    result = db.Column(
        db.Text, db.ForeignKey("result.result", ondelete="CASCADE"), nullable=False
    )
    score_whu = db.Column(db.Integer, nullable=False)
    score_opponent = db.Column(db.Integer, nullable=False)
    goals = db.relationship(
        "Goal", foreign_keys="Goal.id_match", backref="match_g", cascade="all, delete"
    )
    assists = db.relationship(
        "Assist",
        foreign_keys="Assist.id_match",
        backref="match_a",
        cascade="all, delete",
    )
    yellow_cards = db.relationship(
        "YellowCard",
        foreign_keys="YellowCard.id_match",
        backref="match_y",
        cascade="all, delete",
    )
    red_cards = db.relationship(
        "RedCard",
        foreign_keys="RedCard.id_match",
        backref="match_r",
        cascade="all, delete",
    )
    created = db.Column(db.DateTime(timezone=True), default=datetime.today())
    updated = db.Column(
        db.DateTime(timezone=True), nullable=True, onupdate=datetime.today()
    )

    def __repr__(self) -> str:
        return f"Match: {self.id}: West Ham United FC: {self.score_whu} | {self.opponent}: {self.score_opponent}"


class Goal(db.Model):
    __tablename__ = "goal"
    __table_args__ = {"schema": "premier_league"}

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    created = db.Column(db.DateTime(timezone=True), default=datetime.today())
    updated = db.Column(
        db.DateTime(timezone=True), nullable=True, onupdate=datetime.today()
    )
    id_match = db.Column(db.Integer, db.ForeignKey("match.id"))
    id_player = db.Column(db.Integer, db.ForeignKey("player.number"))


class Assist(db.Model):
    __tablename__ = "assist"
    __table_args__ = {"schema": "premier_league"}

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    created = db.Column(db.DateTime(timezone=True), default=datetime.today())
    updated = db.Column(
        db.DateTime(timezone=True), nullable=True, onupdate=datetime.today()
    )
    id_match = db.Column(db.Integer, db.ForeignKey("match.id"))
    id_player = db.Column(db.Integer, db.ForeignKey("player.number"))


class YellowCard(db.Model):
    __tablename__ = "yellow_card"
    __table_args__ = {"schema": "premier_league"}

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    created = db.Column(db.DateTime(timezone=True), default=datetime.today())
    updated = db.Column(
        db.DateTime(timezone=True), nullable=True, onupdate=datetime.today()
    )
    id_match = db.Column(db.Integer, db.ForeignKey("match.id"))
    id_player = db.Column(db.Integer, db.ForeignKey("player.number"))


class RedCard(db.Model):
    __tablename__ = "red_card"
    __table_args__ = {"schema": "premier_league"}

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    player = db.Column(db.Integer, db.ForeignKey("player.number"))
    created = db.Column(db.DateTime(timezone=True), default=datetime.today())
    updated = db.Column(
        db.DateTime(timezone=True), nullable=True, onupdate=datetime.today()
    )
    id_match = db.Column(db.Integer, db.ForeignKey("match.id"))
    id_player = db.Column(db.Integer, db.ForeignKey("player.number"))


class Team(db.Model):
    __tablename__ = "team"
    __table_args__ = {"schema": "premier_league"}

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    team = db.Column(db.Text, unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"Club: {self.team}"


class Place(db.Model):
    __tablename__ = "place"
    __table_args__ = {"schema": "premier_league"}

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    place = db.Column(db.Text, unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"Place: {self.place}"


class Result(db.Model):
    __tablename__ = "result"
    __table_args__ = {"schema": "premier_league"}

    id_result = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    result = db.Column(db.Text, unique=True, nullable=False)

    def __repr__(self) -> str:
        return f"Result: {self.result}"
