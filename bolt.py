import json
import requests
import time
from boltiot import Bolt



SELLING_PRICE  =  17082.93

API_KEY = "your_api_key"
DEVICE_ID  = "your_device_id"
bolt = Bolt(API_KEY, DEVICE_ID)


def price_check():
    url = "https://min-api.cryptocompare.com/data/price"

    querystring = {"fsym":"BTC","tsyms":"USD"}

    response = requests.request("GET", url, params=querystring)
    response = json.loads(response.text)
    current_price = response['USD']
    return current_price

while True:
    market_price = price_check()
    print ("Market price is", market_price)
    print ("Selling price is", SELLING_PRICE)
    time.sleep(4)
    if market_price > SELLING_PRICE:
        bolt.digitalWrite("0", "HIGH")
        time.sleep(60)
        bolt.digitalWrite("0", "LOW")
