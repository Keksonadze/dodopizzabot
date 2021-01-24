import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix= "!")
bot.remove_command('help')

@bot.event
async def on_ready():
    print("Bot is online")
 
@bot.command(pass_content = True)
async def kek(ctx):
    await ctx.send("cock")
    
@bot.command()
async def hello(ctx): # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author # Объявляем переменную author и записываем туда информацию об авторе.

    await ctx.send(f'Hello, {author.mention}!')
       
token = os.environ.get('BOT_TOKEN')

bot.run(str(token))
