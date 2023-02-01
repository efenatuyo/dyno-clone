from discord.ext import commands
from discord import option
import configparser
import discord
from discord import default_permissions
config = configparser.ConfigParser(allow_no_value=True)
config.read('database.ini')




  


class name(commands.Cog, name="name"):
  """note"""

  def __init__(self, bot: commands.Bot):
    self.bot = bot
  
  


def setup(bot: commands.Bot):
  
  bot.add_cog(name(bot))