import discord
import aiohttp
from discord import Webhook
from discord.ext import commands

class Welcome(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.url = None
        self.bot.loop.create_task(self.identifyWebhook())

    async def identifyWebhook(self):

        await self.bot.wait_until_ready()

        guild = self.bot.get_guild(1101405315599192177)
        channel = guild.get_channel(1101405316119273544)
        whooks = await guild.webhooks()

        for i in whooks:
            if i.name == "Discord Workshop":
                self.url = i.url
                return


        async with aiohttp.ClientSession() as cs:
            async with cs.get(str(self.bot.user.avatar.url)) as r:
                image_bytes = await r.read()


            web = await channel.create_webhook(name="Workshop", avatar=image_bytes, reason="Welcome Messages")

            self.url = web.url
            print(self.url)
            return

    @commands.Cog.listener()
    async def on_member_join(self, member):

        if not self.url:
            return

        embed = discord.Embed(
            title="",
            description="**WELCOME!**",
            color=discord.Color.green(),
            type="rich"
        )

        embed.add_field(name="User", value=member.mention, inline=True)
        embed.set_thumbnail(url=member.avatar.url)

        async with aiohttp.ClientSession() as session:
            webhook = Webhook.from_url(self.url, session=session)
            await webhook.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Welcome(bot))