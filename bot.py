import discord
from discord.ext import commands

token = 'ODAyNTMxMjA0MTk2MjA0NTQ1.YAwlbQ.dhmb0t9OVn4S941Z3K5nKzcxyEY'
bot = commands.Bot(command_prefix='=')

@bot.command()
async def want(ctx):
    await ctx.send("������ �����?")

@bot.command()
async def pizza(ctx):
    await ctx.send("���������?")
    
@bot.command()
async def niko(ctx):
    await ctx.send("������� ���������")
    
@bot.command()
async def dodo(ctx):
    await ctx.send("�����")
 
 
@bot.command()
async def battle1(ctx):
    await ctx.send("������ ���������? �� �����...")
    
@bot.command()
async def jenny(ctx):
    await ctx.send("��! � ����� �...")
    
@bot.command()
async def python(ctx):
    await ctx.send("����� ����(���� �����)")
    
@bot.command()
async def gay(ctx):
    await ctx.send("�����")
    
@bot.command()
async def wakeman(ctx):
    await ctx.send("�������, �� ���������")
    
@bot.command()
async def intelligence(ctx):
    await ctx.send("������������ ��������� 1 ������ 0")
    
@bot.command()
async def hello(ctx):
    author = ctx.message.author
    await ctx.send(f'������, {author.mention}!')
    
import json
import requests
@bot.command()
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/fox') 
    json_data = json.loads(response.text) 

    embed = discord.Embed(color = 0xff9900, title = 'Random Fox') 
    embed.set_image(url = json_data['link']) 
    await ctx.send(embed = embed)


bot.run(token)