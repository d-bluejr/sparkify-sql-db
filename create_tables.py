import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    """Creates a fresh database for testing.

    Connects as the studentdb user who has DB drop and create priviledges, drops and then creates the sparkifydb database, and then reconnects as sparkify.

    """
    # connect to default database
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()

    # connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    return cur, conn


def drop_tables(cur, conn):
    """Drops the tables in the sparkify database.

    Runs the list of drop queries from the sql_queries script.

    Keyword arguments:
    cur -- the sparkify DB cursor
    conn -- the sparkify DB connection
    """

    # drop the tables using the sql_queries.py queries
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """Creates the tables in the sparkify database.

    Runs the list of create queries from the sql_queries script.

    Keyword arguments:
    cur -- the sparkify DB cursor
    conn -- the sparkify DB connection
    """

    # create the tables using the sql_queries.py queries
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    cur, conn = create_database()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()