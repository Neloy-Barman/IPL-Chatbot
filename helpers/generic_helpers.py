from config import saved_instances
from intent_helpers.date_helper import dateHandler
from intent_helpers.venues_helper import venueHandler
from intent_helpers.season_helper import seasonHandler
from db_helpers.teams_db import teams, match_winner, toss_winner
from intent_helpers.player_of_match_helper import playerOfMatchHandler
from intent_helpers.team_info_helper import teamInfoHandler, teamInfoNextHandler
from intent_helpers.match_info_helper import matchInfoHandler, matchInfoNextHandler
from intent_helpers.umpire_info_helper import umpireInfoHandler, umpireInfoNextHandler
from db_helpers.umpires_db import get_first_umpire, get_second_umpire, get_both_umpires
from db_helpers.match_db import toss_decision, win_by_runs, win_by_wickets, dls, result

want_to_know_more = "Do you wish to know more?"
more_options = [{"text": "Yes"},{"text": "No"}]

intents_mapping = {
    "Venue" : venueHandler,
    "Date Info": dateHandler,
    "Seasons" : seasonHandler,
    "Team Info" : teamInfoHandler,
    "Match Info" : matchInfoHandler,
    "Umpire Info" : umpireInfoHandler,
    "Team Info Next" : teamInfoNextHandler,
    "Match Info Next" : matchInfoNextHandler,
    "Umpire Info Next" : umpireInfoNextHandler,
    "Player of the Match": playerOfMatchHandler
}

team_sub_intents = {
    'Teams': teams,
    'Toss Winner': toss_winner,
    'Match Winner': match_winner,
}

umpire_sub_intents = {
    '1st Umpire': get_first_umpire,
    '2nd Umpire': get_second_umpire,
    'Both the Umpires': get_both_umpires
}

match_sub_intents = {
    'Toss Decision': toss_decision,
    'Runs Win': win_by_runs,
    'Wickets Win': win_by_wickets,
    'DLS': dls,
    'Result': result,
}

# Fetching saved instances in the config file
def fetch_instances(session_id):
    season = saved_instances[session_id]['season']
    date = saved_instances[session_id]['date']
    venue = saved_instances[session_id]['venue']
    return season, date, venue