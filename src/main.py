import os

from src.constants import *
from src.utils.groupings import generate_new_groups
from src.utils.utils import format_groupings_to_readable_format
from src.store.store import serialize_as_json, deserialize_json, load_graph, update_existing_groupings_file

def generate_response(data):
    msg = " ".join(data['text'].split(" ")[1:]).lower()
    if msg == CURRENT_DATES_COMMAND:
        # return last group in all groupings
        # return get_current_dates()
        return CURRENT_DATES_COMMAND
    elif msg == NEW_DATES_COMMAND:
        # if time for new dates, return new dates
        # else return not time for new dates yet
        # return generate_new_dates()
        return NEW_DATES_COMMAND
    elif msg == HELP_COMMAND:
        BOT_NAME = os.getenv('BOT_NAME')
        return
        """Usage:
                @{0} current dates — I will send the current week's dates.
                @{1} new dates — I will generate new dates and send them for everyone to see 🥳.
                @{2} help — I will return this help text letting you know how to invoke me!
        """.format(BOT_NAME, BOT_NAME, BOT_NAME)
    return None


def generate_new_dates():
    graph = load_graph(GRAPH_FILENAME)
    existing_groupings = deserialize_json(WEEKLY_GROUPINGS_FILENAME)
    groups = generate_new_groups(graph, existing_groupings, n=GROUP_SIZE)
    serialize_as_json(GRAPH_FILENAME, graph)
    update_existing_groupings_file(WEEKLY_GROUPINGS_FILENAME, existing_groupings, groups)
    return format_groupings_to_readable_format(groups)

def get_current_dates():
    existing_groupings = deserialize_json(WEEKLY_GROUPINGS_FILENAME)
    current_dates = existing_groupings[len(existing_groupings)-1]
    return format_groupings_to_readable_format(current_dates)
