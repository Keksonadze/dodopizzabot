import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix= "!")
bot.remove_command('help')

@bot.event
async def on_ready():
    print("Bot is online")
 
@bot.command(pass_content = True)
async def kek():
    await Bot.say("cock")
       
token = os.environ.get('BOT_TOKEN')

bot.run(str(token))
