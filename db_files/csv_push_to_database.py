import csv
from db_helpers.db_connection import create_connection, close_connection


# Create connection
connection = create_connection()

if connection.is_connected():
    print("Connection successful.")
else:
    print("Connection failed!!")

# Creating a cursor object to execute SQL queries
cursor = connection.cursor()

# Opening the csv file
with open('Data/IPL_chatbot_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    # Skipping Header Row
    next(csv_reader)

    # Iterating over rows and executing queries
    for row in csv_reader:
        query = "INSERT INTO iplstat(season, city, date, team1, team2, toss_winner, toss_decision, result, dl_applied, winner, win_by_runs, win_by_wickets, player_of_match, venue, umpire1, umpire2) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        cursor.execute(query, (row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16]))

# Committing changes to the database
connection.commit()

# Closing the cursor and the connection
cursor.close()
close_connection(connection)

print("Data inserted successfully!!")