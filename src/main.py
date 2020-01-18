import os

from datetime import datetime, timedelta

from src.constants.commands import CURRENT_DATES_COMMAND, HELP_COMMAND, NEW_DATES_COMMAND
from src.constants.constants import MONDAY, BOT_NAME, GROUP_SIZE
from src.utils.groupings import generate_new_groups
from src.utils.utils import groupings_to_str

def generate_response(data, graph_client, grouping_client):
    msg = " ".join(data['text'].split(" ")[1:]).lower()
    if msg == CURRENT_DATES_COMMAND:
        return handle_current_dates_command(grouping_client)
    elif msg == NEW_DATES_COMMAND:
        return handle_new_dates_command(graph_client, grouping_client)
    elif msg == HELP_COMMAND:
        BOT_NAME = os.getenv('BOT_NAME')
        return ("Usage:\n\n"
        "@{0} current dates --> see the current dates.\n"
        "@{1} new dates --> get new dates (once a week) 🥳.\n"
        "@{2} help --> get info on how to invoke bot 🤖.").format(BOT_NAME, BOT_NAME, BOT_NAME)

def handle_current_dates_command(grouping_client):
    current_groupings = grouping_client.get_latest_grouping()
    excluded_member = current_groupings['excluded'][0]
    return groupings_to_str(current_groupings['groupings'], excluded_member)

def handle_new_dates_command(graph_client, grouping_client):
    latest_grouping = grouping_client.get_latest_grouping()
    now = datetime.now()
    if now.weekday() == MONDAY and (now-latest_grouping['date']).days >= 6:
        existing_groupings = grouping_client.get_all_groupings()
        return generate_new_dates(existing_groupings, graph_client, grouping_client)
    # current date + days until next monday
    new_dates_date = now+timedelta(days=(7-now.weekday()))
    return "Oops, it's not time for new dates yet! New dates will be available on {} 👀.".format(datetime.strftime(new_dates_date,
                                                                                                                       "%A, %B %d, %Y"))

def generate_new_dates(existing_groupings, graph_client, grouping_client):
    graph = graph_client.get_latest_graph_instance()['graph']
    groups, updated_graph = generate_new_groups(graph, existing_groupings, n=GROUP_SIZE)    
    graph_client.insert_graph_instance(updated_graph)
    excluded_member = None
    groups = groups
    if len(groups[0]) == 1:
        excluded_member = groups[0][0]
        groups = groups[1:]
    grouping_client.insert_grouping(groups, excluded_member=excluded_member)
    return groupings_to_str(groups, excluded_member)
