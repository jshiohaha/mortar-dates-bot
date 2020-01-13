import os
import json

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

from src.main import generate_response

# print(generate_response({
#     'text': '@mortarbot help'
# }))
app = Flask(__name__)

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
    if should_generate_response(data):
        response = generate_response(data)
        if response is not None:
            send_message(response)

    return "OK", 200
