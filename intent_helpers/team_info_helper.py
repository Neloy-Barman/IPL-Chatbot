from config import saved_instances
from dbHelpers.seasons_db import getSeasons


# Team Info intent Handler
def teamInfoHandler(payload):
    # Text fetched from the chatbot agent
    response_payload = payload['queryResult']['fulfillmentMessages']
    # Session Id
    session_id = payload['session']
    saved_instances[session_id] = {}
    saved_instances[session_id]['intent'] = 'Team Info'
    print(f'This is saved instance: {saved_instances}')
    return response_payload


# Team Info Next process Handler
def teamInfoNextHandler(payload):
    session_id = payload['session']
    next_info = payload['queryResult']['queryText']
    saved_instances[session_id]['subIntent'] = next_info
    seasons = getSeasons()
    seasons.sort()
    options = [{"text": str(season)} for season in seasons]
    response_payload =  [{'text': {'text': ['I can assist you with the team information, but please choose one season from the following.']}}, {'payload': {'richContent': [[{'type': 'chips', 'options': options}]]}}]
    return {"fulfillmentMessages": response_payload}