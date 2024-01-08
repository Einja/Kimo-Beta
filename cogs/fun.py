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

    @app_commands.command(name="poke", description="Ping another user!")
    async def poke(self, ctx: discord.Interaction, user: discord.Member):
        try:
            if ctx.user == user:
                await ctx.response.send_message("Poking yourself huh...?")
            else:
                await ctx.response.send_message(f"{ctx.user.mention} poked {user.mention}!")
        except:
            await ctx.response.send_message(f"User {user.display_name} was not found in this server!")


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if 'owo' in message.content.lower():
            await message.channel.send("What's This?")

        elif 'king' in message.content.lower():
            gif_path = 'cogs/images_or_gifs/gg.gif'
            await message.channel.send(file=discord.File(gif_path))

async def setup(bot):
    await bot.add_cog(FunCommands(bot))
