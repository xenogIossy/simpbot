import os

routes = []

for path in os.listdir(os.getcwd()):
    routes.append(path)

import discord
from discord.ext import commands

token = os.environ["token"]
intents = discord.Intents().all()
bot = commands.Bot(command_prefix='!', intents=intents)

#client = discord.Client(intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')
    await bot.change_presence(activity=discord.Game(name="Python"))

@bot.event
async def on_message(message):
    print("Message from {0.author}: {0.content}".format(message))
    await bot.process_commands(message)

@bot.command()
async def ayo(ctx, member : commands.MemberConverter):
    await ctx.send(f"{member.mention} is SIMPING!")

bot.run(token)
