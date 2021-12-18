import discord
import random
import asyncio
from discord.ext import commands

token = "insert token here"
client = discord.Client()

@client.event
async def on_ready():
    print("Ready for deez nuts!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "ligma" in message.content.lower():
        await message.channel.send("Ligma balls")

    if "sugma" in message.content.lower():
        await message.channel.send("Sugma balls")

    if "jocelyn" in message.content.lower():
        await message.channel.send("Jocelyn deez nuts in your mouth")

    if "suck" in message.content.lower():
        await message.channel.send("Suck on deez nuts")

    if "bofa" in message.content.lower():
        await message.channel.send("Bofa deez nuts")

client.run(token)







