import discord
from icecream import ic

from util import logger, config

# Add loguru logger to all modules
logger = logger.get_logger()

bot = discord.Bot(command_prefix=config.bot_prefix)


@bot.event
async def on_ready():
    ic(f"We have logged in as {bot.user}")


@bot.slash_command()
async def ping(ctx):
    await ctx.respond("pong!")

if __name__ == '__main__':
    bot.run(config.bot_token)
