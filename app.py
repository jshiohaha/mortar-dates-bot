import os
import json

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)

BOT_NAME = '@mbdates'

def send_message(msg):
    url = 'https://api.groupme.com/v3/bots/post'

    data = {
        'bot_id': os.getenv('GROUPME_BOT_ID'),
        'text': msg
    }

    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()


def should_respond(msg):
    # check if message references bot name
    if msg.split(" ")[0] != BOT_NAME:
        return False
    return True

@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()
    message = data['text']

    if should_respond(message):
        # ignore our own messages
        if data['name'] != BOT_NAME:
            msg = '{}, you sent "{}"'.format(data['name'], message)
            send_message(msg)

    return "OK", 200