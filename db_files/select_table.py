from db_helpers.db_connection import create_connection, close_connection


# Create connection
connection = create_connection()

if connection.is_connected():
    print("Connection successful.")
else:
    print("Connection failed!!")

# Selection query
query = "SELECT * FROM iplstat;"

# Creating a cursor object to execute SQL queries
cursor = connection.cursor()

# Executing query
cursor.execute(query)

# Fetching rows
rows = cursor.fetchall()

# Viewing rows
for row in rows:
    print(row)

# Closing the cursor and the connection
cursor.close()
close_connection(connection)