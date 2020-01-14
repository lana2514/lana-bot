#i have no idea wtf i am doing

import discord
import configparser

config = configparser.ConfigParser()
config.read('settings.ini')
client = discord.Client()

@client.event
async def on_message(message):
    if "FROG" in message.content.upper():
        if message.author != client.user:
            froge = discord.File("froge.png")
            await message.channel.send(file=froge)

client.run(config['Bot']['Token'])