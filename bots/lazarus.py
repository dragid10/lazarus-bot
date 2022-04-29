import discord

from db.redis_db import RedisDB
from util import logger, config
from util.helper import is_thread, thread_archive_event

# Add loguru logger to all modules
logger = logger.get_logger()

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Bot(intents=intents, enable_debug_events=True)
# db = InMemoryDB()
db = RedisDB()


@bot.event
async def on_ready():
    logger.info(f"We have logged in as {bot.user}")


@bot.event
async def on_thread_update(pre_payload, post_payload):
    # Check if this event is a thread archival event before doing anything
    if thread_archive_event(pre_payload, post_payload):
        server_id = post_payload.guild.id.__str__()
        thread_id = post_payload.id.__str__()

        # Immediately unarchive thread if its in our watchlist
        if db.thread_in_watchlist(thread_id, server_id):
            await post_payload.unarchive()
            await bot.get_channel(post_payload.id).send(f"I've resurrected this thread (use `/keeepalive-off` if you'd like me to stop)")


@bot.slash_command(name="ping", description="Checks if the bot is currently up. Will respond `pong` if the bot is alive")
async def ping(ctx):
    await ctx.respond("pong!")


@bot.slash_command(name="keepalive-on",
                   description="Toggle on thread revival service",
                   default_permission=True)
async def keepalive_on(ctx):
    msg_source = ctx.channel
    server_id = ctx.guild_id.__str__()
    thread_id = msg_source.id.__str__()

    #  If the msg comes from a source that isn't a thread, send an error reply
    if not is_thread(msg_source):
        await ctx.respond(
            f"Please execute the `keepalive` command from a thread, and ensure Lazarus has Read/Write permissions in that thread")
        return

    # If the thread is being monitored, send a response
    if db.thread_in_watchlist(thread_id, server_id):
        await ctx.respond(f"This thread is already being monitored!")
        return

    # Add the thread id to the watchlist
    try:
        db.add_thread_to_watchlist(thread_id, server_id)
    except Exception:
        logger.exception(f"Unable to add thread to watchlist")
        await ctx.respond(f"An error occurred trying to watch this thread. Try again later")
        return

    await ctx.send_response("I'll make sure this thread stays alive! 🙂")


@bot.slash_command(name="keepalive-off",
                   description="Toggle off thread revival service",
                   default_permission=True)
async def keepalive_off(ctx):
    msg_source = ctx.channel
    server_id = ctx.guild_id.__str__()
    thread_id = msg_source.id.__str__()

    #  If the msg comes from a source that isn't a thread, send an error reply
    if not is_thread(msg_source):
        await ctx.respond(
            f"Please execute the `keepalive` command from a thread, and ensure Lazarus has Read/Write permissions in that thread")
        return

    # If the thread is not being monitored, send a response
    if not db.thread_in_watchlist(thread_id, server_id):
        await ctx.respond(f"This thread wasn't being monitored")
        return

    # Remove the thread id from the watchlist
    try:
        db.remove_thread_from_watchlist(thread_id, server_id)

    except Exception:
        logger.exception(f"Unable to remove thread from watchlist")
        await ctx.respond(f"An error occurred trying to unwatch this thread. Try again later")
        return

    await ctx.send_response("I'll no longer monitor this thread! 😵")


def run():
    bot.run(config.bot_token, reconnect=True)
