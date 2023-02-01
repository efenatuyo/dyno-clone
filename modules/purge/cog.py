from discord.ext import commands
from discord import option
import configparser
import discord
from typing import Union
from discord import default_permissions
config = configparser.ConfigParser(allow_no_value=True)
config.read('database.ini')




  


class purge(commands.Cog, name="Purge"):
  """Purge messages"""

  def __init__(self, bot: commands.Bot):
    self.bot = bot
  
  @commands.slash_command(description="Change the name of a role.")
  @default_permissions(manage_messages=True)
  @commands.guild_only()
  @option("limit", description="Number of messages to delete.")
  @option("channel", Union[discord.TextChannel], description="Select a channel to purge messages from", required=False)
  async def purge(self, ctx, limit: int, channel: Union[discord.TextChannel]):
   config.read('database.ini')
   if config[str(ctx.guild.id)]["purge"] == "False":
     embed = embed=discord.Embed(description="<:dabloonError:1047471668064428032> The purge command is disabled in this server.", color=0xff0000)
     return await ctx.respond(embed=embed, ephemeral=True)
   else:
    if config[str(ctx.guild.id)]["manager"] == "False":
      embed = embed=discord.Embed(description="<:dabloonError:1047471668064428032> The manager module is disabled in this server.", color=0xff0000)
      return await ctx.respond(embed=embed, ephemeral=True)
    else:
     try:
         if channel == None:
           delete=await ctx.channel.purge(limit=limit)
           embed=discord.Embed(description=f"<:dabloonSucces:1047473138943934474> Succesfully purged {len(delete)} messages in `{ctx.channel.name}`", color=0xf5b60a)
           return await ctx.respond(embed=embed)
         else:
           
           delete = await channel.purge(limit=limit)
           embed=discord.Embed(description=f"<:dabloonSucces:1047473138943934474> Succesfully purged {len(delete)} messages in `{channel}`", color=0xf5b60a)
           return await ctx.respond(embed=embed)
     except:
        embed=discord.Embed(description="<:dabloonError:1047471668064428032> The command failed.", color=0xff0000)
        return await ctx.respond(embed=embed, ephemeral=True)


def setup(bot: commands.Bot):
  
  bot.add_cog(purge(bot))