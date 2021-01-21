import constants
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

client.run(constants.token)