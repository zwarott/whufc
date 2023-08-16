from __init__ import db


class Country(db.Model):
    __tablename__ = "country"
    __table_args__ = {"schema": "general"}

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    country = db.Column(db.Text, unique=True, nullable=False)
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
        return f"Country: {self.country}"


class Position(db.Model):
    __tablename__ = "position"
    __table_args__ = {"schema": "general"}

    id = db.Column(db.Integer, primary_key=True, unique=True)
    position = db.Column(db.Text, unique=True, nullable=False)
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
        return f"Position: {self.position}"


class Competition(db.Model):
    __tablename__ = "competition"
    __table_args__ = {"schema": "general"}

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    competition = db.Column(db.Text, unique=True, nullable=False)
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
        return f"Compettion: {self.competition}"


class Place(db.Model):
    __tablename__ = "place"
    __table_args__ = {"schema": "general"}

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    place = db.Column(db.Text, unique=True, nullable=False)
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
        return f"Place: {self.place}"


class Result(db.Model):
    __tablename__ = "result"
    __table_args__ = {"schema": "general"}

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    result = db.Column(db.Text, unique=True, nullable=False)
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
        return f"Result: {self.result}"
