import random

from injector import inject

import tweepy
from tweepy.api import API

from ..constants.commands import TRUMPME_COMMAND, TWITTER_SEARCH_COMMAND


class TweetsHandler:
    @inject
    def __init__(self, api_client: API):
        self.api_client = api_client

    def _get_full_tweet_text(self, status):
        ''' expecting status object '''
        if hasattr(status, "retweeted_status"):  # Check if Retweet
            try:
                return status.retweeted_status.extended_tweet["full_text"]
            except AttributeError:
                if hasattr(status, "full_text"):
                    return status.retweeted_status.full_text
                else:
                    return status.retweeted_status.text
        else:
            try:
                return status.full_text
            except AttributeError:
                return status.text

    def get_random_tweet_from_user_timeline(self, user_id):
        timeline_statuses = self.api_client.user_timeline(user_id, tweet_mode='extended')
        random_idx = random.randrange(0, len(timeline_statuses), 1)
        status = timeline_statuses[random_idx]
        return self._get_full_tweet_text(status)

    def trump_me_brother(self):
        ''' RIP drake and josh ; Not sure if user id changes, but fewer API calls by just using user id? '''
        # trump_username = "realDonaldTrump"
        trump_userid = 25073877
        return self.get_random_tweet_from_user_timeline(trump_userid)

    def get_random_tweet_with_query(self, query):
        MAX_TWEETS = 10
        searched_tweets = [status for status in tweepy.Cursor(self.api_client.search, q=query).items(MAX_TWEETS)]
        random_idx = random.randrange(0, MAX_TWEETS, 1)
        status = searched_tweets[random_idx]
        return self._get_full_tweet_text(status)

    def generate_response(self, message_struct):
        command = message_struct.tokens.get("cmd")
        query = message_struct.tokens.get("cmd_args")
        if command == TRUMPME_COMMAND:
            return self.trump_me_brother()
        if command == TWITTER_SEARCH_COMMAND:
            if len(query) == 0:
                raise Exception("@{} wyd — you can't query with an empty string!".format(message_struct.sender_name))
            return self.get_random_tweet_with_query(query)