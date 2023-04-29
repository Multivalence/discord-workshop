import discord
from discord.ext import commands

class Events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        await member.send("Bye bye")

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged in as {self.bot.user.name} | {self.bot.user.id}')

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.content == "hello":
            await message.channel.send("Hello")


async def setup(bot):
    await bot.add_cog(Events(bot))