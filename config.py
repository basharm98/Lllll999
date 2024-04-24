## What's up Kangers
## Don't Kang without Creadits else I will rape your mom

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

SESSION_NAME = getenv("SESSION_NAME")

if str(getenv("STRING_SESSION2")).strip() == "":
    SESSION2 = str(None)
else:
    SESSION2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    SESSION3 = str(None)
else:
    SESSION3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    SESSION4 = str(None)
else:
    SESSION4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    SESSION5 = str(None)
else:
    SESSION5 = str(getenv("STRING_SESSION5"))

BOT_TOKEN = getenv("BOT_TOKEN", "7109448315:AAGnBrJyXVxp0uSsyEnb16IIrVSDSGpA7Eg")
BOT_NAME = getenv("BOT_NAME", "music bot")

API_ID = int(getenv("API_ID", "29246569"))
API_HASH = getenv("API_HASH", "a6a0466b72d76a8fd6814cd84b750622")
MONGO_DB_URL = getenv("MONGO_DB_URL", "mongodb+srv://Cloner:Cloner@cluster0.cgc6t.mongodb.net/?retryWrites=true&w=majority")
OWNER_NAME = getenv("OWNER_NAME", "abod")
OWNER_USERNAME = getenv("OWNER_USERNAME", "Timesisnotwaiting")
ALIVE_NAME = getenv("ALIVE_NAME", "abod")
BOT_USERNAME = getenv("BOT_USERNAME", "Msmsmsmsmsmksbot")
OWNER_ID = getenv("OWNER_ID", "6878497585")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", ".")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "TheSupportChat")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "TheUpdatesChannel")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "@H_7y4").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/5d9d0c0b7d9cb483f9867.jpg")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/5d9d0c0b7d9cb483f9867.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/basharm98/Lllll999")
PLAY_IMG = getenv("PLAY_IMG", "https://telegra.ph/file/5d9d0c0b7d9cb483f9867.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/5d9d0c0b7d9cb483f9867.jpg")
CMD_IMG = getenv("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
VIDEO_IMG = getenv("VIDEO_IMG", "https://telegra.ph/file/5d9d0c0b7d9cb483f9867.jpg")
SKIP_IMG = getenv("SKIP_IMG", "https://telegra.ph/file/5d9d0c0b7d9cb483f9867.jpg")
NEXT_IMG = getenv("NEXT_IMG", "https://telegra.ph/file/5d9d0c0b7d9cb483f9867.jpg")
HEROKU_MODE = getenv("HEROKU_MODE", None)
