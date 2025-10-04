import discord
from discord.ext import commands
from generator import gen

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')
    
@bot.event
async def on_message_edit(before, after):
    if before.author == bot.user:
        return
    
    await before.channel.send("Treść wiedomości przed edycją: " + before.content)
    
@bot.command()
async def password(ctx, count_gen = 8):
    await ctx.send(gen(count_gen))
    

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem bot{bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("")
