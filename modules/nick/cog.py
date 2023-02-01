from discord.ext import commands
from discord import option
import configparser
import discord
from discord import default_permissions
config = configparser.ConfigParser(allow_no_value=True)
config.read('database.ini')



 
bot = commands.Bot(intents=discord.Intents.all())
class nickname(commands.Cog, name="Nickname"):
  """Change the nickname of the bot"""

  def __init__(self, bot: commands.Bot):
    self.bot = bot
  
  @commands.slash_command(description="Change the nickname of the bot.")
  @default_permissions(manage_nicknames=True)
  @commands.guild_only()
  @option("name", description="Name to change the bots nickname to.")
  async def nick(self, ctx, name: str):
   config.read('database.ini')
   if config[str(ctx.guild.id)]["nick"] == "False":
     embed = embed=discord.Embed(description="<:dabloonError:1047471668064428032> The nick command is disabled in this server.", color=0xff0000)
     return await ctx.respond(embed=embed, ephemeral=True)
   else:
    if config[str(ctx.guild.id)]["manager"] == "False":
      embed = embed=discord.Embed(description="<:dabloonError:1047471668064428032> The manager module is disabled in this server.", color=0xff0000)
      return await ctx.respond(embed=embed, ephemeral=True)
    else:
     try:
         user = ctx.guild.get_member(1046723699887325194)
         await user.edit(nick=name)
         embed=discord.Embed(description=f"<:dabloonSucces:1047473138943934474> Renamed bot to `{name}`", color=0xf5b60a)
         return await ctx.respond(embed=embed)
     except Exception as e:
        print(e)
        embed=discord.Embed(description="<:dabloonError:1047471668064428032> The command failed.", color=0xff0000)
        return await ctx.respond(embed=embed, ephemeral=True)


def setup(bot: commands.Bot):
  
  bot.add_cog(nickname(bot))
