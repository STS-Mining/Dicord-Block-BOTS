import json
import requests
import time
from datetime import date
import os
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from urllib3 import disable_warnings
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
datapending = 0

with open("PoolLOG.json", "w") as write_file:
    json.dump(datapending, write_file)
print("Reset LOG File Successful")

with open("PoolLOGSolo.json", "w") as write_file:
    json.dump(datapending, write_file)
print("Reset LOG Solo File Successful")

with open("PoolGOLD.json", "w") as write_file:
    json.dump(datapending, write_file)
print("Reset GOLD File Successful")

with open("PoolGOLDSolo.json", "w") as write_file:
    json.dump(datapending, write_file)
print("Reset GOLD Solo File Successful")

with open("PoolSMX.json", "w") as write_file:
    json.dump(datapending, write_file)
print("Reset SMX File Successful")

with open("PoolSMXSolo.json", "w") as write_file:
    json.dump(datapending, write_file)
print("Reset SMX Solo File Successful")

with open("PoolTZN.json", "w") as write_file:
    json.dump(datapending, write_file)
print("Reset TZN File Successful")

with open("PoolTZNSolo.json", "w") as write_file:
    json.dump(datapending, write_file)
print("Reset TZN Solo File Successful")

with open("PoolGRLC.json", "w") as write_file:
    json.dump(datapending, write_file)
print("Reset GRLC File Successful")

with open("PoolGRLCSolo.json", "w") as write_file:
    json.dump(datapending, write_file)
print("Reset GRLC Solo File Successful")
 
with open("PoolYERB.json", "w") as write_file:
    json.dump(datapending, write_file)
print("Reset YERB File Successful")

with open("PoolYERBSolo.json", "w") as write_file:
    json.dump(datapending, write_file)
print("Reset YERB Solo File Successful")

with open("PoolTTN.json", "w") as write_file:
    json.dump(datapending, write_file)
print("Reset TTN File Successful")

with open("PoolTTNSolo.json", "w") as write_file:
    json.dump(datapending, write_file)
print("Reset TTN Solo File Successful")

with open("PoolRVC.json", "w") as write_file:
    json.dump(datapending, write_file)
print("Reset RVC File Successful")

with open("PoolRVCSolo.json", "w") as write_file:
    json.dump(datapending, write_file)
print("Reset RVC Solo File Successful")

with open("pool_api.config", "r") as read_file:
    APIUrl = json.load(read_file)
try:
    response = requests.get(APIUrl, verify=False)
    dragonPoolStats = json.loads(response.text)
 

 
    lastblockLOG = dragonPoolStats["LOG"]["lastblock"]
    #lastblock_soloLOG = dragonPoolStats["LOG"]["lastblock_solo"]
    lastblockTZN = dragonPoolStats["TZN"]["lastblock"]
    #lastblock_soloTZN = dragonPoolStats["TZN"]["lastblock_solo"]
    lastblockGRLC = dragonPoolStats["GRLC"]["lastblock"]
    #lastblock_soloGRLC = dragonPoolStats["GRLC"]["lastblock_solo"]
    lastblockYERB = dragonPoolStats["YERB"]["lastblock"]
    #lastblock_soloYERB = dragonPoolStats["YERB"]["lastblock_solo"]
    lastblockSMX = dragonPoolStats["SMX"]["lastblock"]
    #lastblock_soloSMX = dragonPoolStats["SMX"]["lastblock_solo"]
    lastblockGOLD = dragonPoolStats["GOLD"]["lastblock"]
    #lastblock_soloGOLD = dragonPoolStats["GOLD"]["lastblock_solo"]
    lastblockTTN = dragonPoolStats["TTN"]["lastblock"]
    #lastblock_soloTTN = dragonPoolStats["TTN"]["lastblock_solo"]
    lastblockRVC = dragonPoolStats["RVC"]["lastblock"]
    #lastblock_soloRVC = dragonPoolStats["RVC"]["lastblock_solo"]
    lastblock_soloLOG = 0
    lastblock_soloTZN = 0
    lastblock_soloYERB = 0
    lastblock_soloSMX = 0
    lastblock_soloGOLD = 0
    lastblock_soloTTN = 0
    lastblock_soloRVC = 0
    lastblock_soloGRLC = 0
    
    with open("PoolLOG.json", "w") as write_file:
        json.dump(lastblockLOG, write_file)
    print("Updated LOG Confirmed File Successful")
        
    with open("PoolLOGSolo.json", "w") as write_file:
        json.dump(lastblock_soloLOG, write_file)
    print("Updated LOG Solo Confirmed File Successful")

    with open("PoolTZN.json", "w") as write_file:
        json.dump(lastblockTZN, write_file)
    print("Updated TZN Confirmed File Successful")
        
    with open("PoolTZNSolo.json", "w") as write_file:
        json.dump(lastblock_soloTZN, write_file)
    print("Updated TZN Solo Confirmed File Successful")
    
    with open("PoolGRLC.json", "w") as write_file:
        json.dump(lastblockGRLC, write_file)
    print("Updated GRLC Confirmed File Successful")
      
    with open("PoolGRLCSolo.json", "w") as write_file:
        json.dump(lastblock_soloGRLC, write_file)
    print("Updated GRLC Solo Confirmed File Successful")

    with open("PoolYERB.json", "w") as write_file:
        json.dump(lastblockYERB, write_file)
    print("Updated YERB Confirmed File Successful")
        
    with open("PoolYERBSolo.json", "w") as write_file:
        json.dump(lastblock_soloYERB, write_file)
    print("Updated YERB Solo Confirmed File Successful")

    with open("PoolSMX.json", "w") as write_file:
        json.dump(lastblockSMX, write_file)
    print("Updated SMX Confirmed File Successful")
        
    with open("PoolSMXSolo.json", "w") as write_file:
        json.dump(lastblock_soloSMX, write_file)
    print("Updated SMX Solo Confirmed File Successful")

    with open("PoolGOLD.json", "w") as write_file:
        json.dump(lastblockGOLD, write_file)
    print("Updated GOLD Confirmed File Successful")
        
    with open("PoolGOLDSolo.json", "w") as write_file:
        json.dump(lastblock_soloGOLD, write_file)
    print("Updated GOLD Solo Confirmed File Successful")
    
    with open("PoolTTN.json", "w") as write_file:
        json.dump(lastblockTTN, write_file)
    print("Updated TTN Confirmed File Successful")
        
    with open("PoolTTNSolo.json", "w") as write_file:
        json.dump(lastblock_soloTTN, write_file)
    print("Updated TTN Solo Confirmed File Successful")
    
    with open("PoolRVC.json", "w") as write_file:
        json.dump(lastblockRVC, write_file)
    print("Updated RVC Confirmed File Successful")
    
    with open("PoolRVCSolo.json", "w") as write_file:
        json.dump(lastblock_soloRVC, write_file)
    print("Updated RVC Solo Confirmed File Successful")
    
except requests.exceptions.HTTPError:
    print("DragonPool server HTTPError...")
    
except requests.exceptions.Timeout:
    print("DragonPool server Timeout...")

except requests.exceptions.TooManyRedirects:
    print("DragonPool server TooManyRedirects...")

except requests.exceptions.RequestException:
    print("DragonPool server RequestException...")
    
print("BLOCK FILES RESET AND UPDATED :-)")
    
