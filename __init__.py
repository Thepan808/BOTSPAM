from userbot import *
from userbot.Config import Config
from telethon import TelegramClient
from decouple import config
import logging
import time
from os import getenv


APP_ID = config("APP_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
BOT_TOKEN2 = config("BOT_TOKEN2", default=None)
BOT_TOKEN3 = config("BOT_TOKEN3", default=None)
BOT_TOKEN4 = config("BOT_TOKEN4", default=None)
BOT_TOKEN5 = config("BOT_TOKEN5", default=None)
BOT_TOKEN6 = config("BOT_TOKEN6", default=None)
BOT_TOKEN7 = config("BOT_TOKEN7", default=None)
BOT_TOKEN8 = config("BOT_TOKEN8", default=None)
BOT_TOKEN9 = config("BOT_TOKEN9", default=None)
BOT_TOKEN10 = config("BOT_TOKEN10", default=None)




bot2 = TelegramClient('UstaD2', APP_ID, API_HASH).start(bot_token=BOT_TOKEN2) 

bot3 = TelegramClient('UstaD3', APP_ID, API_HASH).start(bot_token=BOT_TOKEN3) 

bot4 = TelegramClient('UstaD4', APP_ID, API_HASH).start(bot_token=BOT_TOKEN4) 

bot5 = TelegramClient('UstaD5', APP_ID, API_HASH).start(bot_token=BOT_TOKEN5) 

bot6 = TelegramClient('UstaD6', APP_ID, API_HASH).start(bot_token=BOT_TOKEN6) 

bot7 = TelegramClient('UstaD7', APP_ID, API_HASH).start(bot_token=BOT_TOKEN7) 

bot8 = TelegramClient('UstaD8', APP_ID, API_HASH).start(bot_token=BOT_TOKEN8) 

bot9 = TelegramClient('UstaD9', APP_ID, API_HASH).start(bot_token=BOT_TOKEN9) 

bot10 = TelegramClient('UstaD10', APP_ID, API_HASH).start(bot_token=BOT_TOKEN10) 

tgbot = LegendBot
