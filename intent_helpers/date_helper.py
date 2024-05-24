from config import saved_instances
from db_helpers.venues_db import getVenues
from db_helpers.player_of_the_match_db import get_player_of_the_match

def dateHandler(payload):
    
    from helpers.generic_helpers import want_to_know_more, more_options
    from helpers.generic_helpers import umpire_sub_intents, team_sub_intents, match_sub_intents

    # Fetching session id
    session_id = payload['session']

    # Date
    date = payload['queryResult']['queryText']
    saved_instances[session_id]['date'] = date  

    venues = getVenues(year=saved_instances[session_id]['season'], date=date)

    if len(venues) == 1:
        saved_instances[session_id]['venue'] = venues[0]
        intent = saved_instances[session_id]['intent']
        if intent == 'Umpire Info':
            return umpire_sub_intents[saved_instances[session_id]['subIntent']](session_id)  
        elif intent == 'Team Info':
            return team_sub_intents[saved_instances[session_id]['subIntent']](session_id) 
        elif intent == 'Match Info':
            return match_sub_intents[saved_instances[session_id]['subIntent']](session_id)
        elif intent == 'Player of the Match':
            return get_player_of_the_match(session_id) 
    elif len(venues) > 1:
        options = [{"text": venue} for venue in venues]
        response_payload =  [{'text': {'text': ['Which venue info do you want?']}}, {'payload': {'richContent': [[{'type': 'chips', 'options': options}]]}}]
        return {"fulfillmentMessages": response_payload}
    else:
        response_payload = [{'text': {'text': [f'Sorry!! No record found!!.\n{want_to_know_more}']}}, {'payload': {'richContent': [[{'type': 'chips', 'options': more_options}]]}}]
        return {"fulfillmentMessages": response_payload}