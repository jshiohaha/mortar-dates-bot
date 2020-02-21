import random

from injector import inject

from ..constants.constants import BOT_NAME, RANDOM_RESPONSES
from ..constants.commands import DATES_COMMAND, HELP_COMMAND, TRUMPME_COMMAND, TWITTER_SEARCH_COMMAND
from .dates_handler import DatesHandler
from .tweets_handler import TweetsHandler


class Handler:
    @inject
    def __init__(self, tweets_handler: TweetsHandler, dates_handler: DatesHandler):
        self.tweets_handler = tweets_handler
        self.dates_handler = dates_handler
        return

    def generate_response(self, message_struct):
        command = message_struct.tokens.get("cmd")
        if command in [DATES_COMMAND]:
            return self.dates_handler.generate_response(message_struct)
        elif command in [TRUMPME_COMMAND, TWITTER_SEARCH_COMMAND]:
            return self.tweets_handler.generate_response(message_struct)
        elif command == HELP_COMMAND:
            return ("Usage:\n\n"
                    "@{0} dates current : see the current dates.\n"
                    "@{0} dates new : get new dates (once a week) 🥳.\n"
                    "@{0} trumpme : see a random tweet from donnie trump.\n"
                    "@{0} search <non-empy query string> : see a random tweet based on your query.\n"
                    "@{0} help : get info on how to invoke bot 🤖.").format(BOT_NAME)
        else:
            rand_idx = random.randrange(0, len(RANDOM_RESPONSES), 1)
            return RANDOM_RESPONSES[rand_idx]
