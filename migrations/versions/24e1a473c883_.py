"""empty message

Revision ID: 24e1a473c883
Revises:
Create Date: 2023-08-08 10:11:14.546541

"""

from alembic import op
import sqlalchemy as sa

from src.trigger_functions import create_trigger_functions, drop_trigger_functions
from src.triggers import create_triggers, drop_triggers


# revision identifiers, used by Alembic.
revision = "24e1a473c883"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("create schema general")
    op.execute("create schema season_22_23")

    op.create_table(
        "competition",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("competition", sa.Text(), nullable=False),
        sa.Column(
            "created",
            sa.TIMESTAMP(timezone=False),
            server_default=sa.func.current_timestamp(0),
            nullable=False,
        ),
        sa.Column(
            "updated",
            sa.TIMESTAMP(timezone=False),
            onupdate=sa.func.current_timestamp(0),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_competition")),
        sa.UniqueConstraint("competition", name=op.f("uq_competition_competition")),
        sa.UniqueConstraint("id", name=op.f("uq_competition_id")),
        schema="general",
    )
    op.create_table(
        "country",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("country", sa.Text(), nullable=False),
        sa.Column(
            "created",
            sa.TIMESTAMP(timezone=False),
            server_default=sa.func.current_timestamp(0),
            nullable=False,
        ),
        sa.Column(
            "updated",
            sa.TIMESTAMP(timezone=False),
            onupdate=sa.func.current_timestamp(0),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_country")),
        sa.UniqueConstraint("country", name=op.f("uq_country_country")),
        sa.UniqueConstraint("id", name=op.f("uq_country_id")),
        schema="general",
    )
    op.create_table(
        "place",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("place", sa.Text(), nullable=False),
        sa.Column(
            "created",
            sa.TIMESTAMP(timezone=False),
            server_default=sa.func.current_timestamp(0),
            nullable=False,
        ),
        sa.Column(
            "updated",
            sa.TIMESTAMP(timezone=False),
            onupdate=sa.func.current_timestamp(0),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_place")),
        sa.UniqueConstraint("id", name=op.f("uq_place_id")),
        sa.UniqueConstraint("place", name=op.f("uq_place_place")),
        schema="general",
    )
    op.create_table(
        "position",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("position", sa.Text(), nullable=False),
        sa.Column(
            "created",
            sa.TIMESTAMP(timezone=False),
            server_default=sa.func.current_timestamp(0),
            nullable=False,
        ),
        sa.Column(
            "updated",
            sa.TIMESTAMP(timezone=False),
            onupdate=sa.func.current_timestamp(0),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_position")),
        sa.UniqueConstraint("id", name=op.f("uq_position_id")),
        sa.UniqueConstraint("position", name=op.f("uq_position_position")),
        schema="general",
    )
    op.create_table(
        "result",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("result", sa.Text(), nullable=False),
        sa.Column(
            "created",
            sa.TIMESTAMP(timezone=False),
            server_default=sa.func.current_timestamp(0),
            nullable=False,
        ),
        sa.Column(
            "updated",
            sa.TIMESTAMP(timezone=False),
            onupdate=sa.func.current_timestamp(0),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_result")),
        sa.UniqueConstraint("id", name=op.f("uq_result_id")),
        sa.UniqueConstraint("result", name=op.f("uq_result_result")),
        schema="general",
    )
    op.create_table(
        "team",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("team", sa.Text(), nullable=False),
        sa.Column(
            "created",
            sa.TIMESTAMP(timezone=False),
            server_default=sa.func.current_timestamp(0),
            nullable=False,
        ),
        sa.Column(
            "updated",
            sa.TIMESTAMP(timezone=False),
            onupdate=sa.func.current_timestamp(0),
            nullable=True,
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_team")),
        sa.UniqueConstraint("id", name=op.f("uq_team_id")),
        sa.UniqueConstraint("team", name=op.f("uq_team_team")),
        schema="season_22_23",
    )
    op.create_table(
        "match",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("game_date", sa.Date(), nullable=False),
        sa.Column("competition", sa.Text(), nullable=False),
        sa.Column("opponent", sa.Text(), nullable=False),
        sa.Column("place", sa.Text(), nullable=False),
        sa.Column("result", sa.Text(), nullable=False),
        sa.Column("score_whu", sa.Integer(), nullable=False),
        sa.Column("score_opponent", sa.Integer(), nullable=False),
        sa.Column(
            "created",
            sa.TIMESTAMP(timezone=False),
            server_default=sa.func.current_timestamp(0),
            nullable=False,
        ),
        sa.Column(
            "updated",
            sa.TIMESTAMP(timezone=False),
            onupdate=sa.func.current_timestamp(0),
            nullable=True,
        ),
        sa.ForeignKeyConstraint(
            ["competition"],
            ["general.competition.competition"],
            name=op.f("fk_match_competition_competition"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["opponent"],
            ["season_22_23.team.team"],
            name=op.f("fk_match_opponent_team"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["place"],
            ["general.place.place"],
            name=op.f("fk_match_place_place"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["result"],
            ["general.result.result"],
            name=op.f("fk_match_result_result"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_match")),
        sa.UniqueConstraint("game_date", name=op.f("uq_match_game_date")),
        sa.UniqueConstraint("id", name=op.f("uq_match_id")),
        schema="season_22_23",
    )
    op.create_table(
        "player",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("number", sa.Integer(), nullable=False),
        sa.Column("first_name", sa.Text(), nullable=True),
        sa.Column("last_name", sa.Text(), nullable=False),
        sa.Column("born", sa.Date(), nullable=False),
        sa.Column("country", sa.Text(), nullable=False),
        sa.Column("position", sa.Text(), nullable=False),
        sa.Column(
            "created",
            sa.TIMESTAMP(timezone=False),
            server_default=sa.func.current_timestamp(0),
            nullable=False,
        ),
        sa.Column(
            "updated",
            sa.TIMESTAMP(timezone=False),
            onupdate=sa.func.current_timestamp(0),
            nullable=True,
        ),
        sa.ForeignKeyConstraint(
            ["country"],
            ["general.country.country"],
            name=op.f("fk_player_country_country"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["position"],
            ["general.position.position"],
            name=op.f("fk_player_position_position"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_player")),
        sa.UniqueConstraint("id", name=op.f("uq_player_id")),
        schema="season_22_23",
    )
    op.create_table(
        "assist",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "created",
            sa.TIMESTAMP(timezone=False),
            server_default=sa.func.current_timestamp(0),
            nullable=False,
        ),
        sa.Column(
            "updated",
            sa.TIMESTAMP(timezone=False),
            onupdate=sa.func.current_timestamp(0),
            nullable=True,
        ),
        sa.Column("id_match", sa.Integer(), nullable=True),
        sa.Column("id_player", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["id_match"],
            ["season_22_23.match.id"],
            name=op.f("fk_assist_id_match_match"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["id_player"],
            ["season_22_23.player.id"],
            name=op.f("fk_assist_id_player_player"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_assist")),
        sa.UniqueConstraint("id", name=op.f("uq_assist_id")),
        schema="season_22_23",
    )
    op.create_table(
        "goal",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "created",
            sa.TIMESTAMP(timezone=False),
            server_default=sa.func.current_timestamp(0),
            nullable=False,
        ),
        sa.Column(
            "updated",
            sa.TIMESTAMP(timezone=False),
            onupdate=sa.func.current_timestamp(0),
            nullable=True,
        ),
        sa.Column("id_match", sa.Integer(), nullable=True),
        sa.Column("id_player", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["id_match"],
            ["season_22_23.match.id"],
            name=op.f("fk_goal_id_match_match"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["id_player"],
            ["season_22_23.player.id"],
            name=op.f("fk_goal_id_player_player"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_goal")),
        sa.UniqueConstraint("id", name=op.f("uq_goal_id")),
        schema="season_22_23",
    )
    op.create_table(
        "player_match",
        sa.Column("player_number", sa.Integer(), nullable=True),
        sa.Column("match_id", sa.Integer(), nullable=True),
        sa.Column(
            "created",
            sa.TIMESTAMP(timezone=False),
            server_default=sa.func.current_timestamp(0),
            nullable=False,
        ),
        sa.Column(
            "updated",
            sa.TIMESTAMP(timezone=False),
            onupdate=sa.func.current_timestamp(0),
            nullable=True,
        ),
        sa.ForeignKeyConstraint(
            ["match_id"],
            ["season_22_23.match.id"],
            name=op.f("fk_player_match_match_id_match"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["player_number"],
            ["season_22_23.player.id"],
            name=op.f("fk_player_match_player_number_player"),
            ondelete="CASCADE",
        ),
        schema="season_22_23",
    )
    op.create_table(
        "red_card",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "created",
            sa.TIMESTAMP(timezone=False),
            server_default=sa.func.current_timestamp(0),
            nullable=False,
        ),
        sa.Column(
            "updated",
            sa.TIMESTAMP(timezone=False),
            onupdate=sa.func.current_timestamp(0),
            nullable=True,
        ),
        sa.Column("id_match", sa.Integer(), nullable=True),
        sa.Column("id_player", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["id_match"],
            ["season_22_23.match.id"],
            name=op.f("fk_red_card_id_match_match"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["id_player"],
            ["season_22_23.player.id"],
            name=op.f("fk_red_card_id_player_player"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_red_card")),
        sa.UniqueConstraint("id", name=op.f("uq_red_card_id")),
        schema="season_22_23",
    )
    op.create_table(
        "yellow_card",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "created",
            sa.TIMESTAMP(timezone=False),
            server_default=sa.func.current_timestamp(0),
            nullable=False,
        ),
        sa.Column(
            "updated",
            sa.TIMESTAMP(timezone=False),
            onupdate=sa.func.current_timestamp(0),
            nullable=True,
        ),
        sa.Column("id_match", sa.Integer(), nullable=True),
        sa.Column("id_player", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["id_match"],
            ["season_22_23.match.id"],
            name=op.f("fk_yellow_card_id_match_match"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["id_player"],
            ["season_22_23.player.id"],
            name=op.f("fk_yellow_card_id_player_player"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_yellow_card")),
        sa.UniqueConstraint("id", name=op.f("uq_yellow_card_id")),
        schema="season_22_23",
    )

    op.execute(create_trigger_functions)
    op.execute(create_triggers)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("yellow_card", schema="season_22_23")
    op.drop_table("red_card", schema="season_22_23")
    op.drop_table("player_match", schema="season_22_23")
    op.drop_table("goal", schema="season_22_23")
    op.drop_table("assist", schema="season_22_23")
    op.drop_table("player", schema="season_22_23")
    op.drop_table("match", schema="season_22_23")
    op.drop_table("team", schema="season_22_23")
    op.drop_table("result", schema="general")
    op.drop_table("position", schema="general")
    op.drop_table("place", schema="general")
    op.drop_table("country", schema="general")
    op.drop_table("competition", schema="general")

    op.execute("drop schema general cascade")
    op.execute("drop schema season_22_23 cascade")
    op.execute(drop_trigger_functions)
    op.execute(drop_triggers)
    # ### end Alembic commands ###
