import os
import json

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

app = Flask(__name__)


def send_message(msg):
    url = 'https://api.groupme.com/v3/bots/post'

    data = {
        'bot_id': os.getenv('GROUPME_BOT_ID'),
        'text': msg
    }

    request = Request(url, urlencode(data).encode())
    urlopen(request).read().decode()


@app.route('/', methods=['POST'])
def webhook():
    data = request.get_json()

    # ignore our own messages
    if data['name'] != 'mortarboard-dates-bot':
        msg = '{}, you sent "{}"'.format(data['name'], data['text'])
        send_message(msg)

    return "OK", 200