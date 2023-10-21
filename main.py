import discord, random

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

ideas = ['Utiliza el transporte público', 'Compra productos locales', 'Consume productos ecológicos']
meme = ['meme1.jpg','meme2.jpg','meme3.jpg']

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.event
async def on_message(ctx):
    if ctx.author == bot.user:
        return
    if ctx.content.startswith('$hello'):
        await ctx.channel.send('¡Hola! Cof, cof... hay mucha contaminación, te gustaría aprender cómo ser más sostenible para evitar contaminar?')
    if ctx.content.startswith('/idea'):
        idea = random.choice(ideas)
        await ctx.channel.send(idea)
    if ctx.content.startswith('/meme'):
        mem = random.choice(meme)
        await ctx.channel.send(mem)
    else:
        await ctx.channel.send("No puedo procesar este comando, ¡lo siento!")



bot.run("TOKEN")
