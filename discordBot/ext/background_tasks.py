import discord
from discord.ext import commands, tasks

class Background(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.test_data = []
        self.output_data.start()

    @tasks.loop(seconds=10)
    async def output_data(self):
        channel = self.bot.guilds[0].get_channel(1101414390600835072)
        await channel.send(self.test_data)

    @output_data.before_loop
    async def output_before(self):
        await self.bot.wait_until_ready()

    @commands.command()
    async def add(self, ctx, data: str):
        self.test_data.append(data)


async def setup(bot):
    await bot.add_cog(Background(bot))