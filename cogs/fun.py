import discord
from discord.ext import commands
from discord import app_commands

class FunCommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.__class__.__name__} cog has been loaded')

    @app_commands.command(name="hi", description="Say hello!")
    async def hi(self, ctx: discord.Interaction):
        await ctx.response.send_message(f'hello {ctx.user.mention}!')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if 'owo' in message.content.lower():
            await message.channel.send("What's This?")

async def setup(bot):
    await bot.add_cog(FunCommands(bot))
