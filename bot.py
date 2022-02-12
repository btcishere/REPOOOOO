import discord
from discord.ext import commands
import requests
import os
import string
import json

client = commands.Bot(command_prefix=commands.when_mentioned_or(";"))
token = "OTQxNjk5NjU5MzA1NDY3OTY2.YgZwJg.wjRucXe7c_ei2XaH5uIRoLzaq1c"
#client.remove_command('help')

@client.event
async def on_ready():
    print(f"logged in as {client.user}")
    
@client.command()
async def check(ctx, value):
        url = f"https://api.weleakinfo.to/api?value={value}&type=email&key=PDNK-CTYW-RGMJ-BRJA"
        response = requests.get(url)
        await ctx.message.reply(f"```\n%s```" % (response.text))

client.run(token)
