import discord
from discord.ext import commands
from discord import app_commands
from ossapi import GameMode, UserLookupKey

class OsuCommands(commands.Cog):
    def __init__(self, bot, api):
        self.bot = bot
        self.api = api

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} cog has been loaded')

    @app_commands.command(name="stats", description="Fetch osu! player's stats")
    @app_commands.describe(gamemode="Valid parameters are std, taiko, ctb, and mania. Typing anything else or leaving this blank will default to standard mode.")
    async def stats(self, ctx: discord.Interaction, username: str, gamemode: str = ''):
        mode = ""
        gamemode_str = ""
        try:
            match gamemode.lower():
                case "std":
                    mode = GameMode.OSU
                    gamemode_str = "standard"
                case "taiko":
                    mode = GameMode.TAIKO
                    gamemode_str = "taiko"
                case "ctb":
                    mode = GameMode.CATCH
                    gamemode_str = "ctb"
                case "mania":
                    mode = GameMode.MANIA
                    gamemode_str = "mania"
                case _:
                    mode = GameMode.OSU
                    gamemode_str = "standard"
            user = self.api.user(username, mode=mode, key=UserLookupKey.USERNAME)
            response = f'Name: {user.username}. Current rank in {gamemode_str}: #{user.rank_history.data[-1]}'
            await ctx.response.send_message(response)
        except AttributeError:
            await ctx.response.send_message(f"User {username} has no recent plays in {gamemode_str} mode!")
        except Exception as e:
            await ctx.response.send_message(f"User {username} not found! ;_; ")

async def setup(bot):
    api = bot.api
    await bot.add_cog(OsuCommands(bot, api))
