
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

def analyse_volume(volume, average_volume):
    if volume >= average_volume:
        return "Above average volume"
    else:
        return "Below average volume"

def get_ticker_info(ticker_data):
    return "{:10} | {:7} | {:5}% | {:31} | {}".format(
        ticker_data['symbol'], ticker_data['regularMarketPrice'],
        round(ticker_data['regularMarketChangePercent'], 2), ticker_data['shortName'],
        analyse_volume(ticker_data['regularMarketVolume'],
                       ticker_data['averageDailyVolume3Month']))

url = "https://query1.finance.yahoo.com/v7/finance/quote?lang=en-US&region=US&corsDomain=finance.yahoo.com&symbols=NUGT,HSBA.L,LHA.DE,UG.PA,FORTUM.HE&fields=regularMarketPrice,regularMarketChangePercent,regularMarketPreviousClose,regularMarketVolume,shortName,twoHundredDayAverage,twoHundredDayAverageChange,averageDailyVolume3Month"

response = requests.request("GET", url)
ticker_quotes = [t for t in json.loads(response.text)['quoteResponse']['result']]

for t in ticker_quotes:
    print(get_ticker_info(t))




