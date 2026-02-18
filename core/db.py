import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

def get_connect():
    return(
        psycopg2.connect(
            host = os.getenv('DB_HOST'),
            user = os.getenv('DB_USER'),
            password = os.getenv('DB_PASS'),
            dbname = os.getenv('DB_NAME'),
            port = os.getenv('DB_PORT')
        )
    )

def execute_query(query):
    conn = get_connect()
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()    
