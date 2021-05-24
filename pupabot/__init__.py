import sys

import yaml
from loguru import logger
from motor import motor_asyncio
from pupalink import Session
from pyrogram import Client
from pyrogram.raw import functions
from pyrogram.raw.types.bot_command import BotCommand

from .service import SearchService, PupalinkService

__version__ = "0.1.0"

config = yaml.safe_load(open("config.yaml"))

try:
    API_ID = config["core"]["api_id"]
    API_HASH = config["core"]["api_hash"]
    OWNER_ID = config["core"]["owner_id"]
    BOT_TOKEN = config["core"]["bot_token"]
    IDP_SESSION = config["core"]["idp_session"]
    PROXY = config["core"]["proxy"]
    MONGODB_URL = config["core"]["mongodb_url"]
    MONGODB_DB = config["core"]["mongodb_db"]

except KeyError as e:
    logger.exception(f"One or some keys are missing {e}")
    sys.exit(1)


bot = Client("pupabot", API_ID, API_HASH, bot_token=BOT_TOKEN)
session = Session(IDP_SESSION, proxy=PROXY)
motor = motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
db = motor[MONGODB_DB]
search_service = SearchService(db)
pupa_service = PupalinkService(session)
with bot:
    bot.send(
        functions.bots.SetBotCommands(
            commands=[
                BotCommand(command="start",
                           description="Get the welcome message"),
                BotCommand(command="help",
                           description="How to use the bot"),
                BotCommand(command="info",
                           description="Get some useful information about the bot"),
                BotCommand(command="stats",
                           description="Get some statistics about the bot"),
            ]  # type: ignore
        )
    )
