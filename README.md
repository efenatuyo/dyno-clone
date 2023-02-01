# dyno-clone
unfinished clone of the discord bot Dyno


required template to create new command

main.py add into the function start setup 
```
config[str(guild.id)]["command_name"] = "True"'
```
go to modules create new file and inside of it create a file named cog.py

after that use this template

```
from discord.ext import commands
from discord import option
import configparser
import discord
from discord import default_permissions
config = configparser.ConfigParser(allow_no_value=True)
config.read('database.ini')




  


class name(commands.Cog, name="name"):
  """note"""

  def __init__(self, bot: commands.Bot):
    self.bot = bot
  
  


def setup(bot: commands.Bot):
  
  bot.add_cog(name(bot))
```

edit name of class and then bot.add_cog(name(bot))

if you want to create other modules you can create it trough the main file by just doing the same like the the command

make sure to check if the command is disabled in the server or not by doing this
```
from discord.ext import commands
from discord import option
import configparser
import discord
from discord import default_permissions
config = configparser.ConfigParser(allow_no_value=True)
config.read('database.ini')




  


class setnick(commands.Cog, name="Setnick"):
  """changes nick of user"""

  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.slash_command(description="Change the nickname of a user.")
  @default_permissions(manage_nicknames=True)
  @commands.guild_only()
  @option("nickname", description="New nickname for the user.")
  async def setnick(self, ctx, user: discord.Option(discord.Member), nickname: str):
   config.read('database.ini')
   if config[str(ctx.guild.id)]["setnick"] == "False":
     embed = embed=discord.Embed(description="<:dabloonError:1047471668064428032> The setnick command is disabled in this server.", color=0xff0000)
     return await ctx.respond(embed=embed, ephemeral=True)
   else:
    if config[str(ctx.guild.id)]["manager"] == "False":
      embed = embed=discord.Embed(description="<:dabloonError:1047471668064428032> The manager module is disabled in this server.", color=0xff0000)
      return await ctx.respond(embed=embed, ephemeral=True)
    else:
     try:
         await user.edit(nick=nickname)
         embed=discord.Embed(description=f"<:dabloonSucces:1047473138943934474> Nickname changed.", color=0xf5b60a)
         return await ctx.respond(embed=embed)
     except:
        embed=discord.Embed(description=f"<:dabloonError:1047471668064428032> Unable to change nickname for {user.mention}.", color=0xff0000)
        return await ctx.respond(embed=embed, ephemeral=True)

       
def setup(bot: commands.Bot):
  
  bot.add_cog(setnick(bot))
```
