from datetime import datetime, timedelta
import os

from src.constants import *
from src.utils.groupings import generate_new_groups
from src.utils.utils import format_groupings_to_readable_format
from src.store.store import serialize_as_json, deserialize_json, load_graph, update_existing_groupings_file

def generate_response(data):
    msg = " ".join(data['text'].split(" ")[1:]).lower()
    if msg == CURRENT_DATES_COMMAND:
        return get_current_dates()
    elif msg == NEW_DATES_COMMAND:
        existing_groupings = deserialize_json(WEEKLY_GROUPINGS_FILENAME)
        latest_grouping_idx = len(existing_groupings)-1
        latest_grouping = datetime.strptime(existing_groupings[latest_grouping_idx]['date'], DATETIME_FORMAT)
        if datetime.now().weekday() == MONDAY and (datetime.now()-latest_grouping).days >= 6:
            return generate_new_dates(existing_groupings)
        next_dates_date = datetime.now()+timedelta(days=(7-latest_grouping.weekday()))
        return "Oops, it's not time for new dates yet! New dates will be available on {} 👀.".format(datetime.strftime(next_dates_date, "%A, %B %d, %Y"))
    elif msg == HELP_COMMAND:
        BOT_NAME = os.getenv('BOT_NAME')
        return ("Usage:\n\n"
        "@{0} current dates --> see the current dates.\n"
        "@{1} new dates --> get new dates (once a week) 🥳.\n"
        "@{2} help --> get info on how to invoke bot 🤖.").format(BOT_NAME, BOT_NAME, BOT_NAME)

from pprint import pprint
def get_current_dates():
    existing_groupings = deserialize_json(WEEKLY_GROUPINGS_FILENAME)
    current_dates = existing_groupings[len(existing_groupings)-1]
    return format_groupings_to_readable_format(current_dates['groupings'])

def generate_new_dates(existing_groupings):
    graph = load_graph(GRAPH_FILENAME)
    groups = generate_new_groups(graph, existing_groupings, n=GROUP_SIZE)
    # serialize_as_json(GRAPH_FILENAME, graph)
    # update_existing_groupings_file(WEEKLY_GROUPINGS_FILENAME, existing_groupings, groups)
    return format_groupings_to_readable_format(groups[1:])
