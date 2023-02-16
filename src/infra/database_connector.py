import os
import mysql.connector as mysql
from dotenv import load_dotenv

load_dotenv()


class DatabaseConnector:
    """DatabaseConnector."""

    connection = None

    @classmethod
    def connect(cls):
        """Connect."""
        passwd = os.getenv("MYSQL_ROOT_PASSWORD")
        db_connection = mysql.connect(
            host="localhost",
            port="3306",
            database="pipeline_db",
            user="root",
            passwd=f"{passwd}",
        )
        cls.connection = db_connection
