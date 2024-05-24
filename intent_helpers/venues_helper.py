from config import saved_instances
from db_helpers.player_of_the_match_db import get_player_of_the_match

def venueHandler(payload):
    from helpers.generic_helpers import umpire_sub_intents, team_sub_intents, match_sub_intents
    
    # Fetching session id
    session_id = payload['session']

    # venue
    venue = payload['queryResult']['queryText']
    saved_instances[session_id]['venue'] = venue

    intent = saved_instances[session_id]['intent']
    if intent == 'Umpire Info':
        return umpire_sub_intents[saved_instances[session_id]['subIntent']](session_id)  
    elif intent == 'Team Info':
        return team_sub_intents[saved_instances[session_id]['subIntent']](session_id) 
    elif intent == "Match Info":
        return match_sub_intents[saved_instances[session_id]['subIntent']](session_id) 
    elif intent == 'Player of the Match':
        return get_player_of_the_match(session_id) 