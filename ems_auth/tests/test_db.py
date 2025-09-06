import psycopg2
import os
from dotenv import load_dotenv


class TestDBConnection:
    def test_connection(self):
        load_dotenv()
        conn = psycopg2.connect(
            dbname=os.environ.get("DB_NAME"),
            user=os.environ.get("DB_USERNAME"),
            password=os.environ.get("DB_PASSWORD"),
            host=os.environ.get("DB_HOST"),
            port=os.environ.get("DB_PORT"),
        )
        print("✅ Connected successfully")
        conn.close()
