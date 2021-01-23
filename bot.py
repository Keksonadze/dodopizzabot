import json
import requests
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='=')

@bot.command()
async def want(ctx):
    await ctx.send("Õî÷åøü ïèööó?")

@bot.command()
async def pizza(ctx):
    await ctx.send("Ïåïïåðîíè?")
    
@bot.command()
async def niko(ctx):
    await ctx.send("Ñëèøêîì êðàñàó÷åã")
    
@bot.command()
async def dodo(ctx):
    await ctx.send("Ïèööà")
 
 
@bot.command()
async def battle1(ctx):
    await ctx.send("Õî÷åøü ïîäðàòüñÿ? Íó äàâàé...")
    
@bot.command()
async def jenny(ctx):
    await ctx.send("Ýé! ß ëó÷øå å¸...")
    
@bot.command()
async def python(ctx):
    await ctx.send("Ïèòîí ñèëà(õî÷ó ïèòñó)")
    
@bot.command()
async def gay(ctx):
    await ctx.send("Ìàëûø")
    
@bot.command()
async def wakeman(ctx):
    await ctx.send("Âñòàâàé, òû îáîñðàëñÿ")
    
@bot.command()
async def intelligence(ctx):
    await ctx.send("Èñêóñòâåííûé èíòåëëåêò 1 Äæåííè 0")
    
@bot.command()
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f'Äàðîâà, {author.mention}!')
    
@bot.command()
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/fox') 
    json_data = json.loads(response.text) 

    embed = discord.Embed(color = 0xff9900, title = 'Random Fox') 
    embed.set_image(url = json_data['link']) 
    await ctx.send(embed = embed)
    
token = os.environ.get('BOT_TOKEN')

bot.run(str(token))


