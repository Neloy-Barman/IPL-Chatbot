from db_helpers.db_connection import create_connection, close_connection


def getSeasons():
    # Connection to the database
    connection = create_connection()

    # Creating a cursor object to execute SQL queries
    cursor = connection.cursor()

    # Selection query
    query = "SELECT DISTINCT season FROM iplstat;"

    # Executing query using cursor
    cursor.execute(query)

    # Fetching data from the cursor
    seasons_ = cursor.fetchall()
    seasons =  [season[0] for season in seasons_]
    
    # for season in seasons_:
    #     print(season)

    # Closing the cursor and the connection
    cursor.close()
    close_connection(connection=connection)
    
    return seasons
