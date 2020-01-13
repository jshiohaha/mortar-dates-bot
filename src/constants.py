import os
from src.utils.utils import format_data_filename

# POSSIBLE BOT COMMANDS
CURRENT_DATES_COMMAND = "current dates"
NEW_DATES_COMMAND = "new dates"
HELP_COMMAND = "help"

GROUP_SIZE = 2

DATETIME_FORMAT = "%m/%d/%Y %H:%M:%S"

MONDAY = 0

PYMONGO_DB_NAME = os.getenv('PYMONGO_DB_NAME')
PYMONGO_GRAPH_COLLECTION = os.getenv('PYMONGO_GRAPH_COLLECTION')
PYMONGO_GROUPING_COLLECTION = os.getenv('PYMONGO_GROUPING_COLLECTION')
PYMONGO_HOSTNAME = os.getenv('PYMONGO_HOSTNAME')
PYMONGO_USERNAME = os.getenv('PYMONGO_USERNAME')
PYMONGO_PASSWORD = os.getenv('PYMONGO_PASSWORD')

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

DIR_NAME = os.path.dirname(os.path.realpath(__file__))
GRAPH_FILENAME = format_data_filename(DIR_NAME, "groups.json")
WEEKLY_GROUPINGS_FILENAME = format_data_filename(DIR_NAME, "weekly_groupings.json")
