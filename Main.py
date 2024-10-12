from discord.ext import commands
import discord
import time
import psutil

BOT_TOKEN = "YourToken"
CHANNEL_ID = 1279364416013340743  

bot = commands.Bot(command_prefix=".", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Hello, I am ready!")
    channel = bot.get_channel(CHANNEL_ID)
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Cozmo App 3.4.0')) 
    await channel.send("Hello, I am ready!")

@bot.command()    
async def ping(ctx):
    await ctx.send("Pong")
    print("Ping command ran")

@bot.command()
async def vector(ctx):
    await ctx.send("Oh, that's my brother")
    print("Vector command ran")

@bot.command()
async def version(ctx):
    await ctx.send("I am on the app version 3.4.0")
    print("Version command ran")

@bot.command()
async def about(ctx):
    embed = discord.Embed(
        title='Cozmo Bot V0.1.1 alpha',
        description='Cozmo Bot v0.1.1a Made by M12Gyt and developed using Python 3.8 and discord.py and made for the anki cozmo community',
        colour=discord.Colour.blue()
    )
    await ctx.send(embed=embed)
    print("About command ran")
@bot.command()
async def ce(ctx):
    embed = discord.Embed(
        title='Cozmo',
        description='Oh, Ce is my brother also known as Cozmo Collectors Edition',
        colour=discord.Colour.blue()
    )

    embed.set_image(url='https://media.s-bol.com/qxxpEOq1lpw0/550x550.jpg')
    embed.set_footer(text='Here is a image of Cozmo Ce')
    await ctx.send(embed=embed)
    print("ce command ran")
@bot.command()
async def cpu(ctx):
    embed = discord.Embed(
        title='CPU Usage',
        description=(psutil.cpu_percent()),
        colour=discord.Colour.blue()
    )
    await ctx.send(embed=embed)
    print("CPU Usage command ran")
    print(psutil.cpu_percent())
@bot.command()
async def ram(ctx):
    embed = discord.Embed(
        title='RAM Usage',
        description=(psutil.virtual_memory()),
        colour=discord.Colour.blue()
    )
    await ctx.send(embed=embed)
    print("Ram Usage command ran")
    print(psutil.virtual_memory())
@bot.command()
async def se(ctx):
    embed = discord.Embed(
        title='Cozmo',
        description='Oh, Se is my brother also known as Cozmo Special Edition',
        colour=discord.Colour.blue()
    )

    embed.set_image(url='https://m.media-amazon.com/images/I/412ro2Z5uGL._AC_SY780_.jpg')
    embed.set_footer(text='Here is a image of Cozmo se')
    await ctx.send(embed=embed)
    print("se cmd ran")
@bot.command()
async def anki(ctx):
    embed = discord.Embed(
        title='Anki',
        description='Anki is the company who created me but they went bankrupt in 2019 and got bought out by ddl aka digital dream labs or as some call it digital scam labs',
        colour=discord.Colour.blue()
    )

    embed.set_image(url='https://media.discordapp.net/attachments/1279056698618675220/1279070007602450535/IMG_7791.png?ex=66d3c305&is=66d27185&hm=50d7cee4b611a94904d47f8a0a5e8089297bd4cf3ccb619f0542a4eb5a3c9984&=&format=webp&quality=lossless&width=996&height=747')
    embed.set_footer(text='If you want this bot you cant (:')
    await ctx.send(embed=embed)
    print("About anki ran")
@bot.command()
async def cozmo2ce(ctx):
    embed = discord.Embed(
        title='Cozmo',
        description='This is a cozmo ce 2.0 (not actualy) its a cozmo inside a vector shell',
        colour=discord.Colour.blue()
    )

    embed.set_image(url='https://cdn.discordapp.com/attachments/1215133719937941534/1279362114154401823/image.png?ex=66d42a51&is=66d2d8d1&hm=a8fa0118045e322e07b9081e85bfe689d52151d6bc24010968823ccf58dd0261&')
    embed.set_footer(text='Here is a image of a DIY cozmo 2.0 collectors edition')
    await ctx.send(embed=embed)
    print("Cozmo2ce command ran")            

                   
bot.run(BOT_TOKEN)
