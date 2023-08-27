import discord
from pprint import pprint

intents = discord.Intents.all()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
        pprint(message, depth=2)
        # pprint(message.author.guild)
        pprint(message.author.activity)

@client.event
async def on_presence_update(before, after):
    print('from')
    pprint(before.status)
    pprint(before.activity)
    pprint(before.activity.start)
    pprint(before.activity.end)
    print('to')
    pprint(after.status)
    pprint(after.activity)
    pprint(after.activity.start)
    pprint(after.activity.end)
client.run('MTEzMzI4MjA4ODQ3MzMzMzgzMA.GrTD61.9XLUW2JM3GE86v7TjYqMU-KraMmlnVMaRV0UAs')