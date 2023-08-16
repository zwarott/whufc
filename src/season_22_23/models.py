from __init__ import db


player_match = db.Table(
    "player_match",
    db.Column(
        "player_number",
        db.Integer,
        db.ForeignKey("season_22_23.player.id", ondelete="CASCADE"),
    ),
    db.Column(
        "match_id",
        db.Integer,
        db.ForeignKey("season_22_23.match.id", ondelete="CASCADE"),
    ),
    schema="season_22_23",
)


class Player(db.Model):
    __tablename__ = "player"
    __table_args__ = {"schema": "season_22_23"}

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    number = db.Column(db.Integer, nullable=False)
    first_name = db.Column(db.Text, nullable=True)
    last_name = db.Column(db.Text, nullable=False)
    born = db.Column(db.Date, nullable=False)
    country = db.Column(
        db.Text,
        db.ForeignKey("general.country.country", ondelete="CASCADE"),
        nullable=False,
    )
    position = db.Column(
        db.Text,
        db.ForeignKey("general.position.position", ondelete="CASCADE"),
        nullable=False,
    )
    created = db.Column(
        db.DateTime(timezone=False),
        server_default=db.func.current_timestamp(0),
    )
    updated = db.Column(
        db.DateTime(timezone=False),
        nullable=True,
        onupdate=db.func.current_timestamp(0),
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


class Match(db.Model):
    __tablename__ = "match"
    __table_args__ = {"schema": "season_22_23"}

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    game_date = db.Column(db.Date, unique=True, nullable=False)
    competition = db.Column(
        db.Text,
        db.ForeignKey("general.competition.competition", ondelete="CASCADE"),
        nullable=False,
    )
    opponent = db.Column(
        db.Text,
        db.ForeignKey("season_22_23.team.team", ondelete="CASCADE"),
        nullable=False,
    )
    place = db.Column(
        db.Text,
        db.ForeignKey("general.place.place", ondelete="CASCADE"),
        nullable=False,
    )
    result = db.Column(
        db.Text,
        db.ForeignKey("general.result.result", ondelete="CASCADE"),
        nullable=False,
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
    created = db.Column(
        db.DateTime(timezone=False),
        server_default=db.func.current_timestamp(0),
    )
    updated = db.Column(
        db.DateTime(timezone=False),
        nullable=True,
        onupdate=db.func.current_timestamp(0),
    )

    def __repr__(self) -> str:
        return f"Match: {self.id}: West Ham United FC: {self.score_whu} | {self.opponent}: {self.score_opponent}"


class Goal(db.Model):
    __tablename__ = "goal"
    __table_args__ = {"schema": "season_22_23"}

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    created = db.Column(
        db.DateTime(timezone=False),
        server_default=db.func.current_timestamp(0),
    )
    updated = db.Column(
        db.DateTime(timezone=False),
        nullable=True,
        onupdate=db.func.current_timestamp(0),
    )
    id_match = db.Column(db.Integer, db.ForeignKey("season_22_23.match.id"))
    id_player = db.Column(db.Integer, db.ForeignKey("season_22_23.player.id"))


class Assist(db.Model):
    __tablename__ = "assist"
    __table_args__ = {"schema": "season_22_23"}

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    created = db.Column(
        db.DateTime(timezone=False),
        server_default=db.func.current_timestamp(0),
    )
    updated = db.Column(
        db.DateTime(timezone=False),
        nullable=True,
        onupdate=db.func.current_timestamp(0),
    )
    id_match = db.Column(db.Integer, db.ForeignKey("season_22_23.match.id"))
    id_player = db.Column(db.Integer, db.ForeignKey("season_22_23.player.id"))


class YellowCard(db.Model):
    __tablename__ = "yellow_card"
    __table_args__ = {"schema": "season_22_23"}

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    created = db.Column(
        db.DateTime(timezone=False),
        server_default=db.func.current_timestamp(0),
    )
    updated = db.Column(
        db.DateTime(timezone=False),
        nullable=True,
        onupdate=db.func.current_timestamp(0),
    )
    id_match = db.Column(db.Integer, db.ForeignKey("season_22_23.match.id"))
    id_player = db.Column(db.Integer, db.ForeignKey("season_22_23.player.id"))


class RedCard(db.Model):
    __tablename__ = "red_card"
    __table_args__ = {"schema": "season_22_23"}

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    created = db.Column(
        db.DateTime(timezone=False),
        server_default=db.func.current_timestamp(0),
    )
    updated = db.Column(
        db.DateTime(timezone=False),
        nullable=True,
        onupdate=db.func.current_timestamp(0),
    )
    id_match = db.Column(db.Integer, db.ForeignKey("season_22_23.match.id"))
    id_player = db.Column(db.Integer, db.ForeignKey("season_22_23.player.id"))


class Team(db.Model):
    __tablename__ = "team"
    __table_args__ = {"schema": "season_22_23"}

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    team = db.Column(db.Text, unique=True, nullable=False)
    created = db.Column(
        db.DateTime(timezone=False),
        server_default=db.func.current_timestamp(0),
    )
    updated = db.Column(
        db.DateTime(timezone=False),
        nullable=True,
        onupdate=db.func.current_timestamp(0),
    )

    def __repr__(self) -> str:
        return f"Club: {self.team}"
