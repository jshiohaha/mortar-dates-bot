from injector import singleton

import tweepy

from .constants.constants import TWITTER_KEY, TWITTER_SECRET

from tweepy.api import API
from tweepy.auth import AppAuthHandler

from .store.clients import PyMongoClient, GraphMongoClient, GroupingMongoClient
from .response_handlers.dates_handler import DatesHandler
from .response_handlers.tweets_handler import TweetsHandler
from .response_handlers.handler import Handler


def configure(binder):
    binder.bind(DatesHandler, to=DatesHandler, scope=singleton)
    binder.bind(PyMongoClient, to=GraphMongoClient, scope=singleton)
    binder.bind(PyMongoClient, to=GroupingMongoClient, scope=singleton)

    twitter_auth_client = tweepy.AppAuthHandler(TWITTER_KEY, TWITTER_SECRET)
    binder.bind(AppAuthHandler, to=twitter_auth_client, scope=singleton)

    twitter_api_client = tweepy.API(twitter_auth_client)
    binder.bind(API, to=twitter_api_client, scope=singleton)

    binder.bind(TweetsHandler, to=TweetsHandler, scope=singleton)
    binder.bind(Handler, to=Handler, scope=singleton)
