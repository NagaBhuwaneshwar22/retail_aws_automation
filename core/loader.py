import os
from dotenv import load_dotenv
load_dotenv()

def load_to_postgres(df, table_name):
    url = f"jdbc:postgresql://{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    properties = {
        'password' : os.getenv('DB_PASS'),
        'user' : os.getenv('DB_USER'),
        'driver':"org.postgresql.Driver"
    }

    df.write \
    .mode(os.getenv('WRITE_MODE')) \
    .jdbc(url=url, table=table_name, properties=properties)

    