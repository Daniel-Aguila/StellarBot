import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('TOKEN')
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello ' + message.author.name + '!')

    if message.content.startswith('!cult_hc'):
        reply = await message.channel.send('@here Cult Headcount, hosted by ' + message.author.name + '!')
        emojis = ['✅','❌']
        for emoji in emojis:
            await reply.add_reaction(emoji)

    if message.content.startswith('!o3_hc'):
        reply = await message.channel.send('@here O3 Headcount, hosted by ' + message.author.name + '!')
        emojis = ['✅','❌']
        for emoji in emojis:
            await reply.add_reaction(emoji)

    if message.content.startswith('!shatters_hc'):
        reply = await message.channel.send('@here Shatters Headcount, hosted by ' + message.author.name + '!')
        emojis = ['✅','❌']
        for emoji in emojis:
            await reply.add_reaction(emoji)

client.run(token)