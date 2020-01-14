import os

# POSSIBLE BOT COMMANDS
CURRENT_DATES_COMMAND = "current dates"
NEW_DATES_COMMAND = "new dates"
HELP_COMMAND = "help"

GROUP_SIZE = 2

DATETIME_FORMAT = "%m/%d/%Y %H:%M:%S"

MONDAY = 0

BOT_NAME = os.getenv('BOT_NAME')

PYMONGO_DB_NAME = os.getenv('PYMONGO_DB_NAME')
PYMONGO_HOSTNAME = os.getenv('PYMONGO_HOSTNAME')
PYMONGO_USERNAME = os.getenv('PYMONGO_USERNAME')
PYMONGO_PASSWORD = os.getenv('PYMONGO_PASSWORD')
PYMONGO_GRAPH_COLLECTION = os.getenv('PYMONGO_GRAPH_COLLECTION')
PYMONGO_GROUPING_COLLECTION = os.getenv('PYMONGO_GROUPING_COLLECTION')

MEMBERS = [
    "Alex Otto",
    "Braden Dvorak",
    "Bree Hurt",
    "Cheyenne Gerlach",
    "Connor Eksi",
    "Cooper Wright",
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
