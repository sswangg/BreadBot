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
#client = discord.Client()

#Basically Transfers important variables
def init(ctxClient,ctxMessage, ctxPantryLimit, ctxCommonBread,ctxRareBread,ctxMythicalBread,ctxLegendaryBread):
  global client
  global cluster
  global database
  global collection
  global myquery
  global user
  global message
  global pantry_limit
  global common_bread
  global rare_bread
  global mythical_bread
  global legendary_bread
  client = ctxClient
  cluster = pymongo.MongoClient(os.getenv('CONNECTION_URL'))
  database = cluster["UserData"]
  collection = database["UserData"]
  myquery = { "_id": ctxMessage.author.id }
  user = collection.find(myquery)
  message = ctxMessage
  pantry_limit = ctxPantryLimit
  common_bread = ctxCommonBread
  rare_bread = ctxRareBread
  mythical_bread = ctxMythicalBread
  legendary_bread = ctxLegendaryBread
  
#Checks server count
async def servers():
  return("I'm in "+str(len(client.guilds))+" servers.")

#Creates account for user
async def createAccount():
  if (collection.count_documents(myquery) == 0):
          post = {"_id": message.author.id, "pantry": [], "common_pantry": [], "rare_pantry":[],"mythical_pantry":[],"legendary_pantry":[],"card_cooldown":0,"grain":int(0), "farm_cooldown":0, "name":message.author.name, "quest": [], "quest_cooldown":0} 
          collection.insert_one(post)

#Updates User Info(usernames..etc)
async def updateUserInfo():
  global common_pantry
  global rare_pantry
  global mythical_pantry
  global legendary_pantry
  global pantry
  global card_cooldown
  global farm_cooldown
  global grain
  global quest
  global counted_pantry
  global simplified_common_pantry
  global simplified_rare_pantry
  global simplified_mythical_pantry
  global simplified_legendary_pantry
  collection.update_one({"_id":message.author.id}, {"$set":{"name":message.author.name}})
  for result in user:
    common_pantry = result["common_pantry"]
    rare_pantry = result["rare_pantry"]
    mythical_pantry = result["mythical_pantry"]
    legendary_pantry = result["legendary_pantry"]
    pantry = result["pantry"]
    card_cooldown = result["card_cooldown"]
    farm_cooldown = result["farm_cooldown"]
    grain = int(result["grain"])
  
    document = collection.find_one(myquery)

    if "quest" in document.keys():
    #for result in user:
      quest = result["quest"]
      quest_cooldown = result["quest_cooldown"]
  
    if "quest" not in document.keys():
      collection.update_one({"_id":message.author.id},{"$set":{"quest":[]}})
      collection.update_one({"_id":message.author.id},{"$set":{"quest_cooldown":0}})
      quest = []
      quest_cooldown = 0


  counted_pantry = Counter(pantry)
  simplified_common_pantry = set(common_pantry)
  simplified_rare_pantry = set(rare_pantry)
  simplified_mythical_pantry = set(mythical_pantry)
  simplified_legendary_pantry = set(legendary_pantry)

async def bake():
      global card_cooldown
      for result in user:
        card_cooldown = result["card_cooldown"]     
      #Checks to make sure baking meets requirements
      if time.time() - card_cooldown >= 3600 and len(pantry)<pantry_limit:
        card_category = random.randint(1,1000)
        #Common Card Baked
        if card_category > 0 and card_category <= 700:
            card = common_bread[random.randint(0,len(common_bread)-1)]
            embed = discord.Embed(description = "Congratulations, you baked a "+card+". This card is a common", colour = 0x808080)
            await message.channel.send(embed = embed)
            collection.update_one({"_id":message.author.id}, {"$push":{"common_pantry":card}})
            collection.update_one({"_id":message.author.id}, {"$push":{"pantry":card}})
            collection.update_one({"_id":message.author.id}, {"$set":{"card_cooldown":time.time()}})

        #Rare Card Baked
        if card_category > 700 and card_category <= 975:
            card = rare_bread[random.randint(0,len(rare_bread)-1)]
          

            embed = discord.Embed(description = "Congratulations, you baked a "+card+". This card is a rare", colour = 0x0073ff)
            await message.channel.send(embed = embed)
            collection.update_one({"_id":message.author.id}, {"$push":{"rare_pantry":card}})
            collection.update_one({"_id":message.author.id}, {"$push":{"pantry":card}})
            collection.update_one({"_id":message.author.id}, {"$set":{"card_cooldown":time.time()}})

        #Mythical Card Baked
        if card_category > 975 and card_category <= 997:
            card = mythical_bread[random.randint(0,len(mythical_bread)-1)]
          

            embed = discord.Embed(description = "Congratulations, you baked a "+card+". This card is a mythical", colour = 0xb700ff)
            await message.channel.send(embed = embed)
            collection.update_one({"_id":message.author.id}, {"$push":{"mythical_pantry":card}})
            collection.update_one({"_id":message.author.id}, {"$push":{"pantry":card}})
            collection.update_one({"_id":message.author.id}, {"$set":{"card_cooldown":time.time()}})
        #Legendary Card Baked
        if card_category > 997 and card_category <= 1000:
            card = legendary_bread[random.randint(0,len(legendary_bread)-1)]
          
            embed = discord.Embed(description = "Congratulations, you baked a "+card+". This card is a LEGENDARY!", colour = 0xfbff00)
            await message.channel.send(embed = embed)
            collection.update_one({"_id":message.author.id}, {"$push":{"legendary_pantry":card}})
            collection.update_one({"_id":message.author.id}, {"$push":{"pantry":card}})
            collection.update_one({"_id":message.author.id}, {"$set":{"card_cooldown":time.time()}})
     
        return
        
      #Cooldown Time
      if time.time() - card_cooldown < 3600:
        delay_left = 3600- (time.time() - card_cooldown)
        embed = discord.Embed(description = 'You have ' +convert(delay_left)+' left until you can use this command again', colour = 0xff1100)
        await message.channel.send(embed = embed)
      
      else:
        embed = discord.Embed(description = "You have don't have any more room left in your pantry", colour = 0xff1100)
        await message.channel.send(embed = embed)