from discord.ext import commands
from discord import option
import configparser
import discord
from discord import default_permissions
config = configparser.ConfigParser(allow_no_value=True)
config.read('database.ini')




  


class disablenablemodule(commands.Cog, name="Disablenablemodule"):
  """Disables or enables a module"""

  def __init__(self, bot: commands.Bot):
    self.bot = bot
  
  @commands.slash_command(description="Enable/disable a module.")
  @default_permissions(administrator=True)
  @commands.guild_only()
  @option("module", description="Module to enable/disable")
  async def module(self, ctx, command: str):
    config.read('database.ini')
    modules = ["manager", "fun", "misc", "moderator", "roles", "tags", "slowmode"]
    if command.lower() in modules:
      if config[str(ctx.guild.id)][command.lower()] == "True":
        config[str(ctx.guild.id)][command.lower()] = "False"
        with open('database.ini', 'w') as configfile:
              config.write(configfile)
        embed=discord.Embed(description=f"<:dabloonSucces:1047473138943934474> Disabled {command.lower()}.", color=0xf5b60a)
        await ctx.respond(embed=embed)
      else:
        config[str(ctx.guild.id)][command.lower()] = "True"
        with open('database.ini', 'w') as configfile:
              config.write(configfile)
        embed=discord.Embed(description=f"<:dabloonSucces:1047473138943934474> Enabled {command.lower()}.", color=0xf5b60a)
        await ctx.respond(embed=embed)
    else:
     embed=discord.Embed(description=f"<:dabloonError:1047471668064428032> I can't find the {command.lower()} module.", color=0xff0000)
     await ctx.respond(embed=embed, ephemeral=True)


def setup(bot: commands.Bot):
  
  bot.add_cog(disablenablemodule(bot))