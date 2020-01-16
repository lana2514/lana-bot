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

@client.event
async def on_message(message):
    if "FROG" in message.content.upper():
        if message.author != client.user:
            frog1 = discord.File("animals/frog/frog1.png")
            frog2 = discord.File("animals/frog/frog2.png")
            frog3 = discord.File("animals/frog/frog3.png")
            frog4 = discord.File("animals/frog/frog4.png")
            frog5 = discord.File("animals/frog/frog5.png")
            frog6 = discord.File("animals/frog/frog6.png")
            frog7 = discord.File("animals/frog/frog7.png")
            frog8 = discord.File("animals/frog/frog8.png")
            frog9 = discord.File("animals/frog/frog9.png")
            frog10 = discord.File("animals/frog/frog10.png")
            frog11 = discord.File("animals/frog/frog11.png")
            frog12 = discord.File("animals/frog/frog12.png")
            frog13 = discord.File("animals/frog/frog13.png")
            frog14 = discord.File("animals/frog/frog14.png")
            frog15 = discord.File("animals/frog/frog15.png")
            frog16 = discord.File("animals/frog/frog16.png")
            frog17 = discord.File("animals/frog/frog17.png")
            frog18 = discord.File("animals/frog/frog18.png")
            frog19 = discord.File("animals/frog/frog19.png")
            frog20 = discord.File("animals/frog/frog20.png")
            rf = random.randint(1, 20)
            if rf == 1:
                await message.channel.send(file=frog1)
            elif rf == 2:
                await message.channel.send(file=frog2)
            elif rf == 3:
                await message.channel.send(file=frog3)
            elif rf == 4:
                await message.channel.send(file=frog4)
            elif rf == 5:
                await message.channel.send(file=frog5)
            elif rf == 6:
                await message.channel.send(file=frog6)
            elif rf == 7:
                await message.channel.send(file=frog7)
            elif rf == 8:
                await message.channel.send(file=frog8)
            elif rf == 9:
                await message.channel.send(file=frog9)
            elif rf == 10:
                await message.channel.send(file=frog10)
            elif rf == 11:
                await message.channel.send(file=frog11)
            elif rf == 12:
                await message.channel.send(file=frog12)
            elif rf == 13:
                await message.channel.send(file=frog13)
            elif rf == 14:
                await message.channel.send(file=frog14)
            elif rf == 15:
                await message.channel.send(file=frog15)
            elif rf == 16:
                await message.channel.send(file=frog16)
            elif rf == 17:
                await message.channel.send(file=frog17)
            elif rf == 18:
                await message.channel.send(file=frog18)
            elif rf == 19:
                await message.channel.send(file=frog19)
            elif rf == 20:
                await message.channel.send(file=frog20)
    elif "BERD" in message.content.upper():
        if message.author != client.user:
            berd = discord.File("animals/berd.png")
            await message.channel.send(file=berd)

client.run(config['Bot']['Token'])