import mysql.connector

def create_connection():
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database = "ipldb"
    )
    
    return connection

def close_connection(connection):
    connection.close()
