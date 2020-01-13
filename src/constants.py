import os
from src.utils.utils import format_data_filename

# POSSIBLE BOT COMMANDS
CURRENT_DATES_COMMAND = "current dates"
NEW_DATES_COMMAND = "new dates"
HELP_COMMAND = "help"

GROUP_SIZE = 2

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
