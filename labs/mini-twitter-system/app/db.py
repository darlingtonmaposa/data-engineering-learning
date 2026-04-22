import psycopg2

def get_db_connection():

    """"
    Establish a connection to the PostgreSQL database and returns the connection object.
    """
    return psycopg2.connect(
        dbname="mini_twitter",
        user="postgres",
        password="maposa",
        host="172.20.112.1",
        port=5432
    )


