from datetime import datetime, timedelta
import os

from src.constants import *
from src.utils.groupings import generate_new_groups
from src.utils.utils import format_groupings_to_readable_format

def generate_response(data, graph_client, grouping_client):
    msg = " ".join(data['text'].split(" ")[1:]).lower()
    if msg == CURRENT_DATES_COMMAND:
        return get_current_dates(grouping_client)
    elif msg == NEW_DATES_COMMAND:
        latest_grouping = grouping_client.get_latest_grouping()
        if datetime.now().weekday() == MONDAY and (datetime.now()-latest_grouping['date']).days >= 6:
            existing_groupings = grouping_client.get_all_groupings()
            return generate_new_dates(existing_groupings, graph_client, grouping_client)
        next_dates_date = datetime.now()+timedelta(days=(7-latest_grouping['date'].weekday()))
        return "Oops, it's not time for new dates yet! New dates will be available on {} 👀.".format(datetime.strftime(next_dates_date, "%A, %B %d, %Y"))
    elif msg == HELP_COMMAND:
        BOT_NAME = os.getenv('BOT_NAME')
        return ("Usage:\n\n"
        "@{0} current dates --> see the current dates.\n"
        "@{1} new dates --> get new dates (once a week) 🥳.\n"
        "@{2} help --> get info on how to invoke bot 🤖.").format(BOT_NAME, BOT_NAME, BOT_NAME)

from pprint import pprint
def get_current_dates(grouping_client):
    current_groupings = grouping_client.get_latest_grouping()
    excluded_member = current_groupings['excluded'][0]
    return format_groupings_to_readable_format(current_groupings['groupings'], excluded_member)

def generate_new_dates(existing_groupings, graph_client, grouping_client):
    graph = graph_client.get_latest_graph_instance()['graph']
    groups, updated_graph = generate_new_groups(graph, existing_groupings, n=GROUP_SIZE)    
    graph_client.insert_graph_instance(updated_graph)
    grouping_client.insert_grouping(groups[1:], excluded_member=groups[0][0])
    return format_groupings_to_readable_format(groups[1:], groups[0][0])
