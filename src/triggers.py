create_triggers = """
-- Tables in 'general' schema.
-- Create trigger for 'country' table.
CREATE TRIGGER country_trigger
BEFORE UPDATE ON general.country
FOR EACH ROW EXECUTE PROCEDURE public.updated_tf();

-- Create trigger for 'position' table.
CREATE TRIGGER position_trigger
BEFORE UPDATE ON general.position
FOR EACH ROW EXECUTE PROCEDURE public.updated_tf();

-- Create trigger for 'competition' table.
CREATE TRIGGER competition_trigger
BEFORE UPDATE ON general.competition
FOR EACH ROW EXECUTE PROCEDURE public.updated_tf();

-- Create trigger for 'place' table.
CREATE TRIGGER place_trigger
BEFORE UPDATE ON general.place
FOR EACH ROW EXECUTE PROCEDURE public.updated_tf();

-- Create trigger for 'result' table.
CREATE TRIGGER result_trigger
BEFORE UPDATE ON general.result
FOR EACH ROW EXECUTE PROCEDURE public.updated_tf();


-- Tables in 'season_22_23' schema.
-- Create trigger for 'player_match' table.
CREATE TRIGGER player_match_trigger
BEFORE UPDATE ON season_22_23.player_match
FOR EACH ROW EXECUTE PROCEDURE public.updated_tf();

-- Create trigger for 'player' table.
CREATE TRIGGER player_trigger
BEFORE UPDATE ON season_22_23.player
FOR EACH ROW EXECUTE PROCEDURE public.updated_tf();

-- Create trigger for 'match' table.
CREATE TRIGGER match_trigger
BEFORE UPDATE ON season_22_23.match
FOR EACH ROW EXECUTE PROCEDURE public.updated_tf();

-- Create trigger for 'goal' table.
CREATE TRIGGER goal_trigger
BEFORE UPDATE ON season_22_23.goal
FOR EACH ROW EXECUTE PROCEDURE public.updated_tf();

-- Create trigger for 'assist' table.
CREATE TRIGGER assist_trigger
BEFORE UPDATE ON season_22_23.assist
FOR EACH ROW EXECUTE PROCEDURE public.updated_tf();

-- Create trigger for 'yellow_card' table.
CREATE TRIGGER yellow_card_trigger
BEFORE UPDATE ON season_22_23.yellow_card
FOR EACH ROW EXECUTE PROCEDURE public.updated_tf();

-- Create trigger for 'red_card' table.
CREATE TRIGGER red_card_trigger
BEFORE UPDATE ON season_22_23.red_card
FOR EACH ROW EXECUTE PROCEDURE public.updated_tf();

-- Create trigger for 'team' table.
CREATE TRIGGER team_trigger
BEFORE UPDATE ON season_22_23.team
FOR EACH ROW EXECUTE PROCEDURE public.updated_tf();
"""

drop_triggers = """
-- Drop triggers within tables in 'general' schema.
DROP TRIGGER IF EXISTS country_trigger ON general.position;
DROP TRIGGER IF EXISTS position_trigger ON general.position;
DROP TRIGGER IF EXISTS competition_trigger ON general.position;
DROP TRIGGER IF EXISTS place_trigger ON general.position;
DROP TRIGGER IF EXISTS result_trigger ON general.position;

-- Drop triggers within tables in 'season_22_23' schema.
DROP TRIGGER IF EXISTS player_match_trigger ON general.position;
DROP TRIGGER IF EXISTS player_trigger ON general.position;
DROP TRIGGER IF EXISTS match_trigger ON general.position;
DROP TRIGGER IF EXISTS goal_trigger ON general.position;
DROP TRIGGER IF EXISTS assist_trigger ON general.position;
DROP TRIGGER IF EXISTS yellow_card_trigger ON general.position;
DROP TRIGGER IF EXISTS red_card_trigger ON general.position;
DROP TRIGGER IF EXISTS team_trigger ON general.position;
"""
