import discord
import os
import random
from discord.ext import commands
from discord.ext.commands import Bot
import time
import datetime
from datetime import datetime
from replit import db
from keep_alive import keep_alive
import pymongo
import dns
import discord.utils
from discord.utils import get
from pymongo import MongoClient
import math
import collections
from collections import Counter
from basicFunctions import *
from main import *
#Basically Transfers important variables
  
#Checks server count
async def servers():
  return("I'm in "+str(len(client.guilds))+" servers.")
  



async def pantry():
  global common_pantry
  global rare_pantry
  global mythical_pantry
  global legendary_pantry
  for result in user:
    common_pantry = result["common_pantry"]
    rare_pantry = result["rare_pantry"]
    mythical_pantry = result["mythical_pantry"]
    legendary_pantry = result["legendary_pantry"]
  seperator = ', '
  
  common_shown = [count_duplicates(x, counted_pantry) for x in simplified_common_pantry]
  rare_shown = [count_duplicates(x, counted_pantry) for x in simplified_rare_pantry]
  mythical_shown = [count_duplicates(x, counted_pantry) for x in simplified_mythical_pantry]
  legendary_shown = [count_duplicates(x, counted_pantry) for x in simplified_legendary_pantry]
    
  pantry_shown = '**Commons**: '+seperator.join(sorted(common_shown))+'\n\n**Rares**: '+seperator.join(sorted(rare_shown))+'\n\n**Mythicals**: '+seperator.join(sorted(mythical_shown))+'\n\n**Legendaries** '+seperator.join(sorted(legendary_shown))
    
  embed = discord.Embed(title = message.author.name+"'s pantry:", description = pantry_shown, colour = 0x000000)
  embed.set_footer(text = 'Cards sell value: '+str(len(common_pantry)*500+len(rare_pantry)*2500+len(mythical_pantry)*6000+len(legendary_pantry)*20000)+' grain'+" | Size: "+str(len(pantry))+"/"+str(pantry_limit))
  await message.channel.send(embed = embed)