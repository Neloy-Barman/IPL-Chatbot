import os
import mysql.connector
from dotenv import load_dotenv


load_dotenv()

db_host = os.getenv("db_host")
db_user = os.getenv("db_user")
db_password = os.getenv("db_password")
db_database = os.getenv("db_database")
db_port = os.getenv("db_port")

def create_connection():
    connection = mysql.connector.connect(
        host = db_host,
        user =  db_user,
        password = db_password,
        database = db_database,
        port = db_port
    )
    
    return connection


def close_connection(connection):
    connection.close()
