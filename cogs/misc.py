import discord
from discord.ext import commands

import config


class Misc(commands.Cog):
    """Miscellaneous Commands"""

    def __init__(self, client):
        self.client = client

    @commands.command(name="github")
    async def github(self, ctx):
        await ctx.send("Contribute to the Bot! https://github.com/Cryplo/BreadBot")

    @commands.command(name="servers")
    async def servers(self, ctx):
        await ctx.send("I'm in " + str(len(self.client.guilds)) + " servers.")

    @commands.command(name="invitelink")
    async def invitelink(self, ctx):
        await ctx.send('https://discord.com/api/oauth2/authorize?client_id=819653343839911956&permissions=8&scope=bot')

    @commands.command(name="updatelog")
    async def showUpdateLog(self, ctx):
        embed = discord.Embed(description=config.updateLog, colour=0x000000)
        await ctx.send(embed=embed)

    @commands.command(name="faq")
    async def faq(self, ctx):
        embed = discord.Embed(description=config.faqContent, colour=0x000000)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Misc(client))
