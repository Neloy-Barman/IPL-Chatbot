from config import saved_instances
from dbHelpers.seasons_db import getSeasons


# Umpire Info Intent Handler
def umpireInfoHandler(payload):
    # Text fetched from the chatbot agent
    response_payload = payload['queryResult']['fulfillmentMessages']
    # Session Id
    session_id = payload['session']
    saved_instances[session_id] = {}
    saved_instances[session_id]['intent'] = 'Umpire Info'
    return response_payload


# Umpire Info Next process Handler
def umpireInfoNextHandler(payload):
    session_id = payload['session']
    next_info = payload['queryResult']['queryText']
    saved_instances[session_id]['subIntent'] = next_info
    seasons = getSeasons()
    seasons.sort()
    options = [{"text": str(season)} for season in seasons]
    response_payload =  [{'text': {'text': ['I can assist you with the details about the umpires, but please choose one option from the following.']}}, {'payload': {'richContent': [[{'type': 'chips', 'options': options}]]}}]
    return {"fulfillmentMessages": response_payload}
