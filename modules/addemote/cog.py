from discord.ext import commands
from discord import option
import configparser
import discord
from discord import default_permissions
config = configparser.ConfigParser(allow_no_value=True)
config.read('database.ini')




  


class addemote(commands.Cog, name="Addemote"):
  """Adds an emote to the server"""

  def __init__(self, bot: commands.Bot):
    self.bot = bot
  
  @commands.slash_command(description="Adds an emote to the server.")
  @default_permissions(manage_emojis_and_stickers=True)
  @commands.guild_only()
  @option("name", description="Emote name.")
  @option("attachment", discord.Attachment, description="Image file")
  async def addemote(self, ctx, name: str, attachment: discord.Attachment):
   config.read('database.ini')
   if config[str(ctx.guild.id)]["addemote"] == "False":
     embed = embed=discord.Embed(description="<:dabloonError:1047471668064428032> The addemote command is disabled in this server.", color=0xff0000)
     return await ctx.respond(embed=embed, ephemeral=True)
   else:
    if config[str(ctx.guild.id)]["manager"] == "False":
      embed = embed=discord.Embed(description="<:dabloonError:1047471668064428032> The manager module is disabled in this server.", color=0xff0000)
      return await ctx.respond(embed=embed, ephemeral=True)
    else:
     try:
         role = await ctx.guild.create_custom_emoji(name=name, image=await attachment.read())
         embed=discord.Embed(description=f"<:dabloonSucces:1047473138943934474> Created emote named `{name}`", color=0xf5b60a)
         return await ctx.respond(embed=embed)
     except:
        print()
        embed=discord.Embed(description="<:dabloonError:1047471668064428032> The command failed.", color=0xff0000)
        return await ctx.respond(embed=embed, ephemeral=True)


def setup(bot: commands.Bot):
  
  bot.add_cog(addemote(bot))