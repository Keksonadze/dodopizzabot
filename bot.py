import discord
from discord.ext import commands
import os

Bot = commands.Bot(command_prefix= "!")
Bot.remove_command('help')

@Bot.event
async def on_ready():
    print("Bot is online")
 
@Bot.command(pass_content = True)
    async def ping():
        await Bot.say("Pong")
       
token = os.environ.get('BOT_TOKEN')

bot.run(str(token))
