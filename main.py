import discord
from discord.ext import commands
import os
from os import environ

client = commands.Bot(command_prefix="!")
token = environ["Token"]
f = open("rules.txt", "r")
rules = f.readlines()

@client.event
async def on_ready():
    print("Bot is ready!")

@client.command(aliases = ["rules"])
async def rule(ctx, *, number):
    await ctx.send(rules[int(number) - 1])

@client.command(aliases = ["c"])
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount = 2):
    await ctx.channel.purge(limit = amount + 1)

client.run(token)
