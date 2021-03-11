import webbrowser
import asyncio
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import re

'''
original by cleary#6546 // @preorderd
fork by sheppy#7645 - specifically for PartAlert
'''

#pylint: disable=anomalous-backslash-in-string

#enter token of discord account that has access to watch specified channels
token = ''

#prompt user enter keywords to check for in links
keywords = ['amazon', 'partalert.net', 'nvidia.com', 'nvidia.co.uk']

#prompt user to enter negative keywords that will prevent a browser window from opening to have no blacklisted words, press enter right away
blacklist = []

#enter channel id(s) where links would be picked up (monitor channel id) seperated by commas. these should be ints
channels = [
    805107870546133023, # PartAlert #robynhood-alerts
    806954441056059422, # PartAlert #rtx3060
    802674527850725377, # PartAlert #rtx3060ti
    802674552541806662, # PartAlert #rtx3070
    802674584473567303, # PartAlert #rtx3080
    802674601519611925, # PartAlert #rtx3090
    802674384120446996 # PartAlert #founders-edition 
]

client = Bot('adawd@@#^^')
client.remove_command('help')

global start_count
start_count = 0

#check for keywords and blacklisted words in message urls and open browser if conditions are met
async def check_urls(urls):
    for url in urls:
        if any(x in url.lower() for x in keywords) and all(x not in url.lower() for x in blacklist):
            # TODO: This is a big workaround.... fix the source
            # For some reason a ', is added to the end of embedded links. Remove it if present
            if url[-2:] == "',":
                print("Fixing this URL!...")
                url = url[:-2]

            #enter path to chrome here, for windows 10, this should work
            webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(url)
            #webbrowser.get("C:/Program Files (x86)/BraveSoftware/Brave-Browser/Application/brave.exe %s").open(url)
            print(f'Opened {url}')

@client.event
async def on_message(message):
    global start_count
    # temporary bypass to weird d.py cacheing issue
    # only print this info on the first time the client launches. this is due to d.py calling on_ready() after the bot regains connection
    if start_count == 0:
        print('\n{} is ready to cop some restocks.\n'.format(str(client.user)))
        if len(keywords) >= 1 and keywords[0] != '':
            print('Watching for keywords {}.\n'.format(', '.join(keywords)))
        else:
            print('No keywords have been provided.\n')
        if len(blacklist) > 0:
            print('Ignoring keywords {}.\n'.format(', '.join(blacklist)))
        else:
            print('No keywords currently blacklisted.\n')
        start_count += 1
    else:
        if message.channel.id in channels:
            # Below checks for URLs in embedded messages (like PartAlink alerts)
            if message.embeds:
                for embed in message.embeds:
                    toembed = embed.to_dict()
                    if str(toembed['type']).lower() != 'link':
                        try:
                            for field in toembed['fields']:#
                                # The following original code wasn't working for urls containing #
                                #urls = re.findall("(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+",str(field))
                                # Replaced with:
                                # TODO: I put a (probably) bad regex in here trying to filter off the ', with '?,?
                                urls = re.findall(r"(https?://[^\s]+)'?,? ", str(field)) 
                                if urls:
                                    await check_urls(urls)
                        except:
                            pass
            # Below just checks message content 
            if message.content != '':
                # The following original code wasn't working for urls containing #
                #urls = re.findall("(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+",message.content)
                # Replaced with:
                urls = re.findall(r'(https?://[^\s]+)', message.content)
                if urls:
                    await check_urls(urls)

client.run(token,bot=False)
