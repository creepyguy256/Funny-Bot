import discord
from discord.ext import commands
import os
from os import environ

client = commands.Bot(command_prefix="!")
token = environ["Token"]

@client.event
async def on_ready():
    print("Bot is ready!")

@client.command()
async def hello(ctx):
    await ctx.send("Hi!")

client.run(token)