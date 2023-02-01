from discord.ext import commands
from discord import option
import configparser
import discord
from typing import Union
from discord import default_permissions
config = configparser.ConfigParser(allow_no_value=True)
config.read('database.ini')




  


class avatar(commands.Cog, name="Avatar"):
  """Get the avatar of a user"""

  def __init__(self, bot: commands.Bot):
    self.bot = bot
  
  @commands.slash_command(description="Get the avatar of a user.")
  @commands.guild_only()
  @option("user", Union[discord.Member], description="The user to get it from.", required=False)
  async def avatar(self, ctx, user: Union[discord.Member]):
   config.read('database.ini')
   if config[str(ctx.guild.id)]["avatar"] == "False":
     embed = embed=discord.Embed(description="<:dabloonError:1047471668064428032> The avatar command is disabled in this server.", color=0xff0000)
     return await ctx.respond(embed=embed, ephemeral=True)
   else:
    if config[str(ctx.guild.id)]["misc"] == "False":
      embed = embed=discord.Embed(description="<:dabloonError:1047471668064428032> The misc module is disabled in this server.", color=0xff0000)
      return await ctx.respond(embed=embed, ephemeral=True)
    else:
      try:
        if user == None:
         try:
          embed=discord.Embed(title=f"{ctx.author.name}#{ctx.author.discriminator}\n\n**Avatar**", color=0xf5b60a)
          embed.set_image(url=ctx.author.avatar.url)
          return await ctx.respond(embed=embed)
         except:
           return await ctx.respond("This user does not have any avatar")
        else:
         try:
          embed=discord.Embed(title=f"{user.name}#{user.discriminator}\n\n**Avatar**",  color=0xf5b60a)
          embed.set_image(url=user.avatar.url)
          return await ctx.respond(embed=embed)
         except:
          return await ctx.respond("This user does not have any avatar")
      except Exception as e:
         print(e)
         embed=discord.Embed(description="<:dabloonError:1047471668064428032> The command failed.", color=0xff0000)
         return await ctx.respond(embed=embed, ephemeral=True)   


def setup(bot: commands.Bot):
  
  bot.add_cog(avatar(bot))