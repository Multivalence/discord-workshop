import discord
import typing
from discord.ext import commands


async def is_correct_channel(ctx):
    return ctx.channel.name == "general"


class Advanced(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.guild_only()
    @commands.command(name="hello2", description="says hello", aliases=["h2"])
    async def hello2(self, ctx):
        await ctx.send("Hello!")

    @commands.is_owner()
    @commands.command(name="say2", description="says whatever you want it to", aliases=["s2"])
    async def say2(self, ctx, text: str):
        await ctx.send(text)

    # @commands.has_permissions(administrator=True)
    @commands.has_role("Admin")
    @commands.command(name="give", description="gives a role to user", aliases=["g"])
    async def give(self, ctx, role: discord.Role):
        await ctx.author.add_roles(role)
        await ctx.reply("Successfully gave role")

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def cooldown(self, ctx):
        await ctx.send("Test")

    @commands.command()
    @commands.check(is_correct_channel)
    async def customcheck(self, ctx):
        await ctx.send("success")

    # Allows any of the given params
    @commands.command()
    async def union(self, ctx, what: typing.Union[discord.TextChannel, discord.Member]):
        await ctx.send(what)

    @commands.command()
    async def bottles(self, ctx, amount: typing.Optional[int] = 99, *, liquid="milk"):
        await ctx.send(f"{amount} bottles of {liquid} on the wall!")

    @commands.command()
    async def shop(self, ctx, buy_sell: typing.Literal['buy', 'sell'], amount: typing.Literal[1, 2], *, item: str):
        await ctx.send(f'{buy_sell.capitalize()}ing {amount} {item}(s)!')

    @commands.command()
    async def slap(self, ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
        slapped = ", ".join(x.name for x in members)
        await ctx.send(f'{slapped} just got slapped for {reason}')

    @commands.command()
    async def upload(self, ctx, attachment: typing.Optional[discord.Attachment]):
        if attachment is None:
            await ctx.send('You did not upload anything!')
        else:
            await ctx.send(f'You have uploaded <{attachment.url}>')


async def setup(bot):
    await bot.add_cog(Advanced(bot))