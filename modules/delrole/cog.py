from discord.ext import commands
from discord import option
import configparser
import discord
from discord import default_permissions
config = configparser.ConfigParser(allow_no_value=True)
config.read('database.ini')




  


class deleterole(commands.Cog, name="Deleterole"):
  """Delete a role"""

  def __init__(self, bot: commands.Bot):
    self.bot = bot
  
  @commands.slash_command(description="Delete a role.")
  @default_permissions(manage_roles=True)
  @commands.guild_only()
  @option("name", description="Name of the role.")
  async def delrole(self, ctx, role: discord.Option(discord.Role)):
   config.read('database.ini')
   if config[str(ctx.guild.id)]["addrole"] == "False":
     embed = embed=discord.Embed(description="<:dabloonError:1047471668064428032> The delrole command is disabled in this server.", color=0xff0000)
     return await ctx.respond(embed=embed, ephemeral=True)
   else:
    if config[str(ctx.guild.id)]["manager"] == "False":
      embed = embed=discord.Embed(description="<:dabloonError:1047471668064428032> The manager module is disabled in this server.", color=0xff0000)
      return await ctx.respond(embed=embed, ephemeral=True)
    else:
     try:
         role = await role.delete()
         embed=discord.Embed(description=f"<:dabloonSucces:1047473138943934474> Deleted role", color=0xf5b60a)
         return await ctx.respond(embed=embed)
     except:
        embed=discord.Embed(description="<:dabloonError:1047471668064428032> The command failed.", color=0xff0000)
        return await ctx.respond(embed=embed, ephemeral=True)


def setup(bot: commands.Bot):
  
  bot.add_cog(deleterole(bot))