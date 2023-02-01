from discord.ext import commands
from discord import option
import configparser
import discord
from discord import default_permissions
from typing import Union
config = configparser.ConfigParser(allow_no_value=True)
config.read('database.ini')




  


class announce(commands.Cog, name="Announce"):
  """Make the bot send an announcement"""

  def __init__(self, bot: commands.Bot):
    self.bot = bot
  
  @commands.slash_command(description="Send an announcement using this bot.")
  @default_permissions(administrator=True)
  @commands.guild_only()
  @option("message", description="Message.")
  @option("channel", Union[discord.TextChannel], description="Select the channel you want to send the announcement to")
  @option("mention", description="Mention @everyone/@here.", choices=["@everyone", "@here"], required=False)
  async def announce(self, ctx, message: str, channel: Union[discord.TextChannel], mention: str):
   config.read('database.ini')
   if config[str(ctx.guild.id)]["announce"] == "False":
     embed = embed=discord.Embed(description="<:dabloonError:1047471668064428032> The announce command is disabled in this server.", color=0xff0000)
     return await ctx.respond(embed=embed, ephemeral=True)
   else:
    if config[str(ctx.guild.id)]["manager"] == "False":
      embed = embed=discord.Embed(description="<:dabloonError:1047471668064428032> The manager module is disabled in this server.", color=0xff0000)
      return await ctx.respond(embed=embed, ephemeral=True)
    else:
     try:
         if mention == None:
           embed=discord.Embed(description=f"{message}", color=0xf5b60a)
           await channel.send(embed=embed)
         if mention == "@everyone":
           embed=discord.Embed(description=f"{message}", color=0xf5b60a)
           await channel.send("@everyone", embed=embed)
         if mention == "@here":  
           embed=discord.Embed(description=f"{message}", color=0xf5b60a)
           await channel.send("@here", embed=embed)
         embed=discord.Embed(description=f"<:dabloonSucces:1047473138943934474> Announcement sent.", color=0xf5b60a)
         return await ctx.respond(embed=embed, ephemeral=True)
     except:
        embed=discord.Embed(description=f"<:dabloonError:1047471668064428032> The command failed.", color=0xff0000)
        return await ctx.respond(embed=embed, ephemeral=True)  


def setup(bot: commands.Bot):
  
  bot.add_cog(announce(bot))