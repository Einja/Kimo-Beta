import discord
from discord.ext import commands
from ossapi import *
import json
from pathlib import Path

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned_or("."),
            intents=discord.Intents.all(),
        )
        self.cogs_list = self.load_cogs()
        with open("config.json") as f:
            config = json.load(f)
        self.bot_token = config["bot_token"]
        self.client_id = config["client_id"]
        self.client_secret = config["client_secret"]
        self.guild_id = config["guild_id"]
        self.api = Ossapi(self.client_id, self.client_secret)

    def load_cogs(self):
        cogs = []
        cogs_dir = Path("./cogs")
        for path in cogs_dir.iterdir():
            path = path.name
            if "_" not in path:
                cogs.append(f"cogs.{path}.{path}")
        return cogs
    
    async def on_ready(self):
        print(f"Logged in as {self.user}")
        try:
            guild = discord.Object(id=self.guild_id)
            self.tree.copy_global_to(guild=guild)
            synced = await self.tree.sync(guild=guild)
            # synced = await self.tree.sync()
            print(f"Synced {len(synced)} commands")
        except Exception as e:
            print(e)

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            pass

    async def setup_hook(self):
        for ext in self.cogs_list:
            await self.load_extension(ext)


bot = Bot()
bot.run(bot.bot_token)
