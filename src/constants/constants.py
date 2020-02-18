import os

# ----------------------------------------
#               BOT COMMANDS
# 
# NOTE: any command will be prepended with
# the a textual reference to the bot's name
# ----------------------------------------
CURRENT_DATES_COMMAND = "current dates"
NEW_DATES_COMMAND = "new dates"
HELP_COMMAND = "help"

BOT_NAME = os.getenv('BOT_NAME')

GROUP_SIZE = 2

# RIP Cooper Wright :(
MEMBERS = [
    "Alex Otto",
    "Braden Dvorak",
    "Bree Hurt",
    "Cheyenne Gerlach",
    "Connor Eksi",
    "Dylan Mathers",
    "Emily Johnson",
    "Frances Munro",
    "Gauri Ramesh",
    "Gitau Wambugu",
    "Greg Tracey",
    "Hannah O'Neill",
    "Jacob Shiohira",
    "Jayden Garrett",
    "Jess Moore",
    "Lauryn Wengert",
    "Liam Carroll",
    "Lukas Hall",
    "Mary Greufe",
    "Nate Netz",
    "Olivia Maras",
    "Olivia Miller",
    "Philip Holubeck",
    "Spencer Hosch",
    "Spencer Jones",
    "Vinny Malene"
]

NEW_DATES_DAY = 0 # Monday

GROUPME_BOT_ID = os.getenv('GROUPME_BOT_ID')
PYMONGO_DB_NAME = os.getenv('PYMONGO_DB_NAME')
PYMONGO_HOSTNAME = os.getenv('PYMONGO_HOSTNAME')
PYMONGO_USERNAME = os.getenv('PYMONGO_USERNAME')
PYMONGO_PASSWORD = os.getenv('PYMONGO_PASSWORD')
PYMONGO_GRAPH_COLLECTION = os.getenv('PYMONGO_GRAPH_COLLECTION')
PYMONGO_GROUPING_COLLECTION = os.getenv('PYMONGO_GROUPING_COLLECTION')

if os.getenv('ENV') is None or os.getenv('ENV') == 'DEV':
    try:
        from .dev_constants import * 
    except Exception as e:
        raise Exception("Detected development environment, but failed to load constants from dev_constants.")
