import pymongo

from datetime import datetime
import json
import os

from ..utils.utils import build_graph
from ..constants import *

#  ===========================
#          HANDLE I/O
#  ===========================

def serialize_as_json(filename, data, open_as='w'):
    with open(filename, open_as) as f:
        f.write(json.dumps(data))

def deserialize_json(filename):
    data = None
    if os.path.isfile(filename) and os.path.getsize(filename) > 0:
        with open(filename, 'r') as f:
            data = json.load(f)
    return data

def load_graph(filename):
    data = deserialize_json(filename)
    if data is None:
        return build_graph(MEMBERS)
    return data

def update_existing_groupings_file(filename, existing_data, groups):
    excluded_member = None
    for idx in range(len(groups)):
        group = groups[idx]
        if len(group) == 1:
            excluded_member = group[0]
            groups = groups[1:]
            break
    existing_data.append({
        "date": datetime.now().strftime(DATETIME_FORMAT),
        "excluded": [excluded_member],
        "groupings": groups
    })
    serialize_as_json(filename, existing_data)



class PyMongoClient:
    hostname = PYMONGO_HOSTNAME
    username = PYMONGO_USERNAME
    password = PYMONGO_PASSWORD

    def __init__(self):
        self.mongoDbUrl = "mongodb+srv://{}:{}@{}/admin".format(self.username, self.hostname, self.password)
        self.client = pymongo.MongoClient(self.mongoDbUrl)
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

    def _checkServerStatus(self):
        serverStatusResult=self.database.command("serverStatus")
        assert serverStatusResult is not None
        return serverStatusResult

class GraphMongoClient(PyMongoClient):
    databaseName = PYMONGO_DB_NAME
    collectionName = PYMONGO_GRAPH_COLLECTION

    def __init__(self):
        super().__init__()
        self._setDatabase(self.databaseName)
        self._setCollection(self.collectionName)

class GroupingsMongoClient(PyMongoClient):
    databaseName = PYMONGO_DB_NAME
    collectionName = PYMONGO_GROUPING_COLLECTION

    def __init__(self):
        super().__init__()
        self._setDatabase(self.databaseName)
        self._setCollection(self.collectionName)
