import discord
import aiohttp
from discord.ext import commands, tasks

class Req(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.data_countries = None
        self.data_worldwide = None
        self.sendRequest.start()

    @tasks.loop(seconds=86400)
    async def sendRequest(self):
        """
        Sends request every 24 hours to static api and saves data in self.data
        """

        # return
        async with aiohttp.ClientSession() as session:
            async with session.get("https://corona.lmao.ninja/v2/all") as resp:
                self.data_worldwide = await resp.json()

            async with session.get("https://corona.lmao.ninja/v2/countries") as resp:
                self.data_countries = await resp.json()

    @sendRequest.before_loop
    async def before_send_request(self):
        """
         Waits for bot to be ready then starts requests loop
        """
        await self.bot.wait_until_ready()

    @commands.guild_only()
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def stats(self, ctx):

        embed = discord.Embed(
            title="COVID-19 Summary",
            description="```Worldwide```",
            colour=discord.Colour.red()
        )

        embed.add_field(name="New Confirmed", value=self.data_worldwide["todayCases"], inline=False)
        embed.add_field(name="Total Confirmed", value=self.data_worldwide["cases"], inline=False)
        embed.add_field(name="New Deaths", value=self.data_worldwide["todayDeaths"], inline=False)
        embed.add_field(name="Total Deaths", value=self.data_worldwide["deaths"], inline=False)
        embed.add_field(name="New Recovered", value=self.data_worldwide["todayRecovered"], inline=False)
        embed.add_field(name="Total Recovered", value=self.data_worldwide["recovered"], inline=False)
        embed.set_footer(text="Note: Data is not 100% Accurate!")

        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Req(bot))