from datetime import datetime
import pymongo

from ..constants.constants import PYMONGO_HOSTNAME, PYMONGO_USERNAME, PYMONGO_PASSWORD, PYMONGO_DB_NAME, PYMONGO_GRAPH_COLLECTION, PYMONGO_GROUPING_COLLECTION


class PyMongoClient:
    hostname = PYMONGO_HOSTNAME
    username = PYMONGO_USERNAME
    password = PYMONGO_PASSWORD

    def __init__(self):
        self.mongoDbUrl = ("mongodb+srv://{}:{}@{}/admin?"
                           "keepAlive=true&poolSize=30"
                           "&autoReconnect=true"
                           "&socketTimeoutMS=360000"
                           "&connectTimeoutMS=360000").format(self.username,
                                                              self.password,
                                                              self.hostname)
        self.client = pymongo.MongoClient(self.mongoDbUrl, port=27017)
        self.database = None
        self.collection = None

    def _getClient(self):
        return self.client

    def _getDatabase(self):
        return self.database

    def _setDatabase(self, database):
        self.database = self._getClient()[database]

    def _getCollection(self):
        return self.collection

    def _setCollection(self, collection):
        self.collection = self._getDatabase()[collection]


class GraphMongoClient(PyMongoClient):
    databaseName = PYMONGO_DB_NAME
    collectionName = PYMONGO_GRAPH_COLLECTION

    def __init__(self):
        super().__init__()
        self._setDatabase(self.databaseName)
        self._setCollection(self.collectionName)

    def insert_graph_instance(self, graph, date=None):
        if date is None:
            date = datetime.now()
        item = {
            'date': date,
            'graph': graph
        }
        self._getCollection().insert_one(item)

    def get_latest_graph_instance(self):
        result = self._getCollection().find().sort('date', pymongo.DESCENDING).limit(1)
        return list(result)[0]


class GroupingMongoClient(PyMongoClient):
    databaseName = PYMONGO_DB_NAME
    collectionName = PYMONGO_GROUPING_COLLECTION

    def __init__(self):
        super().__init__()
        self._setDatabase(self.databaseName)
        self._setCollection(self.collectionName)

    def insert_grouping(self, groups, excluded_member=None, date=None):
        if date is None:
            date = datetime.now()
        item = {
            "date": date,
            "excluded": [excluded_member],
            "groupings": groups
        }
        self._getCollection().insert_one(item)

    def get_all_groupings(self):
        return list(self._getCollection().find({}))

    def get_latest_grouping(self):
        query_result = self._getCollection().find().sort(
            'date', pymongo.DESCENDING).limit(1)
        return list(query_result)[0]
