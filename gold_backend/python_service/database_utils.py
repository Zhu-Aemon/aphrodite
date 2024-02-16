import sqlite3


def get_table_names(database_path):
    # Connect to the SQLite database
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    # Query to retrieve the names of all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

    # Fetch all table names
    table_names = cursor.fetchall()

    # Close the connection
    conn.close()

    # Extract table names from the result
    table_names = [name[0] for name in table_names]

    return table_names