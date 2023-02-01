from discord.ext import commands
from discord import option
import configparser
import discord
from discord import default_permissions
import random
config = configparser.ConfigParser(allow_no_value=True)
config.read('database.ini')




  


class rps(commands.Cog, name="Rps"):
  """Rock, Paper and Scissors"""

  def __init__(self, bot: commands.Bot):
    self.bot = bot
  
  @commands.slash_command(description="Change the name of a role.")
  @commands.guild_only()
  @option("choice", description="Your choice.", choices=["Rock", "Paper", "Scissors"])
  async def rps(self, ctx, choice: str):
   config.read('database.ini')
   if config[str(ctx.guild.id)]["rps"] == "False":
     embed = embed=discord.Embed(description="<:dabloonError:1047471668064428032> The rps command is disabled in this server.", color=0xff0000)
     return await ctx.respond(embed=embed, ephemeral=True)
   else:
    if config[str(ctx.guild.id)]["fun"] == "False":
      embed = embed=discord.Embed(description="<:dabloonError:1047471668064428032> The fun module is disabled in this server.", color=0xff0000)
      return await ctx.respond(embed=embed, ephemeral=True)
    else:
     try:
         botchoice = random.choice(["Rock", "Paper", "Scissors"])
         if botchoice == choice:
          return await ctx.respond(f"You chose ***{choice}***.\nI choose ***{botchoice}***.\nIt's a tie! Please choose another.")
         if botchoice == "Rock" and choice == "Paper":
          return await ctx.respond(f"You chose ***{choice}***.\nI choose ***{botchoice}***.\nPaper wins!")
         if botchoice == "Rock" and choice == "Scissors":
          return await ctx.respond(f"You chose ***{choice}***.\nI choose ***{botchoice}***.\nRock wins!")
         if botchoice == "Paper" and choice == "Rock":
          return await ctx.respond(f"You chose ***{choice}***.\nI choose ***{botchoice}***.\nPaper wins!")
         if botchoice == "Paper" and choice == "Scissors":
          return await ctx.respond(f"You chose ***{choice}***.\nI choose ***{botchoice}***.\nScissors wins!")
         if botchoice == "Scissors" and choice == "Rock":  
          return await ctx.respond(f"You chose ***{choice}***.\nI choose ***{botchoice}***.\nRock wins!")
         if botchoice == "Scissors" and choice == "Paper":  
          return await ctx.respond(f"You chose ***{choice}***.\nI choose ***{botchoice}***.\nScissors wins!")
     except:
        embed=discord.Embed(description="<:dabloonError:1047471668064428032> The command failed.", color=0xff0000)
        return await ctx.respond(embed=embed, ephemeral=True)
  


def setup(bot: commands.Bot):
  
  bot.add_cog(rps(bot))