#i have no idea wtf i am doing

import os
import discord
import configparser
import random
from discord.ext import commands

config = configparser.ConfigParser()
config.read('settings.ini')
client = commands.Bot(command_prefix = 'l.')
frogdir = "animals/frog"

@client.event
async def on_ready():
    print(f'Logged in as\n{client.user.name}\n{client.user.id}\n------')

@client.command()
async def ping(ctx):
    await ctx.send(f'Ping: {round(client.latency * 1000)} ms')

@client.command()
async def frog(ctx):
    frogl = os.listdir(frogdir)
    frogp = discord.File(os.path.join(frogdir, random.choice(frogl)))
    print(os.path.join(frogdir, random.choice(frogl)))
    await ctx.send(file=frogp)

@client.event
async def on_message(message):
    if message.author != client.user:
        if "BERD" in message.content.upper():
            berdp = discord.File("animals/berd.png")
            await message.channel.send(file=berdp)
    await client.process_commands(message)

client.run(config['Bot']['Token'])