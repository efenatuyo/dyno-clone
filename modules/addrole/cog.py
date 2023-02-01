from discord.ext import commands
from discord import option
import configparser
import discord
from discord import default_permissions
config = configparser.ConfigParser(allow_no_value=True)
config.read('database.ini')




  


class addrole(commands.Cog, name="Addrole"):
  """Adds a role"""

  def __init__(self, bot: commands.Bot):
    self.bot = bot
  
  @commands.slash_command(description="Add a new role, with optional color and hoist.")
  @default_permissions(manage_roles=True)
  @commands.guild_only()
  @option("name", description="Name of the role.")
  @option("hoist", description="Display role seperately from other roles in the member list?.", choices=["True", "False"], required=False)
  async def addrole(self, ctx, name: str, hoist: str):
   config.read('database.ini')
   if config[str(ctx.guild.id)]["addrole"] == "False":
     embed = embed=discord.Embed(description="<:dabloonError:1047471668064428032> The addrole command is disabled in this server.", color=0xff0000)
     return await ctx.respond(embed=embed, ephemeral=True)
   else:
    if config[str(ctx.guild.id)]["manager"] == "False":
      embed = embed=discord.Embed(description="<:dabloonError:1047471668064428032> The manager module is disabled in this server.", color=0xff0000)
      return await ctx.respond(embed=embed, ephemeral=True)
    else:
     try:
       if hoist == "True":
         role = await ctx.guild.create_role(name=name, hoist=True)
         embed=discord.Embed(description=f"<:dabloonSucces:1047473138943934474> Created role {role.mention}", color=0xf5b60a)
         return await ctx.respond(embed=embed)
       else:
         role = await ctx.guild.create_role(name=name, hoist=False)
         embed=discord.Embed(description=f"<:dabloonSucces:1047473138943934474> Created role {role.mention}", color=0xf5b60a)
         return await ctx.respond(embed=embed)
     except:
        embed=discord.Embed(description="<:dabloonError:1047471668064428032> The command failed.", color=0xff0000)
        return await ctx.respond(embed=embed, ephemeral=True)


def setup(bot: commands.Bot):
  
  bot.add_cog(addrole(bot))