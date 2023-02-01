
import discord
from discord import default_permissions
from discord import option
from discord.ext import commands
import configparser
import os
config = configparser.ConfigParser(allow_no_value=True)
config.read('database.ini')

bot = commands.Bot(intents=discord.Intents.all())




@bot.event
async def on_ready():
  print('bot online')
  



def startsetup(guild):
  config.read('database.ini')
  config["servers"][str(guild.id)] = None
  config[str(guild.id)] = {}
  config[f"{str(guild.id)}afk"] = {}
  config[str(guild.id)]["manager"] = "True"
  config[str(guild.id)]["fun"] = "True"
  config[str(guild.id)]["misc"] = "True"
  config[str(guild.id)]["moderator"] = "True"
  config[str(guild.id)]["information"] = "True"
  config[str(guild.id)]["roles"] = "True"
  config[str(guild.id)]["tags"] = "True"
  config[str(guild.id)]["slowmode"] = "True"
  config[str(guild.id)]["addrole"] = "True"
  config[str(guild.id)]["setnick"] = "True"
  config[str(guild.id)]["rolename"] = "True"
  config[str(guild.id)]["delrole"] = "True"
  config[str(guild.id)]["command"] = "True"
  config[str(guild.id)]["module"] = "True"
  config[str(guild.id)]["nick"] = "True"
  config[str(guild.id)]["purge"] = "True"
  config[str(guild.id)]["announce"] = "True"
  config[str(guild.id)]["mentionable"] = "True"
  config[str(guild.id)]["addemote"] = "True"
  config[str(guild.id)]["role"] = "True"
  config[str(guild.id)]["rps"] = "True"
  config[str(guild.id)]["dadjoke"] = "True"
  config[str(guild.id)]["poll"] = "True"
  config[str(guild.id)]["info"] = "True"
  config[str(guild.id)]["inviteinfo"] = "True"
  config[str(guild.id)]["afk"] = "True"
  config[str(guild.id)]["discrim"] = "True"
  
  with open('database.ini', 'w') as configfile:
            config.write(configfile)




@bot.event
async def on_guild_join(guild):
  if guild.id == 1046723699887325194:
    pass
  else:  
   if str(guild.id) in config["servers"]:
    pass
   else:
    startsetup(guild)

@bot.event
async def on_message(message:discord.Message):
 config.read('database.ini')
 try:
  if config[str(message.author.guild.id)]["afk"] == "False":
    return
  else:
    pass
  if message.author.bot == True:
     return
  else:
     pass
  try:
     if message.mentions[0] is not None:
       check = True
  except:
     check = False
  if str(message.author.id) in config[f"{str(message.author.guild.id)}afk"]:
    if config[f"{str(message.author.guild.id)}afk"][str(message.author.id)] != "False":
      config[f"{str(message.author.guild.id)}afk"][str(message.author.id)] = "False"
      with open('database.ini', 'w') as configfile:
            config.write(configfile)
      await message.reply('Removed your AFK')
  if check is True:
    id = str(message.mentions[0].id)
    if id in config[f"{str(message.author.guild.id)}afk"]:
    
     if config[f"{str(message.guild.id)}afk"][str(message.mentions[0].id)] != "False":
  
       check = config[f"{str(message.guild.id)}afk"][str(message.mentions[0].id)]
       return await message.reply(f"{message.mentions[0].mention} is AFK: {str(check)}")
     else:
         return
  else:
     return
 except:
   pass
for folder in os.listdir('modules'):
  if os.path.exists(os.path.join("modules", folder, "cog.py")):  
   bot.load_extensions(f"modules.{folder}.cog")    
      
bot.run('MTA0NjcyMzY5OTg4NzMyNTE5NA.GyqmVL.')