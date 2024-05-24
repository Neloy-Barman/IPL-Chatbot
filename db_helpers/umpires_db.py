from config import saved_instances
from db_helpers.db_connection import create_connection, close_connection


# Fetching first umpire from the table
def get_first_umpire(session_id):
    from helpers.generic_helpers import fetch_instances
    from helpers.generic_helpers import want_to_know_more, more_options
    season, date, venue = fetch_instances(session_id=session_id)
    connection = create_connection()
    cursor = connection.cursor()
    query = f"SELECT umpire1 FROM iplstat WHERE season={season} AND date='{date}' AND venue='{venue}';"
    cursor.execute(query)
    umpire = cursor.fetchone()[0]
    cursor.close()
    close_connection(connection)
    response_payload = [{'text': {'text': [f'The 1st umpire was "{umpire}".\n{want_to_know_more}']}}, {'payload': {'richContent': [[{'type': 'chips', 'options': more_options}]]}}]
    return {"fulfillmentMessages": response_payload}


# Fetching second umpire from the table
def get_second_umpire(session_id):
    from helpers.generic_helpers import fetch_instances
    from helpers.generic_helpers import want_to_know_more, more_options
    season, date, venue = fetch_instances(session_id=session_id)
    connection = create_connection()
    cursor = connection.cursor()
    query = f"SELECT umpire2 FROM iplstat WHERE season={season} AND date='{date}' AND venue='{venue}';"
    cursor.execute(query)
    umpire = cursor.fetchone()[0]
    cursor.close()
    close_connection(connection)
    response_payload = [{'text': {'text': [f'The 2nd umpire was "{umpire}".\n{want_to_know_more}']}}, {'payload': {'richContent': [[{'type': 'chips', 'options': more_options}]]}}]
    return {"fulfillmentMessages": response_payload}
    

# Fetching both the umpires from the table
def get_both_umpires(session_id):
    from helpers.generic_helpers import fetch_instances
    from helpers.generic_helpers import want_to_know_more, more_options
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
    response_payload = [{'text': {'text': [f'The 1st umpire was "{umpire1}" and the 2nd one was "{umpire2}".\n{want_to_know_more}']}}, {'payload': {'richContent': [[{'type': 'chips', 'options': more_options}]]}}]
    return {"fulfillmentMessages": response_payload}



