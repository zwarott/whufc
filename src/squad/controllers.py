from time import time

import psycopg2 as ps
from csv import DictReader
from sqlalchemy import update
from flask_sqlalchemy import DefaultMeta

from __init__ import db


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
    >>> csv_to_table("./src/squad/data/positions.csv", "squad.position", commit_changes=False)
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
        # If commit_changes -> True, change will be commited into the database.
        if commit_changes:
            # Commit changes to the database table.
            conn.commit()
            duration = time() - start_time
            # Close communication with the database
            cur.close()
            conn.close()
            # Print data import status with import time.
            print(
                f"Data were succesfully imported into table '{db_table}'.",
                f"Importing time: {duration:.2f} s.",
                sep="\n",
            )
        # If commit_changes -> False, changes will not be commited.
        else:
            # Close communication with the database.
            cur.close()
            conn.close()
            # Print data import status.
            print(f"Data were not imported into table '{db_table}'!")


def update_col(csv_path: str, obj: DefaultMeta, col: str, pk_col: str) -> None:
    """Update column data from csv file.

    Update data in selected column within specific table
    in PostgreSQL database.

    Parameters
    ----------
    csv_path : str
        A string representing path to csv file.
    obj: DefaultMeta
        Class representing table in PostgreSQL database.
    col: str
        Name of column to update.
    pk_col: str
        Name of column with primary key for value pairing.

    Usage Example
    -------------
    >>> update_col("./src/squad/data/positions.csv", Position, "position", "id_position")
    """
    start_time = time()
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = DictReader(f)
        # Create list of dictionaries for updating.
        # to_update[n][pk_col] -> pk_col value
        # to_update[n][col] -> col value
        to_update = [{pk_col: d[pk_col], col: d[col]} for d in reader]

    # Update existing values to the database.
    db.session.execute(update(obj), to_update)
    duration = time() - start_time
    # Commit changes to the database.
    db.session.commit()
    return print(f"Importing time: {duration:.2f} s")
