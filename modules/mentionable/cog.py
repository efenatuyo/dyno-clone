from discord.ext import commands
from discord import option
import configparser
import discord
from discord import default_permissions
config = configparser.ConfigParser(allow_no_value=True)
config.read('database.ini')




  


class mentionable(commands.Cog, name="Mentionable"):
  """Toggle making a role mentionable on/off."""

  def __init__(self, bot: commands.Bot):
    self.bot = bot
  
  @commands.slash_command(description="Toggle making a role mentionable on/off.")
  @default_permissions(manage_roles=True)
  @commands.guild_only()
  async def mentionable(self, ctx, role: discord.Option(discord.Role)):
   config.read('database.ini')
   if config[str(ctx.guild.id)]["mentionable"] == "False":
     embed = embed=discord.Embed(description="<:dabloonError:1047471668064428032> The mentionable command is disabled in this server.", color=0xff0000)
     return await ctx.respond(embed=embed, ephemeral=True)
   else:
    if config[str(ctx.guild.id)]["manager"] == "False":
      embed = embed=discord.Embed(description="<:dabloonError:1047471668064428032> The manager module is disabled in this server.", color=0xff0000)
      return await ctx.respond(embed=embed, ephemeral=True)
    else:
     try:
         if role.mentionable == False:
           
          role = await role.edit(mentionable=True)
          embed=discord.Embed(description=f"<:dabloonSucces:1047473138943934474> Toggled mentionable of `{role.name}` to on", color=0xf5b60a)
          return await ctx.respond(embed=embed)
         if role.mentionable == True:
           role = await role.edit(mentionable=False)
           embed=discord.Embed(description=f"<:dabloonSucces:1047473138943934474> Toggled mentionable of`{role.name}` to off", color=0xf5b60a)
           return await ctx.respond(embed=embed)
     except:
        embed=discord.Embed(description="<:dabloonError:1047471668064428032> The command failed.", color=0xff0000)
        return await ctx.respond(embed=embed, ephemeral=True)


def setup(bot: commands.Bot):
  
  bot.add_cog(mentionable(bot))