from db_helpers.db_connection import create_connection, close_connection


def getVenues(year: int, date):
        
    # Connection to the database
    connection = create_connection()

    # Creating a cursor object to execute SQL queries
    cursor = connection.cursor()

    # Selection query
    query = f"SELECT venue FROM iplstat WHERE season={year} AND date='{date}';"

    # Executing query using cursor
    cursor.execute(query)

    # Fetching data from the cursor
    venues_ = cursor.fetchall()

    venues = [venue[0] for venue in venues_] 

    # for venue in venues:
    #     print(venue[0])

    # Closing the cursor and the connection
    cursor.close()
    close_connection(connection=connection)

    return venues
