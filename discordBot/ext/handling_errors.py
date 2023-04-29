import discord
from discord.ext import commands
import sys
import traceback


# async def cog_command_error(ctx, error)

class Errors(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        # Get original attribute of error
        error = getattr(error, "original", error)

        if isinstance(error, discord.Forbidden):
            return
        elif isinstance(error, discord.HTTPException):
            return

        elif isinstance(error, commands.errors.NotOwner):
            return

        elif isinstance(error, commands.errors.CommandNotFound):
            return

        else:
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


#Setup
async def setup(bot):
    await bot.add_cog(Errors(bot))