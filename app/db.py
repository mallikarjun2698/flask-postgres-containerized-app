
import os
from psycopg2 import connect
from dotenv import load_dotenv

load_dotenv()
def get_db_connection():
    conn = connect(
        host=os.getenv('DB_HOST', 'localhost'),
        database=os.getenv('DB_NAME', 'mydatabase'),
        user=os.getenv('DB_USER', 'postgres'),
        password=os.getenv('DB_PASS', 'password'),
        port=os.getenv('DB_PORT', 5432)
    )
    return conn
