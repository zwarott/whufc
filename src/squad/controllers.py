from time import time
from csv import DictReader

import psycopg2 as ps
from pandas import read_csv
from sqlalchemy import select
from flask_sqlalchemy import DefaultMeta
from sqlalchemy.orm.attributes import InstrumentedAttribute

from __init__ import db


# TO-DO: Check type hinting.
# TO-DO: Write useful comments.
# TO-DO: Test functionality of this user function.
def csv_to_table(
    csv_path: str, db_table: str, commit_changes: bool = True
) -> DefaultMeta:
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
        default value = True.

    Usage Example
    -------------
    >>> csv_to_table("./src/squad/data/countries.csv", "squad.country", commit_changes = False)
    """
    start_time = time()
    # Connect to PostgreSQL database.
    conn = ps.connect("dbname=whufc user=postgres")
    # Open a cursor to perform database operations.
    cur = conn.cursor()
    with open(csv_path, "r", encoding="UTF-8") as f:
        # Copy data from selected csv file into specific schema.table.
        cur.copy_expert("COPY squad.country FROM STDIN WITH (FORMAT CSV, HEADER)", f)
        # If commit_changes = True, change will be commited into the database.
        if commit_changes:
            conn.commit()
            duration = time() - start_time
            return (
                # Close communication with the database.
                cur.close(),
                conn.close(),
                # Print data import status with import time.
                print(
                    f"Data were succesfully imported into table '{db_table}'. Importing time: {duration:.2f} s."
                ),
            )
        # If commit_changes = False, changes will not be commited.
        else:
            return (
                # Close communication with the database.
                cur.close(),
                conn.close(),
                # print data import status.
                print(f"Data were not imported into table '{db_table}'"),
            )


# TO-DO: Check type hinting.
# TO-DO: Create function docstring.
# TO-DO: Write useful comments.
# TO-DO: Test functionality of this user function.
def update_col_data_pd(file_path: str, mapped_object: DefaultMeta) -> None:
    start_time = time()
    data = read_csv(file_path)
    id_match = data["id_match"].tolist()

    for y in db.session.scalars(
        select(mapped_object).order_by(mapped_object.id.asc())
    ).all():
        y.id_match = id_match[y.id - 1]  # Comment, why is there -1!
    duration = time() - start_time
    print(f"Time: {duration:.4f} s")


# TO-DO: Check type hinting.
# TO-DO: Create function docstring.
# TO-DO: Write useful comments.
# TO-DO: Test functionality of this user function.
def update_col_data_csv(
    file_path: str, mapped_object: DefaultMeta, mapped_column: InstrumentedAttribute
) -> None:
    start_time = time()
    with open(file_path, "r", encoding="utf-8") as f:
        reader = DictReader(f)
        try:
            updated_column = [row[mapped_column] for row in reader]
            if mapped_column in mapped_object.__table__.columns.keys():
                for y in db.session.scalars(
                    select(mapped_object).order_by(mapped_object.id.asc())
                ).all():
                    y.mapped_column = updated_column[
                        y.mapped_column - 1
                    ]  # Comment, why is there -1!
            duration = time() - start_time
            print("Data were successfully imported!")
            print(f"Importing time: {duration:.4f} s.")

        except KeyError:
            print(f"Column '{mapped_column}' does not exist!")
