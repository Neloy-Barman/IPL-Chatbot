from config import saved_instances
from db_helpers.seasons_db import getSeasons


# Match Info Intent Handler
def playerOfMatchHandler(payload):
    # Text fetched from the chatbot agent
    response_payload = payload['queryResult']['fulfillmentMessages']
    # Session Id
    session_id = payload['session']
    saved_instances[session_id] = {}
    saved_instances[session_id]['intent'] = 'Player of the Match'
    saved_instances[session_id]['subIntent'] = 'Player of the Match'
    seasons = getSeasons()
    seasons.sort()
    options = [{"text": str(season)} for season in seasons]
    response_payload =  [{'text': {'text': ['I can tell you who the player of match was, but you have to specify the season.']}}, {'payload': {'richContent': [[{'type': 'chips', 'options': options}]]}}]
    return {"fulfillmentMessages": response_payload}
