from datetime import datetime, timedelta
import os

from injector import inject

from .constants.constants import NEW_DATES_DAY, BOT_NAME, GROUP_SIZE, CURRENT_DATES_COMMAND, HELP_COMMAND, NEW_DATES_COMMAND, YOU_UP_COMMAND
from .utils.groupings import generate_new_groups, groupings_to_str
from .store.clients import GraphMongoClient, GroupingMongoClient


class ResponseGenerator:
    @inject
    def __init__(self, graph_client: GraphMongoClient,
                 grouping_client: GroupingMongoClient):
        self.graph_client = graph_client
        self.grouping_client = grouping_client

    def status(self):
        return str(self.grouping_client.get_latest_grouping())

    def handle_current_dates_command(self):
        print("getting current dates")
        current_groupings = self.grouping_client.get_latest_grouping()
        excluded_member = current_groupings['excluded'][0]
        return groupings_to_str(current_groupings['groupings'], excluded_member)

    def generate_new_dates(self, all_groupings):
        print("generating new dates")
        graph = self.graph_client.get_latest_graph_instance()['graph']
        groups, updated_graph = generate_new_groups(
            graph, all_groupings, n=GROUP_SIZE)
        print("inserting graph into mongo")
        self.graph_client.insert_graph_instance(updated_graph)
        excluded_member = None
        groups = groups
        if len(groups[0]) == 1:
            print("found an excluded member")
            excluded_member = groups[0][0]
            groups = groups[1:]
        print("inserting grouping into mongo")
        self.grouping_client.insert_grouping(
            groups, excluded_member=excluded_member)
        return groupings_to_str(groups, excluded_member)

    def handle_new_dates_command(self):
        most_recent_grouping = self.grouping_client.get_latest_grouping()
        now = datetime.now()
        print("checking if it is time for new dates")
        if now.weekday() == NEW_DATES_DAY and (now-most_recent_grouping['date']).days >= 6:
            all_groupings = self.grouping_client.get_all_groupings()
            return self.generate_new_dates(all_groupings)
        # current date + days until next monday
        new_dates_date = now+timedelta(days=(7-now.weekday()))
        return ("Oops, it's not time for new dates yet! New dates "
                "will be available on {} 👀.").format(datetime.strftime(
                    new_dates_date,
                    "%A, %B %d, %Y"))

    def generate_response(self, data):
        msg = " ".join(data['text'].split(" ")[1:]).lower()
        print(msg)
        if msg == CURRENT_DATES_COMMAND:
            return self.handle_current_dates_command()
        if msg == NEW_DATES_COMMAND:
            return self.handle_new_dates_command()
        if msg == YOU_UP_COMMAND:
            return "😏"
        if msg == HELP_COMMAND:
            return ("Usage:\n\n"
                    "@{0} current dates --> see the current dates.\n"
                    "@{0} new dates --> get new dates (once a week) 🥳.\n"
                    "@{0} help --> get info on how to invoke bot 🤖.").format(BOT_NAME)
