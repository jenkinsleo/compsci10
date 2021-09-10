#simple discord bot to respond to a message when one is recieved

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="/")

#event to tell us when we are succesfully connected

@bot.event
async def on_ready():
    print(f'We have logged on as: {bot.user}')


@bot.command()
async def hello(ctx):
    print(f"Command recieved from {ctx.message.author}")
    await ctx.send(f'Hello {ctx.message.author.mention} 👋')

@bot.command()
async def repeat(ctx, *, arg):
    print(f"Repeating Message: {arg}, From: {ctx.message.author}")
    await ctx.send(arg)

#grabs the token from txt document and launches the bot
f = open('token.txt', 'r')
token = f.read()
f.close()

bot.run(token)