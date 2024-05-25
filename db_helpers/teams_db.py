from db_helpers.db_connection import create_connection, close_connection

# Fetching Team from the table
def teams(session_id):
    from generic_helpers import fetch_instances
    from generic_helpers import want_to_know_more, more_options
    season, date, venue = fetch_instances(session_id=session_id)
    connection = create_connection()
    cursor = connection.cursor()
    query = f"SELECT team1 FROM iplstat WHERE season={season} AND date='{date}' AND venue='{venue}';"
    cursor.execute(query)
    team1 = cursor.fetchone()[0]
    query = f"SELECT team2 FROM iplstat WHERE season={season} AND date='{date}' AND venue='{venue}';"
    cursor.execute(query)
    team2 = cursor.fetchone()[0]
    cursor.close()
    close_connection(connection)
    response_payload = [{'text': {'text': [f'"{team1}" played against "{team2}".\n{want_to_know_more}']}}, {'payload': {'richContent': [[{'type': 'chips', 'options': more_options}]]}}]
    return {"fulfillmentMessages": response_payload}


# Fetching winner team from the table
def match_winner(session_id):
    from generic_helpers import fetch_instances
    from generic_helpers import want_to_know_more, more_options
    season, date, venue = fetch_instances(session_id=session_id)
    connection = create_connection()
    cursor = connection.cursor()
    query = f"SELECT winner FROM iplstat WHERE season={season} AND date='{date}' AND venue='{venue}';"
    cursor.execute(query)
    team = cursor.fetchone()[0]
    cursor.close()
    close_connection(connection)
    response_payload = [{'text': {'text': [f'"{team}" won the match.\n{want_to_know_more}']}}, {'payload': {'richContent': [[{'type': 'chips', 'options': more_options}]]}}]
    return {"fulfillmentMessages": response_payload}


# Fetching toss winner team from the table
def toss_winner(session_id):
    from generic_helpers import fetch_instances
    from generic_helpers import want_to_know_more, more_options
    season, date, venue = fetch_instances(session_id=session_id)
    connection = create_connection()
    cursor = connection.cursor()
    query = f"SELECT toss_winner FROM iplstat WHERE season={season} AND date='{date}' AND venue='{venue}';"
    cursor.execute(query)
    team = cursor.fetchone()[0]
    cursor.close()
    close_connection(connection)
    response_payload = [{'text': {'text': [f'"{team}" won the toss.\n{want_to_know_more}']}}, {'payload': {'richContent': [[{'type': 'chips', 'options': more_options}]]}}]
    return {"fulfillmentMessages": response_payload}




