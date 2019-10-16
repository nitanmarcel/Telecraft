import logging
import asyncio
import os
from telethon import TelegramClient
from mcpi.minecraft import Minecraft
from .version import __version__

# Logger setup
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO)

LOGGER = logging.getLogger(__name__)

# Reading environment variables
try:
    API_ID = os.environ["API_ID"]
    API_HASH = os.environ["API_HASH"]
    CHAT = os.environ["TG_CHAT"] # The telegram chat to connect to
except KeyError as e:
    quit(e.args[0] + ' missing from environment variables')


# Create Telegram client

client = TelegramClient('telecraft', API_ID, API_HASH, app_version=__version__)
loop = asyncio.get_event_loop()

# Create connection to the Minecraft server
mc = Minecraft.create()