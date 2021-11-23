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

cluster = pymongo.MongoClient(os.getenv('CONNECTION_URL'))
database = cluster["UserData"]
collection = database["UserData"]

def convert(seconds): 
    seconds = seconds % (24 * 3600) 
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%d:%02d:%02d" % (hour, minutes, seconds) 

def count_duplicates(x, array):
  x = x+"["+str(array[x])+"]"
  return(x)

def db_push(id,key,value):
  collection.update_one({"_id":id}, {"$push":{key:value}})
          
def db_set(id,key,value):
  collection.update_one({"_id":id}, {"$set":{key:value}})