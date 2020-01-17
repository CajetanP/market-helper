
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
        return [ticker_data['symbol'], ticker_data['regularMarketPrice'],
        round(ticker_data['regularMarketChangePercent'], 2), ticker_data['shortName'],
        analyse_volume(ticker_data['regularMarketVolume'],
                       ticker_data['averageDailyVolume3Month']) ]

def format_ticker_info(ticker_data):
    return "{:10} | {:7} | {:5}% | {:32} | {}".format(
        ticker_data[0], ticker_data[1], ticker_data[2], ticker_data[3], ticker_data[4]
    )


def generate_url(tickers):
    return "https://query1.finance.yahoo.com/v7/finance/quote?lang=en-US&region=US&corsDomain=finance.yahoo.com&symbols={}&fields=regularMarketPrice,regularMarketChangePercent,regularMarketPreviousClose,regularMarketVolume,shortName,twoHundredDayAverage,twoHundredDayAverageChange,averageDailyVolume3Month".format(",".join(tickers))

# (165.7-159.09)/159.09

tickers = ["MSFT", "TWTR", "NKE", "RBS.L", "FORTUM.HE"]
positions = {
    "MSFT" : {
        "size": 15,
        "open_price": 159.09
    },
    "TWTR": {
        "size": 15,
        "open_price": 32.15
    },
    "NKE": {
        "size": 15,
        "open_price": 101.78
    },
    "RBS.L": {
        "size": 1120,
        "open_price": 225.0
    },
    "FORTUM.HE": {
        "size": 136,
        "open_price": 21.59
    }
}

response = requests.request("GET", generate_url(tickers))
ticker_quotes = [t for t in json.loads(response.text)['quoteResponse']['result']]

for t in ticker_quotes:
    info = get_ticker_info(t)
    print(format_ticker_info(info))
    if info[0] in positions:
        open_price = positions[info[0]]["open_price"]
        pnl = round(((info[1]/positions[info[0]]["open_price"])-1)*100, 2)
        print("{:10} | {:7} | P&L: {}% ({}%)".format("Long", open_price, round(pnl*5, 2), pnl))
    print()




