from config import saved_instances
from dbHelpers.db_connection import create_connection
from dbHelpers.db_connection import close_connection


# Fetching saved instances in the config file
def fetch_instances(session_id):
    season = saved_instances[session_id]['season']
    date = saved_instances[session_id]['date']
    venue = saved_instances[session_id]['venue']
    return season, date, venue


# Fetching first umpire from the table
def get_first_umpire(session_id):
    season, date, venue = fetch_instances(session_id=session_id)
    connection = create_connection()
    cursor = connection.cursor()
    query = f"SELECT umpire1 FROM iplstat WHERE season={season} AND date='{date}' AND venue='{venue}';"
    cursor.execute(query)
    umpire = cursor.fetchone()[0]
    cursor.close()
    close_connection(connection)
    return {'fulfillmentText': umpire}


# Fetching second umpire from the table
def get_second_umpire(session_id):
    season, date, venue = fetch_instances(session_id=session_id)
    connection = create_connection()
    cursor = connection.cursor()
    query = f"SELECT umpire2 FROM iplstat WHERE season={season} AND date='{date}' AND venue='{venue}';"
    cursor.execute(query)
    umpire = cursor.fetchone()[0]
    cursor.close()
    close_connection(connection)
    return {'fulfillmentText': umpire}
    

# Fetching both the umpires from the table
def get_both_umpires(session_id):
    season, date, venue = fetch_instances(session_id=session_id)
    connection = create_connection()
    cursor = connection.cursor()
    query = f"SELECT umpire1 FROM iplstat WHERE season={season} AND date='{date}' AND venue='{venue}';"
    cursor.execute(query)
    umpire1 = cursor.fetchone()[0]
    query = f"SELECT umpire2 FROM iplstat WHERE season={season} AND date='{date}' AND venue='{venue}';"
    cursor.execute(query)
    umpire2 = cursor.fetchone()[0]
    cursor.close()
    close_connection(connection)
    del saved_instances[session_id]
    return {'fulfillmentText': f"{umpire1}, {umpire2}"}



