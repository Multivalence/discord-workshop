import discord
from discord.ext import commands

class Basics(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="hello", description="says hello", aliases=["h"])
    async def hello(self, ctx):
        await ctx.send("Hello!")

    @commands.command(name="say", description="says whatever you want it to", aliases=["s"])
    async def say(self, ctx, *, text: str):
        await ctx.send(text)


    @commands.command(name="bettersay", description="says whatever you want it to in a certain channel", aliases=["bs"])
    async def bettersay(self, ctx, channel: discord.TextChannel, text: str):
        await channel.send(text)


async def setup(bot):
    await bot.add_cog(Basics(bot))