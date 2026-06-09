from psycopg2 import connect

def get_db_connection():
    conn = connect(
        host='db',
        database='mydatabase',
        user='postgres',
        password='password',
        port=5432
    )
    return conn

