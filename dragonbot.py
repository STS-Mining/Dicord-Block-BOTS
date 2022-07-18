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
Webhook_GoldCash = "https://discord.com/api/webhooks/994894832042524735/YJvLPumbQ5_Vh8l7ITARBeQ5NhSLSD7tcULHuk9lkVpzKWX26h2UNDTE7zwzCNVj6bX7"
Webhook_WoodCoin = "https://discord.com/api/webhooks/988297126196957214/03CcM9TRVTJ7Ok-m0aY3RIDHA-2S5MPVOYBSQPIPNuHYHsvXII9hlTctSPdhlkPXaMFl"
Webhook_SafemineX = "https://discord.com/api/webhooks/994895308318318736/uFsOSTXOoBWr3v-7s7hRAYwz4Dt08fhuJSY5AlYJze82yv8HbTdH3b9ADxp7jH4w_EAR"
Webhook_Tyzen = "https://discord.com/api/webhooks/994895426085994627/YRnAAFMOlJ3G9zhYGbUIwPC5WgJ3kXI445VtRL3yzcud9199iBEv2Nx1i8aFHuhD3vex"
Webhook_Yerbas = "https://discord.com/api/webhooks/994895536563953684/GhZZXQ91swpH0GQ3oAce6AqalED98VtqwzxZMbLFnHKPnOkw3E6BcBRIIyA44UbjN0AO"
Webhook_Titancoin = "https://discord.com/api/webhooks/997317716937543690/Z5JwebWBP7yLaX35tEk2Ql_qxLgRRLdW-OpirYJprmR5zLEL07Xk9bjkvHRh6h_eKBIl"
Webhook_Ravenclassic = "https://discord.com/api/webhooks/997510378605006919/p6hkqbEYhYhBi4htKaJJ3kuNGvA5kapvXee4PuS5robv4bfwcCMDJaQr6XKsjreroWAa"
Webhook_Garlicoin = "https://discord.com/api/webhooks/997659599446491226/xpczShUFXHjsDmjZ2r0pZ3N2xoMWNgyAnksnlwLD0JKY0PVAQQz2rjGDeuDO1vX9s6ju"

#IMPORTANT===================================
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}'.format(secs)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1
        
def MAINBOT():
    print("=======DRAGONPOOL.VIP DISCORD BOT========")
    t = 10 #Seconds between discord posts - adjust as needed. !!!!Not recommended to go below 10 seconds though as discord may ban the bot.
    with open("pool_api.config", "r") as read_file:
        APIUrl = json.load(read_file)
    try:
        response = requests.get(APIUrl, verify=False)
        dragonPoolStats = json.loads(response.text)
        
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
                    ContentCOIN = "New Block Found -|- Block # " + str(lastblockCOIN)
                    data = {
                        "content": "",
                        "username": COIN_NAME + " Pool Bot",
                        "avatar_url": COIN_AVATAR,
                        "type": "rich",
                        "url": "https://dragonpool.vip/site/mining"
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
            print("----Error: No " + COIN + " Data from DragonPool...skipping check")
        

        print("BLOCK CHECKS COMPLETED")

    except requests.exceptions.HTTPError:
        print("DragonPool server HTTPError...")
    except requests.exceptions.Timeout:
        print("DragonPool server Timeout...")

    except requests.exceptions.TooManyRedirects:
        print("DragonPool server TooManyRedirects...")

    except requests.exceptions.RequestException:
        print("DragonPool server RequestException...")
#====================END OF MAINBOT()============================================================

#======START OF COIN CONFIG SHEET: COPY, PASTE & ALTER FOR EACH NEW COIN ADDED TO POOL===========
#================================================================================================
COIN_NAME = "Gold Cash"
COIN_AVATAR = "https://github.com/Debitosphere/CNC.TA.Crucial.Scripts/raw/master/coin_gold.png"
COIN = "GOLD"
COIN_DATA_FILE = "PoolGOLD.json"
Webhook_COIN = Webhook_GoldCash
MAINBOT()
#================================================================================================
COIN_NAME = "Woodcoin"
COIN_AVATAR = "https://github.com/Debitosphere/CNC.TA.Crucial.Scripts/raw/master/coin_log.png"
COIN = "LOG"
COIN_DATA_FILE = "PoolLOG.json"
Webhook_COIN = Webhook_WoodCoin
MAINBOT()
#================================================================================================
COIN_NAME = "Safeminex"
COIN_AVATAR = "https://raw.githubusercontent.com/Debitosphere/CNC.TA.Crucial.Scripts/master/coin_safeminex.png"
COIN = "SMX"
COIN_DATA_FILE = "PoolSMX.json"
Webhook_COIN = Webhook_SafemineX
MAINBOT()
#================================================================================================
COIN_NAME = "Tyzen"
COIN_AVATAR = "https://github.com/Debitosphere/CNC.TA.Crucial.Scripts/raw/master/coin_tyzen.png"
COIN = "TZN"
COIN_DATA_FILE = "PoolTZN.json"
Webhook_COIN = Webhook_Tyzen
MAINBOT()
#================================================================================================
COIN_NAME = "Yerbas"
COIN_AVATAR = "https://github.com/Debitosphere/CNC.TA.Crucial.Scripts/raw/master/coin_yerb.png"
COIN = "YERB"
COIN_DATA_FILE = "PoolYERB.json"
Webhook_COIN = Webhook_Yerbas
MAINBOT()
#================================================================================================
COIN_NAME = "Titan Coin"
COIN_AVATAR = "https://github.com/Debitosphere/CNC.TA.Crucial.Scripts/raw/master/coin_ttn.png"
COIN = "TTN"
COIN_DATA_FILE = "PoolTTN.json"
Webhook_COIN = Webhook_Titancoin
MAINBOT()
#================================================================================================
COIN_NAME = "Ravencoin Classic"
COIN_AVATAR = "https://github.com/Debitosphere/CNC.TA.Crucial.Scripts/raw/master/coin_rvn.png"
COIN = "RVC"
COIN_DATA_FILE = "PoolRVC.json"
Webhook_COIN = Webhook_Ravenclassic
MAINBOT()
#================================================================================================
COIN_NAME = "Garlicoin"
COIN_AVATAR = "https://github.com/STS-Mining/Dicord-Block-BOTS/raw/Master/garlicoin.png"
COIN = "GRLC"
COIN_DATA_FILE = "PoolGRLC.json"
Webhook_COIN = Webhook_Garlicoin
MAINBOT()
#================================================================================================
