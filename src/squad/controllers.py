from time import time

import psycopg2 as ps
from pandas import read_csv
from sqlalchemy import select
from flask_sqlalchemy import DefaultMeta
from sqlalchemy.orm.attributes import InstrumentedAttribute

from __init__ import db
from src.squad.models import Position


def csv_to_table(csv_path: str, db_table: str, commit_changes: bool = True) -> None:
    """Import data from csv file.

    Import data from csv file into PostgreSQL database using
    psycopg2 module.

    Parameters
    ----------
    csv_path : str
        A string representing path to csv file.
    db_table : str
        Name of table within PostgreSQL database.
    commit_changes : bool
        If you do not want commit changes, put False,
        default value --> True.

    Usage Example
    -------------
    >>> csv_to_table("./src/squad/data/positions.csv", "squad.position", commit_changes = False)
    Data were not imported into table 'squad.position'!
    """
    start_time = time()
    # Connect to PostgreSQL database.
    conn = ps.connect("dbname=whufc user=postgres")
    # Open a cursor to perform database operations.
    cur = conn.cursor()
    with open(csv_path, "r", encoding="UTF-8") as f:
        # Copy data from selected csv file into specific schema.table.
        cur.copy_expert(f"COPY {db_table} FROM STDIN WITH (FORMAT CSV, HEADER)", f)
        # If commit_changes --> True, change will be commited into the database.
        if commit_changes:
            # Commit changes to the database table.
            conn.commit()
            duration = time() - start_time
            # Close communication with the database
            cur.close()
            conn.close()
            # Print data import status with import time.
            print(
                f"Data were succesfully imported into table '{db_table}'. Importing time: {duration:.2f} s."
            )
        # If commit_changes --> False, changes will not be commited.
        else:
            # Close communication with the database.
            cur.close()
            conn.close()
            # Print data import status.
            print(f"Data were not imported into table '{db_table}'!")


# TO-DO: Check type hinting.
# TO-DO: Create function docstring.
# TO-DO: Write useful comments.
# TO-DO: Test functionality of this user function.
def update_col(
    csv_path: str, mapped_object: DefaultMeta, mapped_col: str
) -> DefaultMeta:
    """Update column data from csv file.

    Update data in selected column within specific table
    in PostgreSQL database.

    Parameters
    ----------
    csv_path : str
        A string representing path to csv file.
    mapped_object: DefaultMeta
        Class representing table in PostgreSQL database.
    mapped_col: InstrumentedAttribute
        Attribute representing column within table in
        PostgreSQL database.

    Usage Example
    -------------
    >>> update_col("./src/squad/data/positions.csv", Position, "position")
    """
    start_time = time()
    data = read_csv(csv_path)
    col = getattr(mapped_object, mapped_col)
    updating_col = data[mapped_col].tolist()

    # -1 is added due to correct indexing within list of values
    for record in db.session.scalars(
        select(mapped_object).order_by(mapped_object.col.asc())
    ).all():
        record.col = updating_col[record.col - 1]
    duration = time() - start_time
    return db.session.commit(), print(f"Time: {duration:.4f} s")
