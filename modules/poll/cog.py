from discord.ext import commands
from discord import option
import configparser
import discord
from discord import default_permissions#
import requests
config = configparser.ConfigParser(allow_no_value=True)
config.read('database.ini')




  


class poll_create(commands.Cog, name="Poll_create"):
  """create a Poll"""

  def __init__(self, bot: commands.Bot):
    self.bot = bot
  
  @commands.slash_command(description="Create a poll.")
  @commands.guild_only()
  @option("message", description="Message.")
  @option("choice1", description="choice1.")
  @option("choice2", description="choice2.")
  @option("choice3", description="choice3.", required=False)
  @option("choice4", description="choice4.", required=False)
  @option("choice5", description="choice5.", required=False)
  @option("choice6", description="choice6.", required=False)
  @option("choice7", description="choice7.", required=False)
  @option("choice8", description="choice8.", required=False)
  @option("choice9", description="choice9.", required=False)
  @option("choice10", description="choice10.", required=False)
  async def poll_create(self, ctx, message: str, choice1: str, choice2: str, choice3: str, choice4: str, choice5: str, choice6: str, choice7: str, choice8: str, choice9: str, choice10: str):
   config.read('database.ini')
   if config[str(ctx.guild.id)]["poll"] == "False":
     embed = embed=discord.Embed(description="<:dabloonError:1047471668064428032> The poll command is disabled in this server.", color=0xff0000)
     return await ctx.respond(embed=embed, ephemeral=True)
   else:
    if config[str(ctx.guild.id)]["fun"] == "False":
      embed = embed=discord.Embed(description="<:dabloonError:1047471668064428032> The fun module is disabled in this server.", color=0xff0000)
      return await ctx.respond(embed=embed, ephemeral=True)
    else:
      try:
        async def quick(ctx):
         embed=discord.Embed(description=f"<:dabloonSucces:1047473138943934474> Poll created.", color=0xf5b60a)
         await ctx.respond(embed=embed, ephemeral=True)
        options = [choice1, choice2]
        if choice3 is not None:
          options.append(choice3)
        if choice4 is not None:
          options.append(choice4)
        if choice5 is not None:
          options.append(choice5)
        if choice6 is not None:
          options.append(choice6)
        if choice7 is not None:
          options.append(choice7)
        if choice8 is not None:
          options.append(choice8)
        if choice9 is not None:
          options.append(choice9)
        if choice10 is not None:
          options.append(choice10)
        reactions = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟']
        description = []
        for x, option in enumerate(options):
            description += '\n\n {} {}'.format(reactions[x], option)
        embed = discord.Embed(title=message, description=''.join(description), color=0xf5b60a)
        embed.set_footer(text=f"Poll by {ctx.author.name}#{ctx.author.discriminator}")
        react_message = await ctx.send(embed=embed)
        await quick(ctx)
        for reaction in reactions[:len(options)]:
            await react_message.add_reaction(reaction)
        embed.set_footer(text=f'Poll created by {ctx.author.name}#{ctx.author.discriminator}\nPoll ID: {react_message.id}')
        await react_message.edit(embed=embed)

      except Exception as e:
        print(e)
        embed=discord.Embed(description="<:dabloonError:1047471668064428032> The command failed.", color=0xff0000)
        return await ctx.respond(embed=embed, ephemeral=True)



  


def setup(bot: commands.Bot):
  
  bot.add_cog(poll_create(bot))