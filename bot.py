 ##   if message.content.lower().startswith(''):
 ##       await message.channel.send('WAS BOT V2 | smth ')

import discord
import random

SLEBYIMG = ["https://cdn.discordapp.com/attachments/1008409731993444392/1008425766305923142/IMG_1660493009884.jpg", "https://cdn.discordapp.com/attachments/1008409731993444392/1008425779195019414/IMG_1660493139501.jpg","https://media.discordapp.net/attachments/1008409731993444392/1008718639001784390/orca-image--358881908.jpeg?width=318&height=424","https://media.discordapp.net/attachments/1008409731993444392/1008718639257628742/orca-image-620668752.jpeg?width=318&height=424","https://media.discordapp.net/attachments/1008409731993444392/1008718639656075324/orca-image-1241398646.jpeg?width=318&height=424","https://media.discordapp.net/attachments/1008409731993444392/1008718639895171132/orca-image--607296344.jpeg?width=565&height=424","https://media.discordapp.net/attachments/1008409731993444392/1008718640125849690/orca-image-2086803242.jpeg?width=318&height=424","https://media.discordapp.net/attachments/1008409731993444392/1008718640335556618/orca-image--1995839191.jpeg?width=318&height=424","https://media.discordapp.net/attachments/1008409731993444392/1008718640524316682/orca-image-1856284891.jpeg?width=318&height=424","https://media.discordapp.net/attachments/1008409731993444392/1008718640780161054/orca-image-131591960.jpeg?width=318&height=424","https://media.discordapp.net/attachments/1008409731993444392/1008718641501569124/received_1126954874902611.jpeg?width=430&height=424"]
RANDOMIMG = ["https://images-ext-2.discordapp.net/external/iQYmBtcjpe1ROBmZamFK9rOWjie_fh9kNuhMtK5ydzY/%3Fc%3DVjFfZGlzY29yZA/https/media.tenor.com/Sd_ATxkChjAAAAPo/schizophrenia-old-man.mp4","https://media.discordapp.net/attachments/946202718635180142/976510055795015760/r1-1.gif","https://tenor.com/view/fish-baby-fish-baby-baby-fish-pet-fish-gif-21924537","https://media.discordapp.net/attachments/1008409731993444392/1008500819655663718/received_760771041641159.gif?width=433&height=424","https://tenor.com/view/parse-black-man-eggs-gif-24198059","https://cdn.discordapp.com/attachments/965688724581142608/974427041866854440/unknown.png","https://tenor.com/view/stare-what-do-you-want-what-do-you-mean-what-you-talking-about-gif-16262754"]
TURKEY = ["https://images-ext-2.discordapp.net/external/qb7vsIf_uBso3eimI4cPmtSvZ8ViaSQLkrK5IZ6O1z8/https/media.tenor.com/tDRKrbH-9WoAAAPo/happy-turkey-dance-turkey.mp4","https://images-ext-1.discordapp.net/external/bx60i5FGDuBs8SPSWxg8Z6UnUS0N4VXV_kx1hvwM6iA/https/media.tenor.com/KVu54vakzAcAAAPo/turkey-twerk.mp4","https://images-ext-1.discordapp.net/external/Du5Ian7Fa88OJl5R7s_UABsRlTQ8h-JhqcAVYHauasw/https/media.tenor.com/dAySX_UwuIUAAAPo/kim-kardashian.mp4"]

client = discord.Client()

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
    print('Welcome to WhatASleby Bot V2')
    game = discord.Game("WAS Bot V2")
    await client.change_presence(status=discord.Status.dnd, activity=game)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('.set idle'):
        await message.channel.send('WAS BOT V2 | Set status to Idle')
        game = discord.Game("WAS Bot V2 | Idle")
        await client.change_presence(status=discord.Status.idle, activity=game)


    if message.content.lower().startswith('.set dnd'):
        await message.channel.send('WAS BOT V2 | Set status to DoNotDisturb')
        game = discord.Game("WAS Bot V2 | Do Not Disturb")
        await client.change_presence(status=discord.Status.dnd, activity=game)
    
    if message.content.lower().startswith('.set online'):
        await message.channel.send('WAS BOT V2 | Set status to Online')
        game = discord.Game("WAS Bot V2 | Online")
        await client.change_presence(status=discord.Status.online, activity=game)

    if message.content.lower().startswith('.darkweb'):
        await message.channel.send('Thy governmental Agencies tried to permanently block myself from accesing thy so called "Darker Intranet". I have downloaded a Virtual Private Network and logged back into thy site. When i recieved thy connection to thy intranet from the Virtual Private Network, I, myself have purchased a Bank Identification Number. I have "linked" (Attached an Uniform Resource Locator, so called URL of myself committing these petty, bad crimes using a popular video sharing site called YouTube. https://www.youtube.com/watch?v=ubs9b-ssuuM) a moving image slide show, also known as a Video.')

    if message.content.lower().startswith('.set offline'):
        await message.channel.send('WAS BOT V2 | Set status to Offline')
        game = discord.Game("WAS Bot V2 | Offline")
        await client.change_presence(status=discord.Status.offline, activity=game)

    if message.content.lower().startswith('.help'):
        await message.channel.send("""
        Current Commands List
        .giveaway - Hosts a Giveaway (Just say it, it uses AI to guess what you want to give away, and for how long.)
        .fling - :fling
        .turkey - Hot sexy turkey... Sexy turkey turkey gif
        .randomimg - Sends a random image
        .darkweb - The government tried to ban me off the dark web, I downloaded Tor Browser and got back in, Went got a VPN, just bought another BIN
        .set idle - Sets the bot status to Idle :yellow_circle:
        .set dnd - Sets the bot status to Do Not Disturb :red_circle:
        .set online - Sets the bot status to Online :green_circle:
        .set offline - Sets the bot status to Offline :black_circle:
        .sleby - Sends a random What A Sleby... Image
        .help - Sends the commands list
        """)

    if message.content.lower().startswith('.sleby'):
        await message.channel.send(random.choice(SLEBYIMG))

    if message.content.lower().startswith('.fling'):
        await message.channel.send('https://tenor.com/view/everyone-gif-18852241')

    if message.content.lower().startswith('.randomimg'):
        await message.channel.send(random.choice(RANDOMIMG))

    if message.content.lower().startswith('.turkey'):
        await message.channel.send(random.choice(TURKEY))

    if message.content.lower().startswith('.giveaway'):
        await message.channel.send('https://images-ext-1.discordapp.net/external/WbGr6z3UFQ9fQIEijybNbvy_xWmCEmEAzRjU7MDKbNc/https/media.discordapp.net/attachments/878680328628211775/940435184245948426/9cca3b40-e1f0-4d27-b42c-d8897b6cf95d.gif')

    if message.content.lower().startswith('you'):
        await message.channel.send('https://images-ext-1.discordapp.net/external/S-FEHv9RrFVTnv8CB71wGc7sbsC58G5fiG7cFdboBR4/https/media.discordapp.net/attachments/881615461962362933/891863679669268530/image0.gif')

client.run('get yo own token nigga')
