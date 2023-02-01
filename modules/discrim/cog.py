from discord.ext import commands
from discord import option
import configparser
import discord
from discord import default_permissions
config = configparser.ConfigParser(allow_no_value=True)
config.read('database.ini')



bot = discord.Bot()
  


class discrim(commands.Cog, name="Discrim"):
  """random users with the mentioned discrim"""

  def __init__(self, bot: commands.Bot):
    self.bot = bot
  
  @commands.slash_command(description="Shows users with a certain discriminator.")
  @commands.guild_only()
  @option("discrim", description="Discriminator to search for.")
  async def discrim(self, ctx, discrim: int):
   config.read('database.ini')
   if config[str(ctx.guild.id)]["discrim"] == "False":
     embed = embed=discord.Embed(description="<:dabloonError:1047471668064428032> The discrim command is disabled in this server.", color=0xff0000)
     return await ctx.respond(embed=embed, ephemeral=True)
   else:
    if config[str(ctx.guild.id)]["misc"] == "False":
      embed = embed=discord.Embed(description="<:dabloonError:1047471668064428032> The misc module is disabled in this server.", color=0xff0000)
      return await ctx.respond(embed=embed, ephemeral=True)
    else:
     try:
         if len(str(discrim)) != 4:
           embed = embed=discord.Embed(description="<:dabloonError:1047471668064428032> Please provide a valid discriminator.", color=0xff0000)
           return await ctx.respond(embed=embed, ephemeral=True)
         discrims=[]
         number=0
         for m in ctx.guild.members:
          if number == 10:
            break
          if m.discriminator == str(discrim):
            discrims.append(f"{m.name}#{m.discriminator}")
            number+=1
         if not discrims:
           embed = embed=discord.Embed(description="<:dabloonError:1047471668064428032> Couldn't find any user with this discriminator.", color=0xff0000)
           return await ctx.respond(embed=embed, ephemeral=True)  
         embed=discord.Embed(description="\n".join(discrims), color=0xf5b60a)
         return await ctx.respond(embed=embed)
          
     except Exception as e:
        print(e)
        embed=discord.Embed(description="<:dabloonError:1047471668064428032> The command failed.", color=0xff0000)
        return await ctx.respond(embed=embed, ephemeral=True)  


def setup(bot: commands.Bot):
  
  bot.add_cog(discrim(bot))