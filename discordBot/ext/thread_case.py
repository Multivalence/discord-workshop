import discord
import asyncio
import time
from discord.ext import commands


def blocking():
    time.sleep(10)
    return "Slept for 10 seconds"

class ThreadCase(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # If wait param in max_concurrency is True, adds user to queue and waits
    # If wait param in max_concurrency is False, throws an error
    @commands.command()
    @commands.max_concurrency(1, commands.BucketType.user, wait=True)
    async def intensive_command(self, ctx):
        time.sleep(100)

    @commands.command()
    async def intense_command(self, ctx):
        x = asyncio.to_thread(blocking)
        await ctx.send(x)



async def setup(bot):
    await bot.add_cog(ThreadCase(bot))