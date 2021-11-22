import discord
from discord.ext import commands
class Misc(commands.Cog):
  global client
  def __init__(self,client):
    self.client = client
  @commands.command(name="github")
  async def github(self,ctx):
    await ctx.send("Contribute to the Bot! https://github.com/Cryplo/BreadBot")
def setup(client):
  client.add_cog(Misc(client))