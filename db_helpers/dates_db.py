from db_helpers.db_connection import create_connection
from db_helpers.db_connection import close_connection


def getDateRange(season: int):
    # Connection to the database
    connection = create_connection()

    # Creating a cursor object to execute SQL queries
    cursor = connection.cursor()

    # Selection query
    query = f"SELECT MAX(date), MIN(date) FROM iplstat WHERE season={season};"

    # Executing query using cursor
    cursor.execute(query)

    # Fetching data from the cursor
    result = cursor.fetchone()

    # Extract the highest and lowest dates
    max_date = result[0]
    min_date = result[1]

    # Closing the cursor and the connection
    cursor.close()
    close_connection(connection)

    return max_date, min_date  
