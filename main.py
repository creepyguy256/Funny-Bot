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
async def rule(ctx):
    await ctx.send("Rule lol")

async def hello(ctx):
    await ctx.send("Hello!")

client.run(token)
