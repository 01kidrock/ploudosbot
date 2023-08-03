import asyncio
import code
import discord
import json
import time
import random
import string
import os
import os.path
import discord.ext
from discord.ext import commands
from discord.utils import get
import PloudosAPI



if os.path.exists('config.json'):
  with open("config.json") as fr:
    f = json.load(fr)
    username = f.get("username")
    pass = f.get("pass")
    Token = f.get("token")
else:
  pass = os.getenv("pass")
  username = os.getenv("username")
  Token = os.getenv("TOKEN")

print(username)
print(pass)
print(Token)




client = discord.Client()

client = commands.Bot(command_prefix = '/') 






@client.event
async def on_ready():
  print("\n\n\n\nbot online\n" + str(client.user) +"\n"+str(client.user.id)+"\n" + str(client))
#   guild = client.get_guild(1000969163273162833)
#   print(guild)
#   members = guild.members[0]
#   print(members)



@client.event
async def on_message(msg):
  print(msg)





client.run(Token)