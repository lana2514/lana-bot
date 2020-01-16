#i have no idea wtf i am doing

import os
import discord
import configparser
import random

config = configparser.ConfigParser()
config.read('settings.ini')
client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as\n{client.user.name}\n{client.user.id}\n------')


frogdir = "animals/frog"
@client.event
async def on_message(message):
    if message.author != client.user:
        if "FROG" in message.content.upper():
            frogs = os.listdir(frogdir)
            frog = discord.File(os.path.join(frogdir, random.choice(frogs)))
            await message.channel.send(file=frog)
        elif "BERD" in message.content.upper():
            berd = discord.File("animals/berd.png")
            await message.channel.send(file=berd)

client.run(config['Bot']['Token'])