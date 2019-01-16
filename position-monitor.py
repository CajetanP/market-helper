
# Some data persistence for storing tickers to watch
# Processing yahoo finance ticker data to fetch P&L
# Live refresh (?)
#
#
#
#
#


import json
import requests

print("Position monitor\n")

def get_ticker_info(ticker_data):
    return "{} {}".format(ticker_data['symbol'], ticker_data['regularMarketPrice'])

url = "https://query1.finance.yahoo.com/v7/finance/quote?lang=en-US&region=US&corsDomain=finance.yahoo.com&symbols=NUGT,HSBA.L,LHA.DE,UG.PA,FORTUM.HE&fields=regularMarketPrice"

response = requests.request("GET", url)
ticker_quotes = [t for t in json.loads(response.text)['quoteResponse']['result']]

for t in ticker_quotes:
    print(get_ticker_info(t))




