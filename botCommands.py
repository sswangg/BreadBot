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
  
