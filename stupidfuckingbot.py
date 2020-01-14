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
            await message.channel.send("https://media.discordapp.net/attachments/622456794500825098/666665066195845151/froge.png")

client.run(config['Bot']['Token'])