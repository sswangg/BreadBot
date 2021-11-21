#NOTES: ADD A SPACE INFRONT OF EACH COMMAND
import discord
import os
import random
from discord.ext import commands
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
#from commands import update_log
from basicFunctions import *
import config


prefix = '.bread'
madlibs = {}
collectors = []
pantry_limit = config.pantry_limit
common_bread = config.common_bread
rare_bread = config.rare_bread
mythical_bread = config.mythical_bread
legendary_bread = config.legendary_bread
updateLog = config.updateLog
helpContent = config.helpContent
faqContent = config.faqContent



      









#database stuff
cluster = pymongo.MongoClient(os.getenv('CONNECTION_URL'))
database = cluster["UserData"]
collection = database["UserData"]














client = commands.Bot(command_prefix='.bread ')

async def initCommand(message):
  global myquery
  global user
  myquery = { "_id": message.author.id }
  user = collection.find(myquery)
  if (collection.count_documents(myquery) == 0):
          post = {"_id": message.author.id, "pantry": [], "common_pantry": [], "rare_pantry":[],"mythical_pantry":[],"legendary_pantry":[],"card_cooldown":0,"grain":int(0), "farm_cooldown":0, "name":message.author.name, "quest": [], "quest_cooldown":0} 
          collection.insert_one(post)
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
  global quest_cooldown
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



@client.event
async def on_ready():
    
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('bot is being rewritten'))
    prefix = '.bread'

@client.event
async def on_guild_join(guild):
    
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('.bread help; In '+str(len(client.guilds))+' servers'))
    prefix = '.bread'


#initTest(client)
@client.command(name="test")
async def test(ctx,arg):
  await ctx.send(ctx.author.id)



@client.listen("on_message")
async def something(message):
    
    global prefix
    global after_keyowrd
    global player
    global madlibs
    global collectors
    global card_cooldown
    global common_pantry
    global rare_pantry
    global mythical_pantry
    global legendary_pantry
    global pantry
    global grain
    global quest
    global quest_cooldown
    global counted_pantry
    global user
    global collection
    #If message of author is client, then ignore
    if message.author == client.user:
        return
    if message.content.startswith(prefix):
      null, null,command = message.content.partition(prefix)
      command = command.strip()
    else:
      return

    #Temporary
    if message.author.id != 678269158000951307:
      await message.channel.send("Bread bot cant be used right now")
      return
    #Searching for user data
    myquery = { "_id": message.author.id }
    user = collection.find(myquery)

    #collection.find({ "_id": message.author.id })
    #Respons with server count
    if command == 'servers':
      await message.channel.send(servers())

    #Responds with invite link
    if command == 'invitelink':
        await message.channel.send('https://discord.com/api/oauth2/authorize?client_id=819653343839911956&permissions=8&scope=bot')
    #Responds with Help
    if command == 'help':
        embed = discord.Embed(description = helpContent, colour = 0x000000)
        await message.channel.send(embed = embed)
    #Responds with Change Log
    if command == 'update log': 
        embed = discord.Embed(description = updateLog, colour = 0x000000)
        await message.channel.send(embed = embed)
    #changing prefix and storing the new prefix with pickle (doesn't work)
    if message.content.startswith(prefix + ' prefix'):
        mystring = message.content
        prefixpart = 'prefix '
        before_prefix, prefix, after_prefix = mystring.partition(prefixpart)
        await message.channel.send('feature is currently unavailable')
        prefix = '.bread'
        #await message.channel.send('new prefix is '+after_prefix)
        #prefix = after_prefix
        #db[str(discord.Guild.id)] = prefix
    #Responds with faq
    if command == 'faq':
        embed = discord.Embed(description = faqContent, colour = 0x000000)
        await message.channel.send(embed = embed)

    #if message.content.startswith(prefix+' request'):
      #null,null,request = message.content.partition('request')
      #if request != None:
        #request_file = open('requests.txt', 'a')
        #request_file.write(str(message.author.id)+": "+request+"\n")



    ################
    #   
    #
    ##########
    #
    #
    #bread_card_game    

    #Starts user account
    #Idk why theres two different blocks of code for starting a user account

      

####

        #collection.update_one({"_id":message.author.id}, {"$set":{"score":score}})
        
####      
    #Baking
    #if command == 'bake':
      #await bake()
    
    

    
      


      
      



      
    

      


      
      

      




    
    if message.content.startswith(prefix+' trade'):

      if 'for' in message.content and ',' in message.content:
        offer = message.content
        offer = offer.replace(prefix+' trade','') 
        before, null, after = offer.partition(' for ')

        offering_cards = before.split(',')
        offering_cards = [x.strip() for x in offering_cards]
        wanting_cards = after.split(',')
        wanting_cards = [x.strip() for x in wanting_cards]
        all_bread = common_bread[:]+rare_bread[:]+mythical_bread[:]+legendary_bread[:]

        raw_offer_count = len(offering_cards)
        raw_want_count = len(wanting_cards)
        offering_cards = [x for x in offering_cards if x in pantry]
        wanting_cards = [x for x in wanting_cards if x in all_bread]

        if len(offering_cards) == raw_offer_count:
          if len(wanting_cards) == raw_want_count:
            if len(wanting_cards) == len(set(wanting_cards)) and len(offering_cards) == len(set(offering_cards)):
              separator = ", "
              embed = discord.Embed(title = "Trade Offer!", description = message.author.mention+' is trading\n'+separator.join(offering_cards)+" \nfor\n"+separator.join(wanting_cards), colour = 0x0dff00)
              embed.set_footer(text = "React to this message to accept the offer")
              await message.channel.send(embed = embed)
            else:
              embed = discord.Embed(description ="Error: You can't trade two of the same card", colour = 0xff1100)
              await message.channel.send(embed=embed)

          elif str(wanting_cards) not in all_bread:
            embed = discord.Embed(description ="Error: The card(s) you're requesting doesn't exist", colour = 0xff1100)
            await message.channel.send(embed=embed)

        else:
          embed = discord.Embed(description ="Error: You don't have these card(s)!", colour = 0xff1100)
          await message.channel.send(embed=embed)
      #single trade
      if 'for' in message.content and ',' not in message.content:
        offer = message.content
        offer = offer.replace(prefix+' trade','') 
        before, null, after = offer.partition(' for ')

        offering_cards = before
        wanting_cards = after


        embed = discord.Embed(title = "Trade Offer!", description = message.author.mention+' is trading\n'+offering_cards+" \nfor\n"+wanting_cards, colour = 0x0dff00)
        embed.set_footer(text = "React to this message to accept the offer")
        await message.channel.send(embed = embed)


      elif str(wanting_cards) not in all_bread:
        embed = discord.Embed(description ="Error: The card(s) you're requesting doesn't exist", colour = 0xff1100)
        await message.channel.send(embed=embed)

      else:
          embed = discord.Embed(description ="Error: You don't have these card(s)!", colour = 0xff1100)
          await message.channel.send(embed=embed)

    if message.content.startswith(prefix+ ' pantry') and message.content != prefix+' pantry' and len(message.mentions) == 1:
     
      global viewing_id
      msg = message.content
      null, null, after = msg.partition('pantry')
      null, null, after_at = after.partition('@')
      viewing_id, null, null = after_at.partition('>')
      viewing_id = str(viewing_id).replace("!","")
      viewing_id = viewing_id.strip()
      viewing_id = int(viewing_id)
      view_query = { "_id": viewing_id }

      viewing = collection.find(view_query)



        
      if collection.count_documents(view_query) == 1:

        for result in viewing:
            common_pantry = result["common_pantry"]
            rare_pantry = result["rare_pantry"]
            mythical_pantry = result["mythical_pantry"]
            legendary_pantry = result["legendary_pantry"]
            pantry = result["pantry"]
        seperator = ', '
        
        
        counted_pantry = Counter(pantry)
        simplified_common_pantry = set(common_pantry)
        simplified_rare_pantry = set(rare_pantry)
        simplified_mythical_pantry = set(mythical_pantry)
        simplified_legendary_pantry = set(legendary_pantry) 
        
        
        
        common_shown = [count_duplicates(x,counted_pantry) for x in simplified_common_pantry]
        rare_shown = [count_duplicates(x,counted_pantry) for x in simplified_rare_pantry]
        mythical_shown = [count_duplicates(x,counted_pantry) for x in simplified_mythical_pantry]
        legendary_shown = [count_duplicates(x,counted_pantry) for x in simplified_legendary_pantry]
        
        pantry_shown = '**Commons**: '+seperator.join(sorted(common_shown))+'\n\n**Rares**: '+seperator.join(sorted(rare_shown))+'\n\n**Mythicals**: '+seperator.join(sorted(mythical_shown))+'\n\n**Legendaries** '+seperator.join(sorted(legendary_shown))

        viewing_user = await client.fetch_user(viewing_id)

        embed = discord.Embed(title = str(viewing_user.name)+"'s pantry:", description = pantry_shown, colour = 0x000000)
        embed.set_footer(text = 'Cards sell value: '+str(len(common_pantry)*500+len(rare_pantry)*2500+len(mythical_pantry)*6000+len(legendary_pantry)*20000)+' grain'+" | Size: "+str(len(pantry))+"/"+str(pantry_limit))
        
        await message.channel.send(embed = embed)
    
    #grain


    
    if message.content.startswith(prefix+ ' bet'):
      msg = message.content
      null, null, gambling = msg.partition('bet ')
      gambling = str(gambling.strip())
      

      
      if str(gambling).isdigit() == True and int(gambling) <= grain:
        coin = random.randint(1,100)
        if coin <=60:
          gambling = int(gambling)
          gambling = gambling*(random.randint(20,100)/100)
          gambling = math.floor(gambling)
          
          collection.update_one({"_id":message.author.id}, {"$set":{"grain":grain+gambling}})
          embed = discord.Embed(title = "You won the bet!", description = "You won the bet and gained "+str(gambling)+" pieces of grain",colour = 0x0dff00)

          await message.channel.send(embed = embed)
        
        if coin >60:
          gambling = int(gambling)
          collection.update_one({"_id":message.author.id}, {"$set":{"grain":grain-gambling}})
          
          embed = discord.Embed(title = "You lost the bet.", description = "You lost the bet and lost "+str(gambling)+" pieces of grain", colour = 0xff1100)

          await message.channel.send(embed = embed)
      
      if str(gambling).isdigit() == True and int(gambling) > grain:
          embed = discord.Embed(description = "You don't have this much grain", colour = 0xff1100)

          await message.channel.send(embed = embed)
      
      if str(gambling).isdigit() == False:
          embed = discord.Embed(description = "Please enter a non-negative integer to bet", colour = 0xff1100)

          await message.channel.send(embed = embed)
    
    if message.content == prefix+' start quest':
      if time.time()-quest_cooldown > 86400 and len(quest) != 3:
        collection.update_one({"_id":message.author.id}, {"$set":{"quest_cooldown":time.time()}})
      
        available_bread = common_bread[:]

        card_1 = available_bread[random.randint(0, len(available_bread)-1)]
        
        available_bread.remove(card_1)
        
        card_2 = available_bread[random.randint(0, len(available_bread)-1)]
        
        available_bread.remove(card_2)
        
        card_3 = available_bread[random.randint(0, len(available_bread)-1)]

        available_bread.remove(card_3)
      
        collection.update_one({"_id":message.author.id}, {"$push":{"quest":card_1}})
        collection.update_one({"_id":message.author.id}, {"$push":{"quest":card_2}})
        collection.update_one({"_id":message.author.id}, {"$push":{"quest":card_3}})
        embed = discord.Embed(title = 'Quest Started!', description = message.author.mention+' must get '+card_1+', '+card_2+', '+card_3+' in 24 hours in order to receive an award of 2500 grain', colour = 0x0dff00)
        await message.channel.send(embed = embed)
        return
      if time.time()-quest_cooldown > 86400 and len(quest) == 3:
        collection.update_one({"_id":message.author.id}, {"$set":{"quest":[]}})
        collection.update_one({"_id":message.author.id}, {"$set":{"quest_cooldown":time.time()}})
      
        available_bread = common_bread[:]

        card_1 = available_bread[random.randint(0, len(available_bread)-1)]
        available_bread.remove(card_1)
        card_2 = available_bread[random.randint(0, len(available_bread)-1)]
        available_bread.remove(card_2)
        card_3 = available_bread[random.randint(0, len(available_bread)-1)]
        available_bread.remove(card_3)
      
        collection.update_one({"_id":message.author.id}, {"$push":{"quest":card_1}})
        collection.update_one({"_id":message.author.id}, {"$push":{"quest":card_2}})
        collection.update_one({"_id":message.author.id}, {"$push":{"quest":card_3}})
        embed = discord.Embed(title = 'Quest Started!', description = message.author.mention+' must get '+card_1+', '+card_2+', '+card_3+' in 24 hours in order to receive an award of 2500 grain', colour = 0x0dff00)
        await message.channel.send(embed = embed)
        return   
      
      else:
        time_left = convert((quest_cooldown+86400)-time.time())
        embed = discord.Embed(description = message.author.mention+"You can't start a new quest at the moment. The cooldown ends in "+str(time_left), colour = 0xff1100)
        embed.set_footer(text = "Type .bread view quest to see your ongoing quest")
        await message.channel.send(embed = embed)
    
    if message.content == prefix+ ' view quest':

      if len(quest) == 3 and time.time()-quest_cooldown<86400:
        time_left = convert((quest_cooldown+86400)-time.time())
        embed = discord.Embed(title = message.author.name+"'s on going quest:", description = message.author.mention+" needs to get "+quest[0]+", "+quest[1]+", "+quest[2]+" in "+time_left+" in order to claim an award of 2500 grain", colour = 0x0dff00)
        await message.channel.send(embed = embed)
      elif quest_cooldown == 0:
        embed = discord.Embed(description = "It seems like you haven't started a quest yet. Type .bread start quest to start a quest", colour = 0xff1100)
        await message.channel.send(embed = embed)
      elif quest_cooldown+86400<time.time():
        embed = discord.Embed(description = "Looks like it's been more than 24 hours since you started your quest, so the quest is inactive",colour = 0xff1100)
        embed.set_footer(text = "Type .bread start quest to start a new quest")
        await message.channel.send(embed = embed)
      else:
        time_left = convert((quest_cooldown+86400)-time.time())
        embed = discord.Embed(description = "It seems like you've already completed your quest. The cooldown ends in "+str(time_left), colour = 0xff1100)
        await message.channel.send(embed = embed)
    
    if message.content == prefix+' claim quest':
      if len(quest)==3 and time.time()<quest_cooldown+86400:
        card_1 = quest[0]
        card_2 = quest[1]
        card_3 = quest[2]
        if card_1 in common_pantry and card_2 in common_pantry and card_3 in common_pantry:

          common_pantry.remove(card_1)
          pantry.remove(card_1)
          collection.update_one({"_id":message.author.id}, {"$set":{"common_pantry":common_pantry}})
          collection.update_one({"_id":message.author.id}, {"$set":{"pantry":pantry}})

          common_pantry.remove(card_2)
          pantry.remove(card_2)
          collection.update_one({"_id":message.author.id}, {"$set":{"common_pantry":common_pantry}})
          collection.update_one({"_id":message.author.id}, {"$set":{"pantry":pantry}})

          common_pantry.remove(card_3)
          pantry.remove(card_3)
          collection.update_one({"_id":message.author.id}, {"$set":{"common_pantry":common_pantry}})
          collection.update_one({"_id":message.author.id}, {"$set":{"pantry":pantry}})
        
          collection.update_one({"_id":message.author.id}, {"$set":{"quest":[]}})
        
          collection.update_one({"_id":message.author.id}, {"$set":{"grain":grain+3000}})
          embed = discord.Embed(title = "Quest Complete!", description = message.author.name+" completed their quest",colour = 0x0dff00)

          await message.channel.send(embed = embed)
        else:
          embed = discord.Embed(description = "Looks like you don't have the needed cards yet",colour = 0xff1100)
          embed.set_footer(text = "Type .bread view quest to show your ongoing quest")
          await message.channel.send(embed = embed)

      elif quest_cooldown == 0:
        embed = discord.Embed(description = "Looks like you haven't started a quest yet",colour = 0xff1100)
        embed.set_footer(text = "Type .bread start quest to start a quest")
        await message.channel.send(embed = embed)
      
      elif quest_cooldown + 86400 < time.time():
        embed = discord.Embed(description = "Looks like it's been more than 24 hours since you started your quest, so the quest is in active",colour = 0xff1100)
        embed.set_footer(text = "Type .bread start quest to start a new quest")
        await message.channel.send(embed = embed)


      else:
        embed = discord.Embed(description = "Looks like you don't have the needed cards yet",colour = 0xff1100)
        embed.set_footer(text = "Type .bread view quest to show your ongoing quest")
        await message.channel.send(embed = embed)

@client.command(name="github")
async def github(ctx):
  await ctx.send("Contribute to the Bot! https://github.com/Cryplo/BreadBot")

@client.command(name="bake")
async def bake(ctx):
      await initCommand(ctx)
      #Checks to make sure baking meets requirements
      if time.time() - card_cooldown >= 3600 and len(pantry)<pantry_limit:
        card_category = random.randint(1,1000)
        #Common Card Baked
        if card_category > 0 and card_category <= 700:
            card = common_bread[random.randint(0,len(common_bread)-1)]
            embed = discord.Embed(description = "Congratulations, you baked a "+card+". This card is a common", colour = 0x808080)
            
            collection.update_one({"_id":ctx.author.id}, {"$push":{"common_pantry":card}})
            collection.update_one({"_id":ctx.author.id}, {"$push":{"pantry":card}})
            collection.update_one({"_id":ctx.author.id}, {"$set":{"card_cooldown":time.time()}})
            await ctx.send(embed = embed)

        #Rare Card Baked
        if card_category > 700 and card_category <= 975:
            card = rare_bread[random.randint(0,len(rare_bread)-1)]
          

            embed = discord.Embed(description = "Congratulations, you baked a "+card+". This card is a rare", colour = 0x0073ff)
            await ctx.send(embed = embed)
            collection.update_one({"_id":ctx.author.id}, {"$push":{"rare_pantry":card}})
            collection.update_one({"_id":ctx.author.id}, {"$push":{"pantry":card}})
            collection.update_one({"_id":ctx.author.id}, {"$set":{"card_cooldown":time.time()}})

        #Mythical Card Baked
        if card_category > 975 and card_category <= 997:
            card = mythical_bread[random.randint(0,len(mythical_bread)-1)]
          

            embed = discord.Embed(description = "Congratulations, you baked a "+card+". This card is a mythical", colour = 0xb700ff)
            await ctx.send(embed = embed)
            collection.update_one({"_id":ctx.author.id}, {"$push":{"mythical_pantry":card}})
            collection.update_one({"_id":ctx.author.id}, {"$push":{"pantry":card}})
            collection.update_one({"_id":ctx.author.id}, {"$set":{"card_cooldown":time.time()}})
        #Legendary Card Baked
        if card_category > 997 and card_category <= 1000:
            card = legendary_bread[random.randint(0,len(legendary_bread)-1)]
          
            embed = discord.Embed(description = "Congratulations, you baked a "+card+". This card is a LEGENDARY!", colour = 0xfbff00)
            await ctx.send(embed = embed)
            collection.update_one({"_id":ctx.author.id}, {"$push":{"legendary_pantry":card}})
            collection.update_one({"_id":ctx.author.id}, {"$push":{"pantry":card}})
            collection.update_one({"_id":ctx.author.id}, {"$set":{"card_cooldown":time.time()}})
     
        return
        
      #Cooldown Time
      if time.time() - card_cooldown < 3600:
        delay_left = 3600- (time.time() - card_cooldown)
        embed = discord.Embed(description = 'You have ' +convert(delay_left)+' left until you can use this command again', colour = 0xff1100)
        await ctx.send(embed = embed)
      
      else:
        embed = discord.Embed(description = "You have don't have any more room left in your pantry", colour = 0xff1100)
        await ctx.send(embed = embed)

@client.command(name="pantry")
async def show_pantry(ctx):
  await initCommand(ctx)
  common_shown = [count_duplicates(x, counted_pantry) for x in simplified_common_pantry]
  rare_shown = [count_duplicates(x, counted_pantry) for x in simplified_rare_pantry]
  mythical_shown = [count_duplicates(x, counted_pantry) for x in simplified_mythical_pantry]
  legendary_shown = [count_duplicates(x, counted_pantry) for x in simplified_legendary_pantry]

  seperator = ", "
    
  pantry_shown = '**Commons**: '+seperator.join(sorted(common_shown))+'\n\n**Rares**: '+seperator.join(sorted(rare_shown))+'\n\n**Mythicals**: '+seperator.join(sorted(mythical_shown))+'\n\n**Legendaries** '+seperator.join(sorted(legendary_shown))
    
  embed = discord.Embed(title = ctx.author.name+"'s pantry:", description = pantry_shown, colour = 0x000000)
  embed.set_footer(text = 'Cards sell value: '+str(len(common_pantry)*500+len(rare_pantry)*2500+len(mythical_pantry)*6000+len(legendary_pantry)*20000)+' grain'+" | Size: "+str(len(pantry))+"/"+str(pantry_limit))
  await ctx.channel.send(embed = embed)

@client.command(name="cards")
async def cards(ctx):
  seperator = ', '
  cards_shown = '**Commons**: '+seperator.join(sorted(common_bread))+'\n\n**Rares**: '+seperator.join(sorted(rare_bread))+'\n\n**Mythicals**: '+seperator.join(sorted(mythical_bread))+'\n\n**Legendaries**: '+seperator.join(sorted(legendary_bread))
    
  embed = discord.Embed(title = "All cards:", description = cards_shown, colour = 0x000000)
  await ctx.send(embed = embed)
  
@client.command(name="prices")
async def prices(ctx):
  embed = discord.Embed(title = "Prices:", description = "**Buying**\n`Common cards`: 1000 grain\n`Rare cards`: 5000 grain\n `Mythical cards`: 12000 grain\n `Legendary cards`: 40000 grain\n\n**Selling**\n`Common cards`: 500 grain\n`Rare cards`: 2500 grain\n `Mythical cards`: 6000 grain\n`Legendary cards`: 20000 grain", colour = 0x000000)
  await ctx.send(embed = embed)

@client.command(name="sell")
async def sell(ctx,*,selling_card):  
  global grain
  await initCommand(ctx)  
  print(selling_card)
  if selling_card in pantry:


    
    if selling_card in common_pantry:
      common_pantry.remove(selling_card)
      pantry.remove(selling_card)
      collection.update_one({"_id":ctx.author.id}, {"$set":{"common_pantry":common_pantry}})
      collection.update_one({"_id":ctx.author.id}, {"$set":{"pantry":pantry}})
      grain = grain+500        
      collection.update_one({"_id":ctx.author.id}, {"$set":{"grain":grain}})
      embed = discord.Embed(title = selling_card+" has been sold!", description = selling_card+" has been sold for 500 grain", colour = 0x0dff00)
      await ctx.send(embed = embed)
      return

    if selling_card in rare_pantry:
      rare_pantry.remove(selling_card)
      pantry.remove(selling_card)
      collection.update_one({"_id":ctx.author.id}, {"$set":{"rare_pantry":rare_pantry}})
      collection.update_one({"_id":ctx.author.id}, {"$set":{"pantry":pantry}})
      grain = grain+2500          
      collection.update_one({"_id":ctx.author.id}, {"$set":{"grain":grain}})
      embed = discord.Embed(title = selling_card+" has been sold!", description = selling_card+" has been sold for 2500 grain", colour = 0x0dff00)
      await ctx.send(embed = embed)
      return

    if selling_card in mythical_pantry:
      mythical_pantry.remove(selling_card)
      pantry.remove(selling_card)
      collection.update_one({"_id":ctx.author.id}, {"$set":{"mythical_pantry":mythical_pantry}})
      collection.update_one({"_id":ctx.author.id}, {"$set":{"pantry":pantry}})
      grain = grain+6000          
      collection.update_one({"_id":ctx.author.id}, {"$set":{"grain":grain}})
      embed = discord.Embed(title = selling_card+" has been sold!", description = selling_card+" has been sold for 6000 grain", colour = 0x0dff00)
      await ctx.send(embed = embed)
      return

    if selling_card in legendary_pantry:
      legendary_pantry.remove(selling_card)
      pantry.remove(selling_card)
      collection.update_one({"_id":ctx.author.id}, {"$set":{"legendary_pantry":legendary_pantry}})
      collection.update_one({"_id":ctx.author.id}, {"$set":{"pantry":pantry}})
      grain = grain+20000          
      collection.update_one({"_id":ctx.author.id}, {"$set":{"grain":grain}})
      embed = discord.Embed(title = selling_card+" has been sold!", description = selling_card+" has been sold for 20000 grain", colour = 0x0dff00)
      await ctx.send(embed = embed)
      return
  
  if selling_card == 'all':
    collection.update_one({"_id":ctx.author.id}, {"$set":{"common_pantry":[]}})
    collection.update_one({"_id":ctx.author.id}, {"$set":{"rare_pantry":[]}})
    collection.update_one({"_id":ctx.author.id}, {"$set":{"mythical_pantry":[]}})
    collection.update_one({"_id":ctx.author.id}, {"$set":{"legendary_pantry":[]}})
    collection.update_one({"_id":ctx.author.id}, {"$set":{"pantry":[]}})
    
    grain_gained = len(common_pantry)*500+len(rare_pantry)*2500+len(mythical_pantry)*6000+len(legendary_pantry)*20000
    
    collection.update_one({"_id":ctx.author.id}, {"$set":{"grain":grain+grain_gained}})
    
    embed = discord.Embed(title = "You have sold your entire pantry", description = "You have sold your entire pantry and gained "+str(grain_gained)+" grain", colour = 0x0dff00)
    await ctx.send(embed = embed)
    return
  
  if selling_card == "commons":
    collection.update_one({"_id":ctx.author.id}, {"$set":{"common_pantry":[]}})
    collection.update_one({"_id":ctx.author.id}, {"$set":{"pantry":[x for x in pantry if x not in common_pantry]}})
    
    grain_gained = len(common_pantry)*500
    
    collection.update_one({"_id":ctx.author.id}, {"$set":{"grain":grain+grain_gained}})
    
    embed = discord.Embed(title = "You have sold all your common cards", description = "You have sold all your common cards and gained "+str(grain_gained)+" grain", colour = 0x0dff00)
    await ctx.send(embed = embed)
    return
  
  if selling_card == "rares":
    collection.update_one({"_id":ctx.author.id}, {"$set":{"rare_pantry":[]}})
    collection.update_one({"_id":ctx.author.id}, {"$set":{"pantry":[x for x in pantry if x not in rare_pantry]}})

    grain_gained = len(rare_pantry)*2500
    
    collection.update_one({"_id":ctx.author.id}, {"$set":{"grain":grain+grain_gained}})
    
    embed = discord.Embed(title = "You have sold all your rare cards", description = "You have sold all your rare cards and gained "+str(grain_gained)+" grain", colour = 0x0dff00)
    await ctx.send(embed = embed)
    return
  
  if selling_card == "mythicals":
    collection.update_one({"_id":ctx.author.id}, {"$set":{"mythical_pantry":[]}})
    collection.update_one({"_id":ctx.author.id}, {"$set":{"pantry":[x for x in pantry if x not in mythical_pantry]}})

    grain_gained = len(mythical_pantry)*12000
    
    collection.update_one({"_id":ctx.author.id}, {"$set":{"grain":grain+grain_gained}})
    
    embed = discord.Embed(title = "You have sold all your mythical cards", description = "You have sold all your mythical cards and gained "+str(grain_gained)+" grain", colour = 0x0dff00)
    await ctx.send(embed = embed)
    return
  
  if selling_card == "legendaries":
    collection.update_one({"_id":ctx.author.id}, {"$set":{"legendary_pantry":[]}})
    collection.update_one({"_id":ctx.author.id}, {"$set":{"pantry":[x for x in pantry if x not in legendary_pantry]}})

    grain_gained = len(legendary_pantry)*40000
    
    collection.update_one({"_id":ctx.author.id}, {"$set":{"grain":grain+grain_gained}})
    
    embed = discord.Embed(title = "You have sold all your legendary cards", description = "You have sold all your legendary cards and gained "+str(grain_gained)+" grain", colour = 0x0dff00)
    await ctx.send(embed = embed)
    return


  else:
    await ctx.send("You either don't have this item or it doesn't exist")

@client.command(name="buy")
async def buy(ctx,*,buying_card):
  await initCommand(ctx)
  global grain
  for result in user:
    grain = int(result["grain"])
  if buying_card in common_bread and grain >= 1000 and len(pantry)<pantry_limit:
      
        grain = grain-1000
      
        card = buying_card
      

        embed = discord.Embed(description = "Congratulations, you bought a "+card+" for 1000 grain. This card is a common", colour = 0x808080)
        await ctx.send(embed = embed)
        collection.update_one({"_id":ctx.author.id}, {"$push":{"common_pantry":card}})
        collection.update_one({"_id":ctx.author.id}, {"$push":{"pantry":card}})
        collection.update_one({"_id":ctx.author.id}, {"$set":{"grain":grain}})

        return


  
  if buying_card in rare_bread and grain >= 5000 and len(pantry)<pantry_limit:       
    
        card = buying_card
    
        grain = grain-5000   
    

        embed = discord.Embed(description = "Congratulations, you bought a "+card+" for 5000 grain. This card is a rare", colour = 0x0073ff)
        await ctx.send(embed = embed)
        collection.update_one({"_id":ctx.author.id}, {"$push":{"rare_pantry":card}})
        collection.update_one({"_id":ctx.author.id}, {"$push":{"pantry":card}})
        collection.update_one({"_id":ctx.author.id}, {"$set":{"grain":grain}})
        return 

    
  if buying_card in mythical_bread and grain >= 12000 and len(pantry)<pantry_limit:  
        card = buying_card
        grain = grain-12000           

        embed = discord.Embed(description = "Congratulations, you bought a "+card+" for 12000 grain. This card is a mythical", colour = 0xb700ff)
        await ctx.send(embed = embed)
        collection.update_one({"_id":ctx.author.id}, {"$push":{"mythical_pantry":card}})
        collection.update_one({"_id":ctx.author.id}, {"$push":{"pantry":card}})
        collection.update_one({"_id":ctx.author.id}, {"$set":{"grain":grain}})

        return


  if buying_card in legendary_bread and grain >= 40000 and len(pantry)<pantry_limit:
        card = buying_card
        grain = grain-40000 
    
        embed = discord.Embed(description = "Congratulations, you bought a "+card+" for 40000 grain. This card is a LEGENDARY!", colour = 0xfbff00)
        await ctx.send(embed = embed)
        collection.update_one({"_id":ctx.author.id}, {"$push":{"legendary_pantry":card}})
        collection.update_one({"_id":ctx.author.id}, {"$push":{"pantry":card}})

        collection.update_one({"_id":ctx.author.id}, {"$set":{"grain":grain}})
        return
    
  if buying_card not in legendary_bread and buying_card not in mythical_bread and buying_card not in rare_bread and buying_card not in common_bread:
      embed = discord.Embed(description = "This card doesn't exist", colour = 0xff1100)
      embed.set_footer(text = "To check all cards, type .bread cards")
      await ctx.send(embed = embed)
  
  elif len(pantry) >=pantry_limit:
    embed = discord.Embed(description = "You have don't have any more room left in your pantry", colour = 0xff1100)
    await ctx.send(embed = embed)
  
  else:
      embed = discord.Embed(description = "You don't have enough grain", colour = 0xff1100)
      embed.set_footer(text = "To check the prices of bread, type .bread prices")
      await ctx.send(embed = embed)    

@client.command(name="grain")
async def show_grain(ctx,*mention):
  await initCommand(ctx)
  mention = ''.join(mention)
  if mention!='':
    x = "<@!>"
    for char in x:
      mention = mention.replace(char, "")
    viewing_id = mention
    viewing_id = int(viewing_id)

  else:
    viewing_id = ctx.author.id
  view_query = { "_id": viewing_id }

  viewing = collection.find(view_query)
  if collection.count_documents(view_query) == 1:

    for result in viewing:
        grain = result["grain"]
  viewing_user = await client.fetch_user(viewing_id)

  embed = discord.Embed(title = str(viewing_user.name)+"'s grain:", description = grain, colour = 0x000000)
  
  await ctx.send(embed = embed)
@client.command(name="farm")
async def farm(ctx):
  await initCommand(ctx)
  global grain
  global farm_cooldown
  jackpot = random.randint(1,100)  
  
  if time.time()-farm_cooldown > 10 and jackpot < 90:
    grain_gained = random.randint(10,25)
    farm_cooldown = time.time()
    grain = grain+grain_gained
    embed = discord.Embed(description = 'You gained ' +str(grain_gained)+' pieces of grain', colour = 0x0dff00)
    await ctx.send(embed = embed)
    collection.update_one({"_id":ctx.author.id}, {"$set":{"grain":grain}})
    collection.update_one({"_id":ctx.author.id}, {"$set":{"farm_cooldown":farm_cooldown}})
    return  

  if time.time()-farm_cooldown > 10 and jackpot >= 90 and jackpot < 99:
    grain_gained = random.randint(35,65)
    farm_cooldown = time.time()
    grain = grain+grain_gained
    embed = discord.Embed(description = 'Mini Jackpot! You gained ' +str(grain_gained)+' pieces of grain', colour = 0x0dff00)
    await ctx.send(embed = embed)
    collection.update_one({"_id":ctx.author.id}, {"$set":{"grain":grain}})
    collection.update_one({"_id":ctx.author.id}, {"$set":{"farm_cooldown":farm_cooldown}})
    return  
  
  
  if time.time()-farm_cooldown > 10 and jackpot >= 99:
    grain_gained = random.randint(110,140)
    farm_cooldown = time.time()
    grain = grain+grain_gained
    embed = discord.Embed(description = 'HUGE JACKPOT!!! You gained ' +str(grain_gained)+' pieces of grain', colour = 0x0dff00)
    await ctx.send(embed = embed)
    collection.update_one({"_id":ctx.author.id}, {"$set":{"grain":grain}})
    collection.update_one({"_id":ctx.author.id}, {"$set":{"farm_cooldown":farm_cooldown}})
    return  
  
  else:
    farm_delay_left = 10 - (int(time.time()) - int(farm_cooldown))
    embed = discord.Embed(description = 'You have ' +str(farm_delay_left)+' seconds left until you can use this command again', colour = 0xff1100)
    await ctx.send(embed = embed)


@client.event
async def on_raw_reaction_add (payload):
  
  
  message = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)
  author = message.author
  reaction = get(message.reactions)
  
  
  if author == client.user and message.embeds[0].title == 'Trade Offer!' and reaction.count == 1:
      global trader_common_pantry
      global trader_rare_pantry
      global trader_mythical_pantry
      global trader_legendary_pantry
      global trader_pantry
      global trader

      global accepter_common_pantry
      global accepter_rare_pantry
      global accepter_mythical_pantry
      global accepter_legendary_pantry
      global accepter_pantry
      global offering
      global wanting
      global accepter
      msg_description=message.embeds[0].description
      accepter = payload.user_id
      front, null, null = msg_description.partition('>')
      null, null, trader = front.partition('@')

      #print(reaction.message.mentions)



      null, null, end = msg_description.partition('trading')

      offering, null, wanting = end.partition('for')

      offering = offering.strip()
      wanting = wanting.strip()
      trader = str(trader).replace("!","")
      accepter = str(accepter).replace("!","")
      trader = str(trader).strip()
      accepter = str(accepter).strip()
      trader = int(trader)
      accepter = int(accepter)


      offering_cards = offering.split(',')
      offering_cards = [x.strip() for x in offering_cards]
      wanting_cards = wanting.split(',')
      wanting_cards = [x.strip() for x in wanting_cards]






      
      trader_query = { "_id": trader }
      accepter_query = { "_id": accepter }
      trader_find = collection.find(trader_query)
      accepter_find = collection.find(accepter_query)




      for result in trader_find:
        trader_common_pantry = result["common_pantry"]
        trader_rare_pantry = result["rare_pantry"]
        trader_mythical_pantry = result["mythical_pantry"]
        trader_legendary_pantry = result["legendary_pantry"]
        trader_pantry = result["pantry"]
        trader_card_cooldown = result["card_cooldown"]
        trader_farm_cooldown = result["farm_cooldown"]
        trader_grain = int(result["grain"])
      
      for result in accepter_find:
        accepter_common_pantry = result["common_pantry"]
        accepter_rare_pantry = result["rare_pantry"]
        accepter_mythical_pantry = result["mythical_pantry"]
        accepter_legendary_pantry = result["legendary_pantry"]
        accepter_pantry = result["pantry"]
        accepter_card_cooldown = result["card_cooldown"]
        accepter_farm_cooldown = result["farm_cooldown"]
        accepter_grain = int(result["grain"])


      raw_offer_count = len(offering_cards)
      raw_want_count = len(wanting_cards)
      
      offering_cards = [x for x in offering_cards if x in trader_pantry]
      wanting_cards = [x for x in wanting_cards if x in accepter_pantry]



      if len(offering_cards) == raw_offer_count and len(wanting_cards) == raw_want_count and len(offering_cards) == len(set(offering_cards)) and len(wanting_cards) == len(set(wanting_cards)):
        #trader_pantry = [x for x in trader_pantry if x in offering_cards]
        #print(trader_pantry)
        #print(accepter_pantry)
        for x in offering_cards:
          trader_pantry.remove(x)
          if x in common_bread:
            trader_common_pantry.remove(x)

          if x in rare_bread:
            trader_rare_pantry.remove(x)

          if x in mythical_bread:
            trader_mythical_pantry.remove(x)

          if x in legendary_bread:
            trader_legendary_pantry.remove(x)

        for y in wanting_cards:
          
          accepter_pantry.remove(y)
          
          if y in common_bread:
            accepter_common_pantry.remove(y)

          if y in rare_bread:
            accepter_rare_pantry.remove(y)

          if y in mythical_bread:
            accepter_mythical_pantry.remove(y)

          if y in legendary_bread:
            accepter_legendary_pantry.remove(y)
        

        

        
        
        for x in wanting_cards:
          trader_pantry.append(x)
          if x in common_bread:
            trader_common_pantry.append(x)

          if x in rare_bread:
            trader_rare_pantry.append(x)

          if x in mythical_bread:
            trader_mythical_pantry.append(x)

          if x in legendary_bread:
            trader_legendary_pantry.append(x)
        
        for x in offering_cards:
          accepter_pantry.append(x)
          if x in common_bread:
            accepter_common_pantry.append(x)

          if x in rare_bread:
            accepter_rare_pantry.append(x)

          if x in mythical_bread:
            accepter_mythical_pantry.append(x)

          if x in legendary_bread:
            accepter_legendary_pantry.append(x)
        
        collection.update_one({"_id":trader}, {"$set":{"pantry":trader_pantry}})
        collection.update_one({"_id":trader}, {"$set":{"common_pantry":trader_common_pantry}})
        collection.update_one({"_id":trader}, {"$set":{"rare_pantry":trader_rare_pantry}})
        collection.update_one({"_id":trader}, {"$set":{"mythical_pantry":trader_mythical_pantry}})
        collection.update_one({"_id":trader}, {"$set":{"legendary_pantry":trader_legendary_pantry}})

        collection.update_one({"_id":accepter}, {"$set":{"pantry":accepter_pantry}})
        collection.update_one({"_id":accepter}, {"$set":{"common_pantry":accepter_common_pantry}})
        collection.update_one({"_id":accepter}, {"$set":{"rare_pantry":accepter_rare_pantry}})
        collection.update_one({"_id":accepter}, {"$set":{"mythical_pantry":accepter_mythical_pantry}})
        collection.update_one({"_id":accepter}, {"$set":{"legendary_pantry":accepter_legendary_pantry}})
        
        embed = discord.Embed(description = "Trade Complete!", colour =0x0dff00)
        await message.edit(embed = embed)

          

      elif trader == accepter:
        embed = discord.Embed(description = "Trade cancelled", colour = 0xff1100)
        await message.edit(embed = embed)
      else:
        embed = discord.Embed(description = "Error: Cards aren't available", colour = 0xff1100)
        embed.set_footer(text = "You also can't trade two of the same card")
        await message.edit(embed = embed)



    




keep_alive()

client.run(os.getenv('TOKEN'))
