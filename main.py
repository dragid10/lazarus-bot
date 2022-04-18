import discord
from discord import SlashCommand
from discord.ext import commands

from util import logger, config

# Add loguru logger to all modules
logger = logger.get_logger()
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix="/keepalive ", enable_debug_events=True)
slash = SlashCommand(bot, sync_commands=True)

# @bot.event
# async def on_socket_event_type(event_type):
#     ic(type(event_type))
#     logger.debug(event_type)
#
#
# @bot.event
# async def on_socket_raw_receive(msg):
#     ic(type(msg))
#     logger.debug(msg)
#
#
# @bot.event
# async def on_socket_raw_send(payload):
#     ic(type(payload))
#     logger.debug(payload)

if __name__ == '__main__':
    bot.load_extension("cogs.keepalivecog")
    bot.run(config.bot_token, reconnect=True)
