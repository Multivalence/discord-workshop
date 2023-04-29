
# pip install discord.py
# or
# pip install discord.py[voice]

import discord
from discord.ext import commands


class MyBot(commands.Bot):

    def __init__(self):
        super().__init__(
            command_prefix=".",
            status=discord.Status.online,
            activity=discord.Game(name="Hacking the Pentagon"),
            intents=discord.Intents.all(),
            case_insensitive=True
        )

        self.initial_extensions = [
            'ext.basic_commands',
            'ext.advanced_commands',
            'ext.events',
            'ext.background_tasks',
            'ext.handling_errors',
            'ext.webhooks',
            'ext.async_request',
            'ext.thread_case',
        ]

    async def setup_hook(self):
        for ext in self.initial_extensions:
            await self.load_extension(ext)


bot = MyBot()
bot.run("TOKEN")