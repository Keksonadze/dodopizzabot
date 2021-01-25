import discord
from discord.ext import commands
import os
import json
import requests

prefix = "="
bot = commands.Bot(command_prefix= prefix)
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

    await ctx.send(f'Дарова, {author.mention}!')
    
@bot.command()
async def niko(ctx):
    await ctx.send("Слишком красаучег")
    
@bot.command()
async def pizza(ctx):
    await ctx.send("Пепперони?")
    
@bot.command()
async def hotel(ctx):
    await ctx.send("Триваго")

@bot.command()
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/fox') 
    json_data = response.json() 

    embed = discord.Embed(color = 0xff9900, title = 'Рандомная лиса') 
    embed.set_image(url = json_data['link']) 
    await ctx.send(embed = embed) 
    
@bot.command()
async def hug(ctx):
    response = requests.get('https://some-random-api.ml/animu/hug') 
    json_data = response.json() 

    embed = discord.Embed(color = 0xff9900, title = 'Обнимашки UwU') 
    embed.set_image(url = json_data['link']) 
    await ctx.send(embed = embed) 

@bot.command()
async def sus(ctx):
    await ctx.send("When impostor is sus أريد جعة😂😂😂😂")
    
@bot.command()
async def help(ctx):
    emb = discord.Embed(title= "Помощь по командам", colour = 0x39d0d6)
    emb.add_field(name = "{}Команды".format(prefix), value= "Иди в #команды-бота")
    await ctx.send(embed = emb)
       
token = os.environ.get('BOT_TOKEN')

bot.run(str(token))
