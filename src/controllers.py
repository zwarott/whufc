from time import time
from csv import DictReader
import os

import psycopg2 as ps
import pandas as pd
from sqlalchemy import update, create_engine, inspect
from flask_sqlalchemy import DefaultMeta

from __init__ import db


def insert_csv(csv_path: str, db_table: str, columns: list) -> None:
    """Import or append data from csv file into a db table.

    Import data from csv file into an empty table in PostgreSQL database
    using psycopg2 module or append data into a database table with
    existing records. Keep in mind, that names of csv file and db table
    have to be same (for pairing).

    Parameters
    ----------
    csv_path : str
        A string representing path to csv file.
    db_table : str
        Name of table within PostgreSQL database.
    columns : list
        List of columns' names whose recors will
        be inserted.

    Usage Example
    -------------
    >>> insert_csv(
                "./test/pos.csv",
                "general.position",
                ["id", "position"])
    Data were succesfully inserted into the table 'general.position'!
    """
    # Start time of importing process.
    start_time = time()
    # Connect to PostgreSQL database.
    conn = ps.connect("dbname=whufc user=postgres")
    # Open a cursor to perform database operations.
    cur = conn.cursor()
    # Create string with columns' names prepared for inserting into
    # the PostgreSQL database table.
    column_names = ",".join(columns)
    with open(csv_path, "r", encoding="UTF-8") as f:
        # Copy data from selected csv file into specific 'schema.table'.
        cur.copy_expert(
            f"COPY {db_table} ({column_names}) FROM STDIN WITH (FORMAT CSV, HEADER)", f
        )
        # Commit changes to the database table.
        conn.commit()
        # Close communication with the database.
        cur.close()
        # Close connection with the database.
        conn.close()
        # Record time of importing process.
        duration = time() - start_time
        # Print data import status with importing time.
        print(
            f"Data were succesfully imported into the table '{db_table}'.",
            f"Importing time: {duration:.2f} s.",
            sep="\n",
        )


def insert_csv_schema(csv_dir_path: str, schema_name: str) -> None:
    """Import or append data from csv files into the db tables.

    Import and append data from csv files into the tables in PostgreSQL
    database using psycopg2 module. Keep in mind that names of db tables and
    csv file have to be the same (for pairing), need to have id values
    filled as well.

    Parameters
    ----------
    csv_dir_path : str
        A string representing path to directory containing csv files.
    schema_table : str
        Name of schema within PostgreSQL database.
    commit_changes : bool
        If you do not want commit changes, put False,
        default value is True.

        Usage Example
    -------------
    >>> csv_to_table("./src/general/data/", "general")
    """
    # Start time of importing process.
    start_time = time()
    # Connect to PostgreSQL database.
    conn = ps.connect("dbname=whufc user=postgres")
    # Open a cursor to perform database operations.
    cur = conn.cursor()
    # Connect into the database.
    engine = create_engine(
        "postgresql+psycopg2://postgres@localhost:5432/whufc", echo=False
    )
    # Inspect the database.
    inspector = inspect(engine)
    # Create list of tables in certain schema.
    tables = sorted(
        [
            schema_name + "." + table_name
            for table_name in inspector.get_table_names(schema=schema_name)
        ]
    )
    # Create list of all csvs' paths within imported directory path.
    csv_files = sorted(
        [csv_dir_path + csv_path for csv_path in os.listdir(csv_dir_path)]
    )
    # For loop for updating each db table by data from csvs above.
    for csv_file in csv_files:
        with open(csv_file, "r", encoding="UTF-8") as f:
            # Index of each csv file in list for pairing with the index
            # of table in 'tables' list.
            pos = csv_files.index(csv_file)
            csv_reader = DictReader(f)
            dict_from_csv = dict(list(csv_reader)[0])
            columns = list(dict_from_csv.keys())
            column_names = ",".join(columns)
            # Copy data from selected csv file into specific schema.table.
            cur.copy_expert(
                f"COPY {tables[pos]} ({column_names}) FROM STDIN WITH (FORMAT CSV, HEADER)",
                f,
            )
            # Commit changes to the database table.
            conn.commit()
            # Print data import status with import time.
            print(
                f"Data were succesfully imported into the table '{tables[pos]}'.",
            )
    # Close communication with the database.
    cur.close()
    # Close connection with the database.
    conn.close()
    # Record time of importing process.
    duration = time() - start_time
    # Print data import status.
    print(f"Importing time: {duration:.2f} s.")


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
    >>> update_col("./src/general/data/positions.csv", Position, "position", "id_position")
    """
    # Start time of updating process.
    start_time = time()
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = DictReader(f)
        # Create list of dictionaries.
        # to_update[n][pk_col] -> pk_col value
        # to_update[n][col] -> col value
        to_update = [{pk_col: d[pk_col], col: d[col]} for d in reader]

    # Update existing values in the database.
    db.session.execute(update(obj), to_update)
    # Record time of updating process.
    duration = time() - start_time
    # Commit changes to the database.
    db.session.commit()
    # Print column updating status with updating time.
    print(
        f"Column '{col}' in the table '{obj.__tablename__}' was succesfully updated.",
        f"Importing time: {duration:.2f} s",
        sep="\n",
    )


def update_cols(csv_path: str, obj: DefaultMeta, cols: list) -> None:
    """Update selected columns from csv file.

    Update data in selected columns within specific table
    in PostgreSQL database.

    Parameters
    ----------
    csv_path : str
        A string representing path to csv file.
    obj : DefaultMeta
        Class representing table in PostgreSQL database.
    cols: list
        List of selected columns to update. Make sure that
        column with primary key is included.

    Usage Example
    -------------
    >>> update_cols("./src/season_22_23/data/players.csv", Player, ["number", "last_name"])
    """
    # Start time of updating process.
    start_time = time()
    # Create dataframe with selected columns.
    df = pd.read_csv(csv_path, usecols=cols)
    # Create list of dictionaries.
    to_update = df.to_dict("records")

    # Update existing values to the database.
    db.session.execute(update(obj), to_update)
    # Record time of updating process.
    duration = time() - start_time
    # Commit changes to the database.
    db.session.commit()
    # Print column updating status with updating time.
    for col in cols:
        print(
            f"Column '{col}' in the table '{obj.__tablename__}' was succesfully updated.",
            sep="\n",
        )
    print(f"Importing time: {duration:.2f} s")


def del_recs(schema_name: str) -> None:
    """Delete all records from all tables within certain schema.

    Delete all records from all tables within certain schema in
    PostgreSQL database.

    Parameters
    ----------
    schema_name : str
        A string representing existing schema name in PostgreSQL
        database.

    Usage Example
    -------------
    >>> del_recs("general")
    """
    start_time = time()
    # Connect to PostgreSQL database.
    conn = ps.connect("dbname=whufc user=postgres")
    # Open a cursor to perform database operations.
    cur = conn.cursor()
    # Connect into the database.
    engine = create_engine(
        "postgresql+psycopg2://postgres@localhost:5432/whufc", echo=False
    )
    # Inspect the database.
    inspector = inspect(engine)
    # Create list of tables in certain schema.
    tables = [
        schema_name + "." + table_name
        for table_name in inspector.get_table_names(schema=schema_name)
    ]
    for table in tables:
        cur.execute(f"DELETE FROM {table}")
        conn.commit()
        print(f"Data from '{table}' were succesfully deleted.")

    cur.close()
    conn.close()
    duration = time() - start_time
    print(f"Importing time: {duration:.2f} s.")
