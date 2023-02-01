from discord.ext import commands
from discord import option
import configparser
import discord
from discord import default_permissions
config = configparser.ConfigParser(allow_no_value=True)
config.read('database.ini')




  


class afk(commands.Cog, name="Afk"):
  """set afk"""

  def __init__(self, bot: commands.Bot):
    self.bot = bot
  
  @commands.slash_command(description="Set yourself afk.")
  @option("reason", description="Message.")
  async def afk(self, ctx, reason: str):
   config.read('database.ini')
   if config[str(ctx.guild.id)]["afk"] == "False":
     embed = embed=discord.Embed(description="<:dabloonError:1047471668064428032> The afk command is disabled in this server.", color=0xff0000)
     return await ctx.respond(embed=embed, ephemeral=True)
   else:
    if config[str(ctx.guild.id)]["misc"] == "False":
      embed = embed=discord.Embed(description="<:dabloonError:1047471668064428032> The misc module is disabled in this server.", color=0xff0000)
      return await ctx.respond(embed=embed, ephemeral=True)
    else:
     try:
         config[f"{str(ctx.guild.id)}afk"][str(ctx.author.id)] = str(reason)
         with open('database.ini', 'w') as configfile:
            config.write(configfile)
         return await ctx.respond(f"{ctx.author.mention} I set your AFK: {reason}")
     except:
        embed=discord.Embed(description=f"<:dabloonError:1047471668064428032> The command failed.", color=0xff0000)
        return await ctx.respond(embed=embed, ephemeral=True)   


def setup(bot: commands.Bot):
  
  bot.add_cog(afk(bot))