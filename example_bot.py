import discord
print("Working!")
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('honk'):
        await message.channel.send("`honk`")

client.run('ODAwOTE0MDc5NjgxNDc4Njg2.YAZDXA.K1cZM1gV9iU_kXotTEixOAthsP7fw')