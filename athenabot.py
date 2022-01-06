import json
import os
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$', activity=discord.Activity(name="music", type=discord.ActivityType.listening), status=discord.Status.online)

#output a string when bot goes online
@bot.event
async def on_ready():
    print('Logged in as: {0.user.name}, {0.user.id}'.format(bot))

# Opens token.json file and saves the token value to a variable
with open('token.json') as f:
    bot.token = json.load(f)["token"]

# Loads every file in the cogs folder
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        try:
            bot.load_extension(f'cogs.{filename[:-3]}')
        except commands.NoEntryPointError:
            pass

# Start the bot
bot.run(bot.token)
