from config import saved_instances
from db_helpers.seasons_db import getSeasons


# Match Info Intent Handler
def matchInfoHandler(payload):
    # Text fetched from the chatbot agent
    response_payload = payload['queryResult']['fulfillmentMessages']
    # Session Id
    session_id = payload['session']
    saved_instances[session_id] = {}
    saved_instances[session_id]['intent'] = 'Match Info'
    return response_payload


# Match Info Next process Handler
def matchInfoNextHandler(payload):
    session_id = payload['session']
    next_info = payload['queryResult']['queryText']
    saved_instances[session_id]['subIntent'] = next_info
    seasons = getSeasons()
    seasons.sort()
    options = [{"text": str(season)} for season in seasons]
    response_payload =  [{'text': {'text': ['I can assist you with match detail info, but please choose one option from the following.']}}, {'payload': {'richContent': [[{'type': 'chips', 'options': options}]]}}]
    return {"fulfillmentMessages": response_payload}
