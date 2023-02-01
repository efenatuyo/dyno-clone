from discord.ext import commands
from discord import option
import configparser
import discord
from discord import default_permissions#
import requests
config = configparser.ConfigParser(allow_no_value=True)
config.read('database.ini')




  


class info(commands.Cog, name="Info"):
  """info abt the bot"""

  def __init__(self, bot: commands.Bot):
    self.bot = bot
  
  @commands.slash_command(description="Information about the bot.")
  @commands.guild_only()
  async def info(self, ctx):
      try:
        embed=discord.Embed(title="**Dabloon**", color=0xf5b60a)
        embed.add_field(name="**Version**", value="1.0.0", inline=True)
        embed.add_field(name="**Library**", value="Pycord", inline=True)
        embed.add_field(name="**Creator**", value="xolo#4942", inline=True)
        embed.add_field(name="**Invite**", value="[Click me!](https://discord.com/api/oauth2/authorize?client_id=1046723699887325194&permissions=8&scope=bot)", inline=True)
        embed.set_footer(text="©️ Dabloon")
        return await ctx.respond(embed=embed)
      except:
        embed=discord.Embed(description="<:dabloonError:1047471668064428032> The command failed.", color=0xff0000)
        return await ctx.respond(embed=embed, ephemeral=True)
  


def setup(bot: commands.Bot):
  
  bot.add_cog(info(bot))