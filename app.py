from flask import Flask, request
from flask_injector import FlaskInjector
from injector import inject

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from src.constants.constants import BOT_NAME, GROUPME_BOT_ID, MOTORBOT, MORTARBOT
from src.dependencies import configure
from src.response_handlers.dates_handler import DatesHandler
from src.response_handlers.tweets_handler import TweetsHandler
from src.response_handlers.handler import Handler
from src.model.message_struct import MessageStruct

app = Flask(__name__)

def send_message(msg):
    ''' MessageStruct msg '''
    url = 'https://api.groupme.com/v3/bots/post'
    data = {
        'bot_id': GROUPME_BOT_ID,
        'text': msg
    }
    # not validating URL becauase it is fixed above, not
    # manipulatable by an external user 
    print("posting response msg: {}".format(msg))
    req = Request(url, urlencode(data).encode())
    urlopen(req).read().decode()

def should_generate_response(message_struct):
    # ignore messages sent by the bot
    if message_struct.sender_name == BOT_NAME:
        return False
    # check if message first word references bot name, ignore @ sign
    msg_first_word = message_struct.tokens.get("invocation_keyword")
    if msg_first_word[1:] != BOT_NAME:
        if msg_first_word[1:] in [MOTORBOT, MORTARBOT]:
            raise Exception("Bruh, my name is {}... NOT {}".format(BOT_NAME, msg_first_word[1:]))
        return False
    return True

@inject
@app.route('/', methods=['POST'])
def webhook(handler: Handler):
    data = request.get_json()
    message_struct = MessageStruct(data)
    response = ""
    try:
        if should_generate_response(message_struct):
            response = handler.generate_response(message_struct)
    except Exception as e:
        response = "[EXCEPTION]: {}".format(e)
        send_message(response)
    return "OK", 200

FlaskInjector(app=app, modules=[configure])