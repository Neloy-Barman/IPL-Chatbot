import mysql.connector

def getVenues(year: int):
    # Connection to the database
    connection = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "root",
        database = "ipldb"
    )

    # Creating a cursor object to execute SQL queries
    cursor = connection.cursor()

    # Selection query
    query = f"SELECT DISTINCT venue FROM iplstat WHERE season={year};"

    # Executing query using cursor
    cursor.execute(query)

    # Fetching data from the cursor
    venues_ = cursor.fetchall()

    venues = [venue[0] for venue in venues_] 

    # for venue in venues:
    #     print(venue[0])

    # Closing the cursor and the connection
    cursor.close()
    connection.close()

    return venues
