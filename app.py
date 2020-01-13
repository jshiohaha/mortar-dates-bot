import os
import json
import pymongo

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

from src.main import generate_response
from src.constants import PYMONGO_DB_NAME, PYMONGO_HOSTNAME, PYMONGO_USERNAME, PYMONGO_PASSWORD, PYMONGO_GRAPH_COLLECTION, PYMONGO_GROUPING_COLLECTION 

# print(generate_response({
#     'text': '@mortarbot new dates'
# }))

app = Flask(__name__)
MONGO_CLIENT = pymongo.MongoClient("mongodb+srv://{}:{}@{}/".format(PYMONGO_USERNAME, PYMONGO_PASSWORD, PYMONGO_HOSTNAME))

BOT_NAME = os.getenv('BOT_NAME')

def send_message(msg):
    url = 'https://api.groupme.com/v3/bots/post'

    data = {
        'bot_id': os.getenv('GROUPME_BOT_ID'),
        'text': msg
    }

    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()


def should_generate_response(data):
    msg_sender = data['name']
    msg = data['text']
    # ignore our own messages
    if msg_sender == BOT_NAME:
        return False
    # check if message first word references bot name, ignore @ sign
    msg_first_word = msg.split(" ")[0]
    if msg_first_word[1:] != BOT_NAME:
        return False
    return True

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    msg_sender = data['name']
    # ignore our own messages
    if msg_sender != BOT_NAME:
        db = MONGO_CLIENT[PYMONGO_DB_NAME]
        response = str(db) + "\n\n"
        response += str(db[PYMONGO_GRAPH_COLLECTION]) + "\n\n"
        response += str(db[PYMONGO_GROUPING_COLLECTION])
        send_message(response)
    # data = request.get_json()
    # if should_generate_response(data):
    #     response = generate_response(data)
    #     if response is not None:
    #         send_message(response)

    return "OK", 200
