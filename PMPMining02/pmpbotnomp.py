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
    pool.request("GET", "https://pool.pmpmining.com/api/stats")
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
        poolStats = (PoolStats["pools"][POOL_NAME]["poolStats"])
        pending = (PoolStats["pools"][POOL_NAME]["blocks"]["pending"])
        totalPaid = (PoolStats["pools"][POOL_NAME]["poolStats"]["totalPaid"])
        networkBlocks = (PoolStats["pools"][POOL_NAME]["poolStats"]["networkBlocks"])
        networkSolsString = (PoolStats["pools"][POOL_NAME]["poolStats"]["networkSolsString"])
        networkDiff = (PoolStats["pools"][POOL_NAME]["poolStats"]["networkDiff"])
        pending = (PoolStats["pools"][POOL_NAME]["blocks"]["pending"])
        hashrateString = (PoolStats["pools"][POOL_NAME]["hashrateString"])

        try:
            f = open(COIN_DATA_FILE)
        except IOError:
            print("Creating File")
            with open(COIN_DATA_FILE, "w") as write_file:
                data = 0
                json.dump(data, write_file)

        with open(COIN_DATA_FILE, "r") as read_file:
            dataFilepending = json.load(read_file)

        if pending == 0:
            if dataFilepending > pending:
                with open(COIN_DATA_FILE, "w") as write_file:
                    json.dump(pending, write_file)

        if pending > 0:
            if pending > dataFilepending:
                with open(COIN_DATA_FILE, "w") as write_file:
                    json.dump(pending, write_file)

                ContentCOIN = "--- A NEW BLOCK HAS BEEN FOUND ---"  "\nPool Block # " + str(pending) + "\nPool Hashrate: " + str(hashrateString) + "\nTotal Paid By Pool: " + str(totalPaid) + "\n------------ Network Statistics ------------" + "\nNetwork Block # " + str(networkBlocks) + "\nNetwork Hashrate: " + str(networkSolsString) + "\nNetwork Difficulty: " + str(networkDiff)
                data = {
                    "content": "",
                    "username": COIN_NAME + " Pool Bot ",
                    "avatar_url": COIN_AVATAR,
                    "type": "rich",
                    "url": "https://pool.pmpmining.com/api/stats",
                }
                data["embeds"] = [{"title": ContentCOIN, "color": 1127128}]
                response = requests.post(Webhook_COIN, json=data)
                print("----Sending to Discord Bot")
                countdown(int(t))
            if pending < dataFilepending:
                with open(COIN_DATA_FILE, "w") as write_file:
                    json.dump(pending, write_file)
    except KeyError:
        print("----Error: No " + COIN + " data from PMP Mining...skipping check")

# ====================END OF MAINBOT()============================================================
print("=======PMP MINING DISCORD BOT========")
# ======START OF COIN CONFIG SHEET: COPY, PASTE & ALTER FOR EACH NEW COIN ADDED TO POOL===========
# ================================================================================================
COIN_NAME = "BitcoinZ"
COIN_AVATAR = "https://github.com/STS-Mining/Dicord-Block-BOTS/raw/main/btcz.png"
POOL_NAME = "bitcoinz"
COIN = "BTCZ"
COIN_DATA_FILE = "PoolBTCZ.json"
Webhook_COIN = Webhook_Blocknotifications
MAINBOT()
# ================================================================================================
COIN_NAME = "Zclassic"
COIN_AVATAR = "https://github.com/STS-Mining/Dicord-Block-BOTS/raw/main/zcl.png"
POOL_NAME = "zclassic"
COIN = "ZCL"
COIN_DATA_FILE = "PoolZCL.json"
Webhook_COIN = Webhook_Blocknotifications
MAINBOT()
# ================================================================================================
#COIN_NAME = "Gemlink"
#COIN_AVATAR = "https://github.com/STS-Mining/Dicord-Block-BOTS/raw/main/gemlink.png"
#POOL_NAME = 0
#COIN = "GLINK"
#COIN_DATA_FILE = "PoolGLINK.json"
#Webhook_COIN = Webhook_Blocknotifications
#MAINBOT()
# ================================================================================================

# ================================================================================================
print("====All Checks Are Now Complete====")
print("=======PMP MINING DISCORD BOT=======")
# ================================================================================================


