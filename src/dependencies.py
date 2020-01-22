from injector import singleton

from .store.clients import PyMongoClient, GraphMongoClient, GroupingMongoClient
from .response_generator import ResponseGenerator

def configure(binder):
    binder.bind(ResponseGenerator, to=ResponseGenerator, scope=singleton)
    binder.bind(PyMongoClient, to=GraphMongoClient, scope=singleton)
    binder.bind(PyMongoClient, to=GroupingMongoClient, scope=singleton)