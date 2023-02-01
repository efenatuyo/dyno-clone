from discord.ext import commands
from discord import option
import configparser
import discord
from discord import default_permissions
config = configparser.ConfigParser(allow_no_value=True)
config.read('database.ini')




  


class role(commands.Cog, name="Role"):
  """Many role functions ex. role_add or role_remove"""

  def __init__(self, bot: commands.Bot):
    self.bot = bot
  
  @commands.slash_command(description="Add user role or roles.")
  @default_permissions(manage_roles=True)
  @commands.guild_only()
  async def role_add(self, ctx, user:  discord.Option(discord.Member), role:  discord.Option(discord.Role)):
   config.read('database.ini')
   if config[str(ctx.guild.id)]["role"] == "False":
     embed = embed=discord.Embed(description="<:dabloonError:1047471668064428032> The addrole command is disabled in this server.", color=0xff0000)
     return await ctx.respond(embed=embed, ephemeral=True)
   else:
    if config[str(ctx.guild.id)]["manager"] == "False":
      embed = embed=discord.Embed(description="<:dabloonError:1047471668064428032> The manager module is disabled in this server.", color=0xff0000)
      return await ctx.respond(embed=embed, ephemeral=True)
    else:
     try:
         roling = await user.add_roles(role)
         embed=discord.Embed(description=f"<:dabloonSucces:1047473138943934474> Added {user.mention} `{role.name}` role", color=0xf5b60a)
         return await ctx.respond(embed=embed)
     except:
        embed=discord.Embed(description="<:dabloonError:1047471668064428032> The command failed.", color=0xff0000)
        return await ctx.respond(embed=embed, ephemeral=True)



  
  @commands.slash_command(description="Remove user role or roles.")
  @default_permissions(manage_roles=True)
  @commands.guild_only()
  async def role_remove(self, ctx, user:  discord.Option(discord.Member), role:  discord.Option(discord.Role)):
   config.read('database.ini')
   if config[str(ctx.guild.id)]["role"] == "False":
     embed = embed=discord.Embed(description="<:dabloonError:1047471668064428032> The addrole command is disabled in this server.", color=0xff0000)
     return await ctx.respond(embed=embed, ephemeral=True)
   else:
    if config[str(ctx.guild.id)]["manager"] == "False":
      embed = embed=discord.Embed(description="<:dabloonError:1047471668064428032> The manager module is disabled in this server.", color=0xff0000)
      return await ctx.respond(embed=embed, ephemeral=True)
    else:
     try:
         roling = await user.remove_roles(role)
         embed=discord.Embed(description=f"<:dabloonSucces:1047473138943934474> Removed {user.mention} `{role.name}` role", color=0xf5b60a)
         return await ctx.respond(embed=embed)
     except:
        embed=discord.Embed(description="<:dabloonError:1047471668064428032> The command failed.", color=0xff0000)
        return await ctx.respond(embed=embed, ephemeral=True)


  

  @commands.slash_command(description="Remove everyones role or roles.")
  @default_permissions(manage_roles=True)
  @commands.guild_only()
  async def role_removeall(self, ctx, role:  discord.Option(discord.Role)):
   config.read('database.ini')
   if config[str(ctx.guild.id)]["role"] == "False":
     embed = embed=discord.Embed(description="<:dabloonError:1047471668064428032> The addrole command is disabled in this server.", color=0xff0000)
     return await ctx.respond(embed=embed, ephemeral=True)
   else:
    if config[str(ctx.guild.id)]["manager"] == "False":
      embed = embed=discord.Embed(description="<:dabloonError:1047471668064428032> The manager module is disabled in this server.", color=0xff0000)
      return await ctx.respond(embed=embed, ephemeral=True)
    else:
     try:
         
         embed=discord.Embed(description=f"<:dablooninfo:1047452313922584616> Removing `{role.name}` from {len(role.members)} users", color=0x3498db)
         await ctx.respond(embed=embed)
         changed = 0
         for member in ctx.guild.members:
           try:
             if role in member.roles:
               
              await member.remove_roles(role)
              changed += 1
             else:
               pass
           except Exception as e:
             print(e)
         embed=discord.Embed(description=f"<:dabloonSucces:1047473138943934474> Succesfully removed `{role.name}` from {changed} users", color=0xf5b60a)
         await ctx.send(embed=embed)
     except:
        embed=discord.Embed(description="<:dabloonError:1047471668064428032> The command failed.", color=0xff0000)
        return await ctx.respond(embed=embed, ephemeral=True)


       

  @commands.slash_command(description="Adding everyone role or roles.")
  @default_permissions(manage_roles=True)
  @commands.guild_only()
  async def role_all(self, ctx, role:  discord.Option(discord.Role)):
   config.read('database.ini')
   if config[str(ctx.guild.id)]["role"] == "False":
     embed = embed=discord.Embed(description="<:dabloonError:1047471668064428032> The addrole command is disabled in this server.", color=0xff0000)
     return await ctx.respond(embed=embed, ephemeral=True)
   else:
    if config[str(ctx.guild.id)]["manager"] == "False":
      embed = embed=discord.Embed(description="<:dabloonError:1047471668064428032> The manager module is disabled in this server.", color=0xff0000)
      return await ctx.respond(embed=embed, ephemeral=True)
    else:
     try:
         
         embed=discord.Embed(description=f"<:dablooninfo:1047452313922584616> Adding `{role.name}` to {len(ctx.guild.members) - len(role.members)} users", color=0x3498db)
         await ctx.respond(embed=embed)
         changed = 0
         for member in ctx.guild.members:
           try:
              if role in member.roles:
                pass
              else:   
               await member.add_roles(role)
               changed += 1
           except:
             pass
         embed=discord.Embed(description=f"<:dabloonSucces:1047473138943934474> Succesfully added `{role.name}` to {changed} users", color=0xf5b60a)
         await ctx.send(embed=embed)
     except:
        embed=discord.Embed(description="<:dabloonError:1047471668064428032> The command failed.", color=0xff0000)
        return await ctx.respond(embed=embed, ephemeral=True)


       

  @commands.slash_command(description="Adding bots role or roles.")
  @default_permissions(manage_roles=True)
  @commands.guild_only()
  async def role_bots(self, ctx, role:  discord.Option(discord.Role)):
   config.read('database.ini')
   if config[str(ctx.guild.id)]["role"] == "False":
     embed = embed=discord.Embed(description="<:dabloonError:1047471668064428032> The addrole command is disabled in this server.", color=0xff0000)
     return await ctx.respond(embed=embed, ephemeral=True)
   else:
    if config[str(ctx.guild.id)]["manager"] == "False":
      embed = embed=discord.Embed(description="<:dabloonError:1047471668064428032> The manager module is disabled in this server.", color=0xff0000)
      return await ctx.respond(embed=embed, ephemeral=True)
    else:
     try:
         
         embed=discord.Embed(description=f"<:dablooninfo:1047452313922584616> Adding `{role.name}` to {len([m for m in ctx.guild.members if m.bot])} bots", color=0x3498db)
         await ctx.respond(embed=embed)
         changed = 0
         for member in ctx.guild.members:
           try:
            if member.bot:
              if role in member.roles:
                pass
              else:   
               await member.add_roles(role)
               changed += 1
            else:
              pass
           except:
             pass
         embed=discord.Embed(description=f"<:dabloonSucces:1047473138943934474> Succesfully added `{role.name}` to {changed} bots", color=0xf5b60a)
         await ctx.send(embed=embed)
     except:
        embed=discord.Embed(description="<:dabloonError:1047471668064428032> The command failed.", color=0xff0000)
        return await ctx.respond(embed=embed, ephemeral=True)




  @commands.slash_command(description="Adding humans role or roles.")
  @default_permissions(manage_roles=True)
  @commands.guild_only()
  async def role_humans(self, ctx, role:  discord.Option(discord.Role)):
   config.read('database.ini')
   if config[str(ctx.guild.id)]["role"] == "False":
     embed = embed=discord.Embed(description="<:dabloonError:1047471668064428032> The addrole command is disabled in this server.", color=0xff0000)
     return await ctx.respond(embed=embed, ephemeral=True)
   else:
    if config[str(ctx.guild.id)]["manager"] == "False":
      embed = embed=discord.Embed(description="<:dabloonError:1047471668064428032> The manager module is disabled in this server.", color=0xff0000)
      return await ctx.respond(embed=embed, ephemeral=True)
    else:
     try:
         
         embed=discord.Embed(description=f"<:dablooninfo:1047452313922584616> Adding `{role.name}` to {len([m for m in ctx.guild.members if not m.bot])} humans", color=0x3498db)
         await ctx.respond(embed=embed)
         changed = 0
         for member in ctx.guild.members:
           try:
            if not member.bot:
              if role in member.roles:
                pass
              else:   
               await member.add_roles(role)
               changed += 1
            else:
              pass
           except:
             pass
         embed=discord.Embed(description=f"<:dabloonSucces:1047473138943934474> Succesfully added `{role.name}` to {changed} humans", color=0xf5b60a)
         await ctx.send(embed=embed)
     except:
        embed=discord.Embed(description="<:dabloonError:1047471668064428032> The command failed.", color=0xff0000)
        return await ctx.respond(embed=embed, ephemeral=True)



  
def setup(bot: commands.Bot):
  
  bot.add_cog(role(bot))