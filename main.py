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

@client.command(aliases = ["k"])
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason = "No reason provided"):
    await member.kick(reason=reason)
    await ctx.send(member.display_name + " has been kicked because " + reason)

@client.command(aliases = ["b"])
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = "No reason provided"):
    await member.ban(reason=reason)
    await ctx.send(member.display_name + " has been banned because " + reason)

@client.command(aliases = ["ub"])
@commands.has_permissions(ban_members = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split("#")

    for banned_entry in banned_users:
        user = banned_entry.user

        if(user.name, user.discriminator)==(member_name, member_disc):
            await ctx.guild.unban(user)
            await ctx.send(member_name + " has been unbanned!")
            return

    await ctx.send(member + "was not found")

client.run(token)
