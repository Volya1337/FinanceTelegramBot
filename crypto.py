import requests


def btc():
    url = "https://api.cryptonator.com/api/full/btc-usd"
    response = requests.get(url).json()
    p = response["ticker"]["price"]
    return p


btc()


def eth():
    url = "https://api.cryptonator.com/api/full/eth-usd"
    response = requests.get(url).json()
    p = response["ticker"]["price"]
    return p


btc()


def doge():
    url = "https://api.cryptonator.com/api/full/doge-usd"
    response = requests.get(url).json()
    p = response["ticker"]["price"]
    return p


btc()
