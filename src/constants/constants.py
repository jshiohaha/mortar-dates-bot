import os

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

TWITTER_KEY = os.getenv('TWITTER_KEY')
TWITTER_SECRET = os.getenv('TWITTER_SECRET')

RANDOM_RESPONSES = [
    "Hmm... Someone invoked me, but I don't know how to respond!",
    "I heard Emily Johnson pref'd Innocents.",
    "How is Alex Otto not a TikTok star yet? That renegade fire.",
    "I don't know what you want me to say to that, but I promise I'm real!",
    "Free will doesn't exist. Debate.",
    "Iggy's this Wednesday? I'm there if you are.",
    "Bruh, I don't understand that.",
    "Do you like dogs? I like dogs. We should be friends.",
    "Bacon ipsum dolor amet strip steak occaecat ad shoulder, reprehenderit turkey hamburger adipisicing ham.",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur tempor.",
    "哈哈，你们大家听不懂我。",
    "Capitalize on low hanging fruit to identify a ballpark value added activity to beta test.",
    "Y'all, I wish I was as cool as Gauri!!",
    "@Liam — you up?",
    "\"How many people you bless, is how you measure your success.\" – Rick Ross",
    "\"Everyday I’m Hustlin\" – Rick Ross",
    "Mortorbot ❤️ you",
    "Did y'all hear Innocents lost someone to ODK? Spicy!",
    "What's the tea lately? I feel out of the loop",
    "Can we go to Vegas? We've practiced on O street enough at this point.",
    "Who is your mortal enemy?",
    "Who has the stir-the-pot content these days? @ing you Hannah"
]

if os.getenv('ENV') is None or os.getenv('ENV') == 'DEV':
    try:
        from .dev_constants import * 
    except Exception as e:
        raise Exception("Detected development environment, but failed to load constants from dev_constants.")
