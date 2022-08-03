#Author: Debitosphere
#Discord: https://discord.gg/zbdTmA6sxw
#Readme: This bot is designed specifically for the DragonPool.vip API
#Readme: If any changes need to be made, just contact me on Discord
#Readme: and I'll gladly take a look and make alterations to the code
#Readme: If anyone wants a bot coded for their Pool's API, I can
#Readme: investigate their API and come up with something to suit.
#Readme: To add new coin to script, add webhook, add coin to coin-config sheet, add .png image to github and link to this script. Make changes to resetbot also. 
#Readme: Make sure .json files are unlocked in directory and in read/write format.
import ssl
import json
import requests
import time
import urllib3
import os
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from urllib3 import disable_warnings
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
#IMPORTANT: Change the following lines to point to the correct webhooks for the bot channels in discord
Webhook_Blocknotifications = "https://discord.com/api/webhooks/1001701684881412119/X_3GSOvXa6oikcd66lS2YiF6ngunZ_2-uVhP7NPP-juPvMncvc3P1ohymxAVMU6wFrAH"
#IMPORTANT===================================
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}'.format(secs)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1
with open("pool_api.config", "r") as read_file:
    APIUrl = json.load(read_file)
try:
    response = requests.get(APIUrl, verify=False)
    dragonPoolStats = json.loads(response.text)
except requests.exceptions.HTTPError:
    print("PMPMining server HTTPError...")
except requests.exceptions.Timeout:
    print("PMPMining server Timeout...")
except requests.exceptions.TooManyRedirects:
    print("PMPMining server TooManyRedirects...")
except requests.exceptions.RequestException:
    print("PMPMining server RequestException...")
def MAINBOT():
    t = 20 #Seconds between discord posts - adjust as needed. !!!!Not recommended to go below 10 seconds though as discord may ban the bot.

    print("Checking " + COIN_NAME + " BLOCKS")
    try:
        lastblockCOIN = dragonPoolStats[COIN]["lastblock"]
        try:
            f = open(COIN_DATA_FILE)
        except IOError:
            print("Creating File")
            with open(COIN_DATA_FILE, "w") as write_file:
                data = 0
                json.dump(data, write_file)
                
        with open(COIN_DATA_FILE, "r") as read_file:
            dataFilepending = json.load(read_file)
            
        if lastblockCOIN == 0:
            if dataFilepending > lastblockCOIN:
                with open(COIN_DATA_FILE, "w") as write_file:
                    json.dump(lastblockCOIN, write_file)
                    
        if lastblockCOIN > 0:
            if lastblockCOIN > dataFilepending:
                with open(COIN_DATA_FILE, "w") as write_file:
                    json.dump(lastblockCOIN, write_file)
                ContentCOIN = "New Block Found | Block # " + str(lastblockCOIN)
                data = {
                    "content": "",
                    "username": COIN_NAME + " Pool Bot",
                    "avatar_url": COIN_AVATAR,
                    "type": "rich",
                    "url": "https://api.pmpmining.com/pools"
                }
                data["embeds"] = [
                    {
                    "title" : ContentCOIN,
                    "color": 1127128
                    }
                ]
                response = requests.post(Webhook_COIN, json=data)
                print("----Sending to Discord Bot")
                countdown(int(t))
            if lastblockCOIN < dataFilepending:
                with open(COIN_DATA_FILE, "w") as write_file:
                    json.dump(lastblockCOIN, write_file)
    except KeyError:
        print("----Error: No " + COIN + " Data from PMPMining...skipping check")

#====================END OF MAINBOT()============================================================
print("=======PMPMining.com DISCORD BOT========")
#======START OF COIN CONFIG SHEET: COPY, PASTE & ALTER FOR EACH NEW COIN ADDED TO POOL===========
#================================================================================================
COIN_NAME = "Gemlink"
COIN_AVATAR = ""
COIN = "GLINK"
COIN_DATA_FILE = "PoolGLINK.json"
Webhook_COIN = Webhook_Blocknotifications
MAINBOT()
#================================================================================================
COIN_NAME = "Woodcoin"
COIN_AVATAR = "https://github.com/Debitosphere/CNC.TA.Crucial.Scripts/raw/master/coin_log.png"
COIN = "LOG"
COIN_DATA_FILE = "PoolLOG.json"
Webhook_COIN = Webhook_Blocknotifications
MAINBOT()
#================================================================================================
COIN_NAME = "Bitcoin"
COIN_AVATAR = ""
COIN = "BTC"
COIN_DATA_FILE = "PoolBTC.json"
Webhook_COIN = Webhook_Blocknotifications
MAINBOT()
#================================================================================================
COIN_NAME = "Bitcoin Gold"
COIN_AVATAR = ""
COIN = "BTG"
COIN_DATA_FILE = "PoolBTG.json"
Webhook_COIN = Webhook_Blocknotifications
MAINBOT()
#================================================================================================
COIN_NAME = "BitcoinZ"
COIN_AVATAR = ""
COIN = "BTCZ"
COIN_DATA_FILE = "PoolBTCZ.json"
Webhook_COIN = Webhook_Blocknotifications
MAINBOT()
#================================================================================================
COIN_NAME = "Ethereum Classic"
COIN_AVATAR = ""
COIN = "ETC"
COIN_DATA_FILE = "PoolETC.json"
Webhook_COIN = Webhook_Blocknotifications
MAINBOT()
#================================================================================================
COIN_NAME = "Ravencoin"
COIN_AVATAR = ""
COIN = "RVN"
COIN_DATA_FILE = "PoolRVN.json"
Webhook_COIN = Webhook_Blocknotifications
MAINBOT()
#================================================================================================
COIN_NAME = "Flux"
COIN_AVATAR = ""
COIN = "FLUX"
COIN_DATA_FILE = "PoolFLUX.json"
Webhook_COIN = Webhook_Blocknotifications
MAINBOT()
#================================================================================================
COIN_NAME = "Freecash"
COIN_AVATAR = ""
COIN = "FCH"
COIN_DATA_FILE = "PoolFCH.json"
Webhook_COIN = Webhook_Blocknotifications
MAINBOT()
#================================================================================================
COIN_NAME = "Litecoincash"
COIN_AVATAR = ""
COIN = "LCC"
COIN_DATA_FILE = "PoolLCC.json"
Webhook_COIN = Webhook_Blocknotifications
MAINBOT()
#================================================================================================
COIN_NAME = "Maza"
COIN_AVATAR = ""
COIN = "MAZA"
COIN_DATA_FILE = "PoolMAZA.json"
Webhook_COIN = Webhook_Blocknotifications
MAINBOT()
#================================================================================================
COIN_NAME = "Neoxa"
COIN_AVATAR = ""
COIN = "NEOX"
COIN_DATA_FILE = "PoolNEOX.json"
Webhook_COIN = Webhook_Blocknotifications
MAINBOT()
#================================================================================================
COIN_NAME = "Optical Bitcoin"
COIN_AVATAR = ""
COIN = "OBTC"
COIN_DATA_FILE = "PoolOBTC.json"
Webhook_COIN = Webhook_Blocknotifications
MAINBOT()
#================================================================================================
COIN_NAME = "Zclassic"
COIN_AVATAR = ""
COIN = "ZCL"
COIN_DATA_FILE = "PoolZCL.json"
Webhook_COIN = Webhook_Blocknotifications
MAINBOT()
#================================================================================================
COIN_NAME = "Zero"
COIN_AVATAR = ""
COIN = "ZER"
COIN_DATA_FILE = "PoolZER.json"
Webhook_COIN = Webhook_Blocknotifications
MAINBOT()
#================================================================================================
COIN_NAME = "Bitcoin Atom"
COIN_AVATAR = ""
COIN = "BCA"
COIN_DATA_FILE = "PoolBCA.json"
Webhook_COIN = Webhook_Blocknotifications
MAINBOT()
#================================================================================================













#================================================================================================
print("BLOCK CHECKS COMPLETED")
#================================================================================================
