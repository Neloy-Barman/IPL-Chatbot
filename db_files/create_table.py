from db_helpers.db_connection import create_connection, close_connection


# Create connection
connection = create_connection()

if connection.is_connected():
    print("Connection successful.")
else:
    print("Connection failed!!")

# Table Creation  
table_creation_query = """
    CREATE TABLE iplstat (
        sid INT AUTO_INCREMENT PRIMARY KEY,
        season INT,
        city VARCHAR(255),
        date DATE,
        team1 VARCHAR(255),
        team2 VARCHAR(255),
        toss_winner VARCHAR(255),
        toss_decision VARCHAR(50),
        result VARCHAR(50),
        dl_applied INT,
        winner VARCHAR(255),
        win_by_runs INT, 
        win_by_wickets INT,
        player_of_match VARCHAR(255),
        venue VARCHAR(255),
        umpire1 VARCHAR(255),
        umpire2 VARCHAR(255)
    );
""" 

# Creating a cursor object to execute SQL queries
cursor = connection.cursor()

cursor.execute(table_creation_query)

# Committing changes to the database
connection.commit()

# Closing the cursor and the connection
cursor.close()
close_connection(connection)

print("Table created successfully!!!")