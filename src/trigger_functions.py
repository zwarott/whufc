create_trigger_functions = """
-- Create trigger function for filling 'updated' column.
CREATE FUNCTION public.updated_tf()
RETURNS trigger AS
$$
BEGIN
NEW.updated = current_timestamp(0);
RETURN NEW;
END;
$$
LANGUAGE plpgsql;
"""

drop_trigger_functions = """
DROP FUNCTION IF EXISTS public.updated_tf;
"""
