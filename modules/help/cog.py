from discord.ext import commands
from discord import option
import configparser
import discord
from discord import default_permissions
config = configparser.ConfigParser(allow_no_value=True)
config.read('database.ini')




  


class help(commands.Cog, name="Help"):
  """help command"""

  def __init__(self, bot: commands.Bot):
    self.bot = bot
  
  @commands.slash_command(description="Get a list of commands. To get more info about a specific command use `help <command>`")
  @option("command", description="The  catagory or command you want more info on.", required=False)
  async def help(self, ctx, command: str):
    embed=discord.Embed(title="**Dabloon Commands List**", description="**:gear: Visit our [support server](https://discord.gg/bRCuY5Nz)!**", color=0xf5b60a)
    config.read('database.ini')
    othercommand = ["module"]
    if command == None or command.lower() not in config[str(ctx.guild.id)]:
     embed.add_field(name=":wrench: **Managing**", value="`/help manager`", inline=True)
     embed.add_field(name="**:wrench: Miscellaneous**", value="`/help misc`", inline=True)
     embed.add_field(name="<:dabloonModerator:1047852503070408704> **Moderating**", value="`/help moderator`", inline=True)
     embed.add_field(name="<:dablooninfo:1047452313922584616> **Information**", value="`/help information`", inline=True)
     embed.add_field(name="<:dabloonRole:1047857570196488292> **Roles**", value="`/help role`", inline=True)
     embed.add_field(name=":clock12: **Slowmode**", value="`/help slowmode`", inline=True)
     embed.add_field(name=":laughing: **Fun**", value="`/help fun`", inline=True)
     embed.set_footer(text="©️ Dabloon")
     return await ctx.respond(embed=embed)  
  
    if command.lower() == "manager":
     embed=discord.Embed(title="**Help Category: :wrench: Managing**", description="To get more info about a command use `/help [command]`", color=0xf5b60a)
     embed.add_field(name="**All Commands:**", value="`module`, `command`, `addrole`, `rolename`, `delrole`, `setnick`, `nick`, `purge`, `announce`, `mentionable`, `addemote`, `role`", inline=False)
     embed.set_footer(text="©️ Dabloon")
     return await ctx.respond(embed=embed)
    if command.lower() == "module":
      embed=discord.Embed(title="**Help: Module**", description="Disable or enable a module in the server.", color=0xf5b60a)
      embed.add_field(name="**Command Usage**", value="`/module [module]`", inline=False)
      return await ctx.respond(embed=embed)
    if command.lower() == "command":
      embed=discord.Embed(title="**Help: Command**", description="Disable or enable a command in the server.", color=0xf5b60a)
      embed.add_field(name="**Command Usage**", value="`/command [module]`", inline=False)
      return await ctx.respond(embed=embed)
    if command.lower() == "addrole":
      embed=discord.Embed(title="**Help: Addrole**", description="Create a new role in the server.", color=0xf5b60a)
      embed.add_field(name="**Command Usage**", value="`/addrole [name]`\n`/addrole [name] [hoist (default=False)]`", inline=False)
      await ctx.respond(embed=embed)
    if command.lower() == "setnick":
      embed=discord.Embed(title="**Help: Setnick**", description="Changes the nickname of a user.", color=0xf5b60a)
      embed.add_field(name="**Command Usage**", value="`/setnick [user] [new nickname]`", inline=False)
      await ctx.respond(embed=embed)

      




    


    if command.lower() == "nick":
      embed=discord.Embed(title="**Help: Nick**", description="Changes the nickname of the bot.", color=0xf5b60a)
      embed.add_field(name="**Command Usage**", value="`/nick [new nickname]`", inline=False)
      await ctx.respond(embed=embed)

      
    if command.lower() == "purge":
      embed=discord.Embed(title="**Help: Purge**", description="Purges messages in the current channel or mentioned channel.", color=0xf5b60a)
      embed.add_field(name="**Command Usage**", value="`/purge [limit]`\n`/purge [limit] [channel (default=current)]`", inline=False)
      await ctx.respond(embed=embed)
    if command.lower() == "announce":
      embed=discord.Embed(title="**Help: Announce**", description="Announce a message with the Dabloon bot.", color=0xf5b60a)
      embed.add_field(name="**Command Usage**", value="`/announce [message] [channel]`\n`/announce [message] [channel] [mention (default=None)]`", inline=False)
      await ctx.respond(embed=embed)

    if command.lower() == "mentionable":
      embed=discord.Embed(title="**Help: Mentionable**", description="Toggle mentionable of a role on/off.", color=0xf5b60a)
      embed.add_field(name="**Command Usage**", value="`/mentionable [role] [channel]`", inline=False)
      await ctx.respond(embed=embed)
      
    if command.lower() == "addemote":
      embed=discord.Embed(title="**Help: Addemote**", description="Creates a new emoji in the server.", color=0xf5b60a)
      embed.add_field(name="**Command Usage**", value="`/addemote [name] [attachment]`", inline=False)
      await ctx.respond(embed=embed)
      





    if command.lower() == "role":
      embed=discord.Embed(title="**Help: Role**", description="Adds a role or roles to a specefic user/users.", color=0xf5b60a)
      embed.add_field(name="**Command Usage**", value="`/role_add [user] [role]`\n`/role_remove [user] [remove]`\n`/role_all [role]`\n`/role_removeall [role]`\n`/role_bots [role]`\n`/role_humans [role]`", inline=False)
      await ctx.respond(embed=embed)




    
    
    if command.lower() == "fun":
     embed=discord.Embed(title="**Help Category: :laughing: Fun**", description="To get more info about a command use `/help [command]`", color=0xf5b60a)
     embed.add_field(name="**All Commands:**", value="`rps`, `dadjoke`, `poll`, `flip`", inline=False)
     embed.set_footer(text="©️ Dabloon")
     return await ctx.respond(embed=embed)
    if command.lower() == "rps":
      embed=discord.Embed(title="**Help: Rps**", description="Play Rock, Paper, Scissors.", color=0xf5b60a)
      embed.add_field(name="**Command Usage**", value="`/rps [choice]`", inline=False)
      await ctx.respond(embed=embed)
    if command.lower() == "dadjoke":
      embed=discord.Embed(title="**Help: Dadjoke**", description="Get a dadjoke.", color=0xf5b60a)
      embed.add_field(name="**Command Usage**", value="`/dadjoke`", inline=False)
      await ctx.respond(embed=embed)
    if command.lower() == "poll":
      embed=discord.Embed(title="**Help: Poll**", description="Start a poll (max 10 choices).", color=0xf5b60a)
      embed.add_field(name="**Command Usage**", value="`/poll_create [message] [choice1] - [choice10]`", inline=False)
      await ctx.respond(embed=embed)
      
    if command.lower() == "flip":
      embed=discord.Embed(title="**Help: Flip**", description="Flip a coin.", color=0xf5b60a)
      embed.add_field(name="**Command Usage**", value="`/flip`", inline=False)
      await ctx.respond(embed=embed)

    if command.lower() == "information":
     embed=discord.Embed(title="**Help Category: <:dablooninfo:1047452313922584616> Information**", description="To get more info about a command use `/help [command]`", color=0xf5b60a)
     embed.add_field(name="**All Commands:**", value="`info`", inline=False)
     await ctx.respond(embed=embed)
    if command.lower() == "info":
      embed=discord.Embed(title="**Help: Info**", description="Get informations about the bot.", color=0xf5b60a)
      embed.add_field(name="**Command Usage**", value="`/info`", inline=False)
      await ctx.respond(embed=embed)

    if command.lower() == "misc":
     embed=discord.Embed(title="**Help Category: :wrench: Miscellaneous**", description="To get more info about a command use `/help [command]`", color=0xf5b60a)
     embed.add_field(name="**All Commands:**", value="`afk`, `discrim`, `avatar`", inline=False)
     embed.set_footer(text="©️ Dabloon")
     return await ctx.respond(embed=embed)
    if command.lower() == "afk":
      embed=discord.Embed(title="**Help: AFK**", description="Set yourself AFK.", color=0xf5b60a)
      embed.add_field(name="**Command Usage**", value="`/afk [reason]`", inline=False)
      return await ctx.respond(embed=embed)
    if command.lower() == "discrim":
      embed=discord.Embed(title="**Help: Discrim**", description="Search for users in server with a certain discrim.", color=0xf5b60a)
      embed.add_field(name="**Command Usage**", value="`/discrim [discrim]`", inline=False)
      return await ctx.respond(embed=embed)

    if command.lower() == "avatar":
      embed=discord.Embed(title="**Help: Avatar**", description="Get the avatar of a user.", color=0xf5b60a)
      embed.add_field(name="**Command Usage**", value="`/avatar`\n`/avatar [user (required=False)]`", inline=False)
      return await ctx.respond(embed=embed)
def setup(bot: commands.Bot):
  
  bot.add_cog(help(bot))