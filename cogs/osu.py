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
        print(f"{self.__class__.__name__} cog has been loaded")

    @app_commands.command(name="stats", description="Fetch osu! player's stats")
    @app_commands.describe(
        gamemode="Valid parameters are std, taiko, ctb, and mania. Typing anything else or leaving this blank will default to standard mode."
    )
    async def stats(self, ctx: discord.Interaction, username: str, gamemode: str = ""):
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
            if user.is_deleted or user.is_restricted:
                raise Exception
            if user.rank_history.data[-1] == 0:
                raise AttributeError
            pp_count = user.statistics.pp
            response = f"Name: {user.username} \nCurrent rank in {gamemode_str}: #{user.rank_history.data[-1]} \nPerformance Points: {pp_count}"
            await ctx.response.send_message(response)
        except AttributeError:
            await ctx.response.send_message(
                f"User {username} has no recent plays in {gamemode_str} mode!"
            )
        except Exception:
            await ctx.response.send_message(f"User {username} not found! ;_; ")

    @app_commands.command(
        name="rs", description="Fetch the most recent play of the user."
    )
    @app_commands.describe()
    async def rs(self, ctx: discord.Interaction, username: str):
        try:
            user = self.api.user(username, key=UserLookupKey.USERNAME)
            recent_score = self.api.user_scores(user.id, "recent", include_fails=True)[
                0
            ]
            print(recent_score)
            score_acc = str(round(recent_score.accuracy * 100, 2)) + "%"
            # rank = recent_score.statistics.rank returns a Grade object, make parsing function
            beatmapset = recent_score.beatmapset
            artist = beatmapset.artist
            song_title = beatmapset.title
            mapset_host = beatmapset.creator
            beatmap = recent_score.beatmap
            diff_name = beatmap.version
            star_rating = beatmap.difficulty_rating
            """
            add the following:
            score
            letter grade
            mods
            stars
            GD (if there is one)
            link to mapset
            pp
            max combo
            300 count
            100 count
            50 count
            miss count
            """
            response = (
                f"Recent score for {user.username}:\n"
                f"Beatmap ID: {beatmapset.id}\n"
                f"{artist} - {song_title} [{diff_name}]\n"
                f"Mapset Host: {mapset_host}\n"
                f"Accuracy: {score_acc}\n"
                f"Difficulty: {star_rating}\n"
            )
            await ctx.response.send_message(response)
        except IndexError:
            # specify the mode
            await ctx.response.send_message(
                f"User {user.username} has no recent plays!"
            )


async def setup(bot):
    api = bot.api
    await bot.add_cog(OsuCommands(bot, api))
