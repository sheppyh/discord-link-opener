# discord-link-opener
Automatically open browser tabs when links matching given constraints are sent in discord channels.

# Installation and Usage
1.   Download Python 3.6.x or 3.7.x . Before installing, make sure to check “Add Python to PATH”.
2.   Once installed, open CMD and type the following two commands:
```
                     pip install discord.py[voice] 
                     pip install asyncio
```
3.    Download Link Opener: https://github.com/sheppyh/discord-link-opener
4.    Copy open.py to your desktop.
5.    Right click open.py and select “Edit with IDLE”. Once in the code, only do the following two things:
                     Add the discord channel IDs (separated by commas) that you would like to monitor.
                     Add your Discord token. (Tutorial on how to find your token: 
                        https://www.youtube.com/watch?v=tI1lzqzLQCs)
                     If you want to change keywords and blacklist, make sure to use the correct Python syntax, as in Discord for help if confused.
6.    Save the file.
7.    Wait for the bot to automatically open Chrome browser tabs when links matching given constraints are sent in the specified discord channels. 
8.    Cook.

# Requirements
asyncio, discord.py

# Operating Systems
This was designed for and only tested on windows.

