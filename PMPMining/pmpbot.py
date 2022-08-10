# Author: STS-Mining
# Readme: To add new coin to script, add webhook, add coin to coin-config sheet, add .png image to github and link to this script. 
# Readme: Make sure .json files are unlocked in directory and in read/write format.

import json
import requests
import time
import os
import certifi #print
import ssl
from urllib3 import PoolManager
from urllib3.util.ssl_ import create_urllib3_context
ctx = create_urllib3_context()
ctx.load_default_certs()
ctx.options |= ssl.OP_ENABLE_MIDDLEBOX_COMPAT
with PoolManager(ssl_context=ctx) as pool:
    pool.request("GET", "https://api.pmpmining.com/pools")
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
# IMPORTANT: Change the following lines to point to the correct webhooks for the bot channels in discord
Webhook_Blocknotifications = "https://discord.com/api/webhooks/1001701684881412119/X_3GSOvXa6oikcd66lS2YiF6ngunZ_2-uVhP7NPP-juPvMncvc3P1ohymxAVMU6wFrAH"
# IMPORTANT===================================
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = "{:02d}".format(secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

with open("pool_api.config", "r") as read_file:
    APIUrl = json.load(read_file)

try:
    response = requests.get(APIUrl, verify=True)
    PoolStats = json.loads(response.text)

except requests.exceptions.HTTPError:
    print("PMP Mining server HTTPError...")
except requests.exceptions.Timeout:
    print("PMP Mining server Timeout...")
except requests.exceptions.TooManyRedirects:
    print("PMP Mining server TooManyRedirects...")
except requests.exceptions.RequestException:
    print("PMP Mining server RequestException...")

def MAINBOT():
    t = 10  # Seconds between discord posts - adjust as needed. !!!!Not recommended to go below 10 seconds though as discord may ban the bot.

    print("Checking " + COIN_NAME + " Blocks")
    try:
        totalBlocks = (PoolStats["pools"][CoinIndex]["totalBlocks"])
        networkStats = (PoolStats["pools"][CoinIndex]["networkStats"])
        blockHeight = (PoolStats["pools"][CoinIndex]["networkStats"]["blockHeight"])
        lastPoolBlockTime = (PoolStats["pools"][CoinIndex]["lastPoolBlockTime"])
        networkHashrate = (PoolStats["pools"][CoinIndex]["networkStats"]["networkHashrate"])
        networkDifficulty = (PoolStats["pools"][CoinIndex]["networkStats"]["networkDifficulty"])
        poolHashrate = (PoolStats["pools"][CoinIndex]["poolStats"]["poolHashrate"])
        totalPaid = (PoolStats["pools"][CoinIndex]["totalPaid"])

        try:
            f = open(COIN_DATA_FILE)
        except IOError:
            print("Creating File")
            with open(COIN_DATA_FILE, "w") as write_file:
                data = 0
                json.dump(data, write_file)

        with open(COIN_DATA_FILE, "r") as read_file:
            dataFilepending = json.load(read_file)

        if totalBlocks == 0:
            if dataFilepending > totalBlocks:
                with open(COIN_DATA_FILE, "w") as write_file:
                    json.dump(totalBlocks, write_file)

        if totalBlocks > 0:
            if totalBlocks > dataFilepending:
                with open(COIN_DATA_FILE, "w") as write_file:
                    json.dump(totalBlocks, write_file)

                ContentCOIN = "--- A NEW BLOCK HAS BEEN FOUND ---"  "\nPool Block # " + str(totalBlocks) + "\nPool Hashrate: " + str(poolHashrate) + "\nTotal Paid By Pool: " + str(totalPaid) + "\n------------ Network Statistics ------------" + "\nNetwork Block # " + str(blockHeight) + "\nNetwork Hashrate: " + str(networkHashrate) + "\nNetwork Difficulty: " + str(networkDifficulty)
                data = {
                    "content": "",
                    "username": COIN_NAME + " Pool Bot ",
                    "avatar_url": COIN_AVATAR,
                    "type": "rich",
                    "url": "https://api.pmpmining.com/pools",
                }
                data["embeds"] = [{"title": ContentCOIN, "color": 1127128}]
                response = requests.post(Webhook_COIN, json=data)
                print("----Sending to Discord Bot")
                countdown(int(t))

            if totalBlocks < dataFilepending:
                with open(COIN_DATA_FILE, "w") as write_file:
                    json.dump(totalBlocks, write_file)

    except KeyError:
        print("----Error: No " + COIN + " data from PMP Mining... skipping check")
# ====================END OF MAINBOT()============================================================
print("=======PMP MINING DISCORD BOT========")
# ======START OF COIN CONFIG SHEET: COPY, PASTE & ALTER FOR EACH NEW COIN ADDED TO POOL===========
# ================================================================================================
COIN_NAME = "Litecoin Cash"
COIN_AVATAR = "https://github.com/STS-Mining/Dicord-Block-BOTS/raw/main/litcoincash.png"
CoinIndex = 0
COIN = "LCC"
COIN_DATA_FILE = "PoolLCC.json"
Webhook_COIN = Webhook_Blocknotifications
MAINBOT()
# ================================================================================================
COIN_NAME = "Bitcoin Gold"
COIN_AVATAR = "https://github.com/STS-Mining/Dicord-Block-BOTS/raw/main/bitcoingold.png"
CoinIndex = 1
COIN = "BTG"
COIN_DATA_FILE = "PoolBTG.json"
Webhook_COIN = Webhook_Blocknotifications
MAINBOT()
# ================================================================================================
COIN_NAME = "Optical BTC"
COIN_AVATAR = "https://github.com/STS-Mining/Dicord-Block-BOTS/raw/main/opticalbitcoin.png"
CoinIndex = 2
COIN = "OBTC"
COIN_DATA_FILE = "PoolOBTC.json"
Webhook_COIN = Webhook_Blocknotifications
MAINBOT()
# ================================================================================================
COIN_NAME = "Maza"
COIN_AVATAR = "https://github.com/STS-Mining/Dicord-Block-BOTS/raw/main/mazacoin.png"
CoinIndex = 3
COIN = "MAZA"
COIN_DATA_FILE = "PoolMAZA.json"
Webhook_COIN = Webhook_Blocknotifications
MAINBOT()
# ================================================================================================
COIN_NAME = "Vertcoin"
COIN_AVATAR = "https://github.com/STS-Mining/Dicord-Block-BOTS/raw/main/vtc.png"
CoinIndex = 4
COIN = "VTC"
COIN_DATA_FILE = "PoolVTC.json"
Webhook_COIN = Webhook_Blocknotifications
MAINBOT()
# ================================================================================================
#COIN_NAME = "Gemlink"
#COIN_AVATAR = "https://github.com/STS-Mining/Dicord-Block-BOTS/raw/coin-avatars/gemlink.png"
#CoinIndex = 0
#COIN = "GLINK"
#COIN_DATA_FILE = "PoolGLINK.json"
#Webhook_COIN = Webhook_Blocknotifications
#MAINBOT()
# ================================================================================================
print("====All Checks Are Now Complete====")
print("=======PMP MINING DISCORD BOT=======")
# ================================================================================================
