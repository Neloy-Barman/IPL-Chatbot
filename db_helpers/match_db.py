from db_helpers.db_connection import create_connection, close_connection


# Fetching toss decision
def toss_decision(session_id):
    from helpers.generic_helpers import fetch_instances
    from helpers.generic_helpers import want_to_know_more, more_options
    season, date, venue = fetch_instances(session_id=session_id)
    connection = create_connection()
    cursor = connection.cursor()
    query = f"SELECT toss_winner FROM iplstat WHERE season={season} AND date='{date}' AND venue='{venue}';"
    cursor.execute(query)
    team = cursor.fetchone()[0]
    query = f"SELECT toss_decision FROM iplstat WHERE season={season} AND date='{date}' AND venue='{venue}';"
    cursor.execute(query)
    decision = cursor.fetchone()[0]
    cursor.close()
    close_connection(connection)
    response_payload = [{'text': {'text': [f'"{team}" won the toss and decided to "{decision}".\n{want_to_know_more}']}}, {'payload': {'richContent': [[{'type': 'chips', 'options': more_options}]]}}]
    return {"fulfillmentMessages": response_payload}


# Fetching win by runs
def win_by_runs(session_id):
    from helpers.generic_helpers import fetch_instances
    from helpers.generic_helpers import want_to_know_more, more_options
    season, date, venue = fetch_instances(session_id=session_id)
    connection = create_connection()
    cursor = connection.cursor()
    query = f"SELECT winner FROM iplstat WHERE season={season} AND date='{date}' AND venue='{venue}';"
    cursor.execute(query)
    team = cursor.fetchone()[0]
    query = f"SELECT win_by_runs FROM iplstat WHERE season={season} AND date='{date}' AND venue='{venue}';"
    cursor.execute(query)
    runs = cursor.fetchone()[0]
    cursor.close()
    close_connection(connection)
    response_payload = [{'text': {'text': [f'"{team}" won by "{runs} runs".\n{want_to_know_more}']}}, {'payload': {'richContent': [[{'type': 'chips', 'options': more_options}]]}}]
    return {"fulfillmentMessages": response_payload}


# Fetching win by wickets
def win_by_wickets(session_id):
    from helpers.generic_helpers import fetch_instances
    from helpers.generic_helpers import want_to_know_more, more_options
    season, date, venue = fetch_instances(session_id=session_id)
    connection = create_connection()
    cursor = connection.cursor()
    query = f"SELECT winner FROM iplstat WHERE season={season} AND date='{date}' AND venue='{venue}';"
    cursor.execute(query)
    team = cursor.fetchone()[0]
    query = f"SELECT win_by_wickets FROM iplstat WHERE season={season} AND date='{date}' AND venue='{venue}';"
    cursor.execute(query)
    wickets = cursor.fetchone()[0]
    cursor.close()
    close_connection(connection)
    response_payload = [{'text': {'text': [f'"{team}" won by "{wickets} wickets".\n{want_to_know_more}']}}, {'payload': {'richContent': [[{'type': 'chips', 'options': more_options}]]}}]
    return {"fulfillmentMessages": response_payload}


# Fetching match result
def result(session_id):
    from helpers.generic_helpers import fetch_instances
    from helpers.generic_helpers import want_to_know_more, more_options
    season, date, venue = fetch_instances(session_id=session_id)
    connection = create_connection()
    cursor = connection.cursor()
    query = f"SELECT result FROM iplstat WHERE season={season} AND date='{date}' AND venue='{venue}';"
    cursor.execute(query)
    res = cursor.fetchone()[0]
    cursor.close()
    close_connection(connection)
    response_payload = [{'text': {'text': [f'Match result was "{res}".\n{want_to_know_more}']}}, {'payload': {'richContent': [[{'type': 'chips', 'options': more_options}]]}}]
    return {"fulfillmentMessages": response_payload}


# Fetching dls applied or not
def dls(session_id):
    from helpers.generic_helpers import fetch_instances
    from helpers.generic_helpers import want_to_know_more, more_options
    season, date, venue = fetch_instances(session_id=session_id)
    connection = create_connection()
    cursor = connection.cursor()
    query = f"SELECT dl_applied FROM iplstat WHERE season={season} AND date='{date}' AND venue='{venue}';"
    cursor.execute(query)
    dl_applied = cursor.fetchone()[0]
    cursor.close()
    close_connection(connection)
    if dl_applied:
        text = "'DLS' was applied."
    else:
        text = "'DLS' was 'not' applied."
    response_payload = [{'text': {'text': [f'{text}.\n{want_to_know_more}']}}, {'payload': {'richContent': [[{'type': 'chips', 'options': more_options}]]}}]
    return {"fulfillmentMessages": response_payload}




