import discord
from discord.ext import commands
from generator import gen
from young import you


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
async def spam(ctx, yourword = "", count_word = 5):
    await ctx.send(yourword * count_word)


@bot.command()
async def word(ctx, wordls = ""):
    await ctx.send(you(wordls))
    
@bot.command()
async def helpbot(ctx):
    await ctx.send("❓💬 JAK OBSŁUGIWAĆ CHATBOTA 💬❓")
    await ctx.send("📌 - Jeśli edytujesz wiadomość, CHATBOT przyśle wiadomość przed edycją 📝")
    await ctx.send("🔑 - Jeśli wpiszesz $password (długość hasła)/jeśli nie wpiszesz liczby, hasło będzie miało 8 znaków 🔐")
    await ctx.send("👋 - Jeśli wpiszesz $hello, bot się z tobą przywita 🤖")
    await ctx.send("⚡ - Jeśli wpiszesz $spam (słowo które ma być powtórzone) (liczba powtórzeń/jeśli nie wpiszesz liczby, automatycznie zostanie wybrana liczba 5) 🌀")
    await ctx.send("📖 - Jeśli wpiszesz $word (któreś z tych słów: CRINGE, LOL, ROFL, SHEESH, CREEPY), CHATBOT napisze definicję tych słów 🧐")



    
bot.run("")
