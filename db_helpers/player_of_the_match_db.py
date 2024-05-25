from config import saved_instances
from db_helpers.db_connection import create_connection
from db_helpers.db_connection import close_connection


# Fetching first umpire from the table
def get_player_of_the_match(session_id):
    from generic_helpers import fetch_instances
    from generic_helpers import want_to_know_more, more_options
    season, date, venue = fetch_instances(session_id=session_id)
    connection = create_connection()
    cursor = connection.cursor()
    query = f"SELECT player_of_match FROM iplstat WHERE season={season} AND date='{date}' AND venue='{venue}';"
    cursor.execute(query)
    player = cursor.fetchone()[0]
    cursor.close()
    close_connection(connection)
    response_payload = [{'text': {'text': [f'"{player}" was the player of the match.\n{want_to_know_more}']}}, {'payload': {'richContent': [[{'type': 'chips', 'options': more_options}]]}}]
    return {"fulfillmentMessages": response_payload}