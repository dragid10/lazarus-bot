from discord.ext import commands
from discord.ext.commands import Context
from discord_slash import cog_ext

from util import logger
from util.helper import is_thread

logger = logger.get_logger()


class KeepaliveCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._keepalive: bool = False
        self.server_id: int = None

    @commands.Cog.listener()
    async def on_ready(self):
        logger.debug(f"We have logged in as {self.bot.user}")

    @commands.Cog.listener()
    async def on_thread_update(self, pre_payload, post_payload):
        logger.debug("A THREAD WAS ARCHIVED")

    @cog_ext.cog_slash(name="ping", description="Checks if the bot is currently up. Will respond `pong` if the bot is alive")
    async def ping(self, ctx: Context):
        await ctx.reply("pong!")
        await ctx.send("pong!")
        await ctx.respond("pong!")

    @commands.group(name="keepalive",
                    description="Ensure a thread doesn't archive or continually revives it, if it does become archived",
                    default_permission=True,
                    pass_context=True)
    async def keepalive(self, ctx: Context):
        pass

    @keepalive.command()
    async def on(self, ctx: Context):
        msg_source = ctx.channel

        # If the msg comes from a source that isn't a thread, send an error reply
        if not is_thread(msg_source):
            await ctx.respond(f"Please execute the `keepalive` command from a thread!")
            return
        self._keepalive = True
        await ctx.respond("I'll make sure this thread stays alive! 🙂")

    @keepalive.command()
    async def off(self, ctx: Context):
        msg_source = ctx.channel

        # If the msg comes from a source that isn't a thread, send an error reply
        if not is_thread(msg_source):
            await ctx.respond(f"Please execute the `keepalive` command from a thread!")
            return
        self._keepalive = False
        await ctx.respond("I'll no longer keep this thread alive")


def setup(bot):
    bot.add_cog(KeepaliveCog(bot))
