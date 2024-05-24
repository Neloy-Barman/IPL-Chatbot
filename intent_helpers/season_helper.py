from config import saved_instances
from dbHelpers.dates_db import getDateRange


def seasonHandler(payload):

    # Fetching session id
    session_id = payload['session']

    # Year
    year = payload['queryResult']['queryText']
    
    # Converting year to string
    year = int(year)

    saved_instances[session_id]['season'] = year

    max_date, min_date = getDateRange(season=year)

    response_text = f"The {year} session of IPL held between {min_date} to {max_date}. Kindly Enter a date between these to proceed."

    return {"fulfillmentText": response_text}
