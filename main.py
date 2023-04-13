# bot.py
from keep_alive import keep_alive

import os
import discord
#import requests
#import json
import re
from discord.ext.commands import Bot
#from discord import FFmpegPCMAudio
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
PREFIX = os.getenv('DISCORD_PREFIX')
client = discord.Client()

client = Bot(command_prefix=list(PREFIX))


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='replit edition'))

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(f'{client.user} has connected to Discord!:\n'
          f'{client.user} is connected to the following guild:\n'
          f'{guild.name}(id: {guild.id})\n'
          f'Sometimes Life is Pain\n'
          f'for da love of god stop breakin shid\n'
          f'Riperino piperino instagramerino prejecterino')


#dafric is a F ur mum meen im trynha ;eern > Wat did u say ble
#pipshi bvg vairak zin neka es  pipshi basic shidu dara ble kas dzive viniem nepalidzes
#pispshi zinot pitonu jau ir sasniegusi vairak neka es
@client.event
async def on_message(message):
    if message.author == client.user:
        return
# Use regex to match a link starting with "https://www.instagram.com/"
    match = re.match(r'(https:\/\/www\.instagram\.com\/\S+)', message.content)

    if match:
        # Get the matched link
        link = match.group(1)
        author = message.author.name
        # Modify the link to replace "instagram" with "ddinstagram"
        modified_link = link.replace("instagram", "ddinstagram")

        # Send the modified link as a message
        await message.delete()
        await message.channel.send(f"Posted by {author}: {modified_link}")


# Use regex to match a link starting with "https://twitter.com/"
    match = re.match(r'(https:\/\/twitter\.com\/\S+)', message.content)

    if match:
        # Get the matched link
        link = match.group(1)
        author = message.author.name
        # Modify the link to replace "twitter" with "fxtwitter"
        modified_link = link.replace("twitter", "fxtwitter")

        # Send the modified link as a message
        await message.delete()
        await message.channel.send(f"Posted by {author}: {modified_link}")

    if message.content.startswith('$hello'):
        await message.channel.send('Whoever summoned me is gay')
        if message.content.startswith('$hello'):
            await message.delete()

    if message.content.startswith('$bruh'):
        await message.channel.send(
            'https://tenor.com/view/bruh-bye-ciao-gif-5156041')
        if message.content.startswith('$bruh'):
            await message.delete()

    if message.content.startswith('$gang'):
        await message.channel.send(
            'https://media.giphy.com/media/cVSWa1PDcToGc/giphy.gif')
        if message.content.startswith('$gang'):
            await message.delete()

    if message.content.startswith('$slap'):
        await message.channel.send(
            'https://tenor.com/view/el-risitas-come-on-come-on-man-mustache-serious-gif-17362553'
        )
        if message.content.startswith('$slap'):
            await message.delete()

    if message.content.startswith('$pain'):
        await message.channel.send(
            'https://tenor.com/view/hide-the-pain-harold-gif-10575677')
        if message.content.startswith('$pain'):
            await message.delete()

    if message.content.startswith('e'):
        await message.channel.send('ko e ble')

    if message.content.startswith('dirst'):
        await message.channel.send('nedirsies daudz te ja')

    if message.content.startswith('pips'):
        await message.channel.send('pats ne labaks')

    if message.content.startswith('k'):
        await message.channel.send('ko tu rej')

    #if message.author.id == 242671461926567937:
    #  await message.channel.send('ej prom')

    #if message.content.startswith('k'): #pidarasi #sam takoi
    #await message.channel.send('***ricii sachini kvadru***') #That is just a step too far
    #May you rest in peace...
    #if message.content.startswith('e'):
    #await message.delete()

print(
    'long time long time'
)  # <- why this not work?????? cuz ur brain smol lmao <- faken tru men not funi
# This has been signed by LifeDeLicious ;)
# Nice

#o privet mairi (nice) sakuma domaju nice bus
#im sorry kas te ble notiek neazsarnojam ludzu commentus un nohuja pa kuru laiku ble Long time long time suka 74 lines

#yall cant add anythin other then ble check n send
#Blyats vot nevajag pythona mateni krucit ble te ja
print('laipni lugti jauniesi tikko pargajam pari loopam')
#      a = 2
#       while a == 2: #jaunieshi mes te neplusojam aritmetisko
#        print('ge')   #ar ko atskiras "" no '' : huizin vecit
#   if a == 3 :
#    print('lopu nav iespejams salauzt')
print('phew tikam paari')
#ahueli ko notika ar manu ble pakarotshanu
#Pog kkas vairak outputojas
#sha bots succos
keep_alive()
client.run(TOKEN)
