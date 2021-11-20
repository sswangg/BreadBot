myquery = { "_id": message.author.id }
    user = collection.find(myquery)

    if message.content == prefix + ' bake' or message.content == prefix+' pantry' or message.content == prefix+' farm' or message.content == prefix+' grain' or message.content.startswith(prefix+' sell') or message.content.startswith(prefix+' buy') or message.content.startswith(prefix+' trade') or message.content.startswith(prefix+ ' bet') or message.content == prefix+' start quest' or message.content == prefix+' view quest' or message.content == prefix+' claim quest':
      if (collection.count_documents(myquery) == 0):
          post = {"_id": message.author.id, "pantry": [], "common_pantry": [], "rare_pantry":[],"mythical_pantry":[],"legendary_pantry":[],"card_cooldown":0,"grain":int(0), "farm_cooldown":0, "name":message.author.name, "quest": [], "quest_cooldown":0} 
          collection.insert_one(post)


    if message.content == prefix + ' bake' or message.content == prefix+' pantry' or message.content == prefix+' farm' or message.content == prefix+' grain' or message.content.startswith(prefix+' sell') or message.content.startswith(prefix+' buy')or message.content.startswith(prefix+' buy') or message.content.startswith(prefix+' trade') or  message.content.startswith(prefix+ ' bet') or message.content == prefix+' start quest' or message.content == prefix+' view quest' or message.content == prefix+' claim quest' or message.content == prefix+ ' test':
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


    if message.content == prefix + ' test':
      pantry = common_pantry+rare_pantry+mythical_pantry+legendary_pantry
      collection.update_one({"_id":message.author.id},{"$set":{"pantry":pantry}})