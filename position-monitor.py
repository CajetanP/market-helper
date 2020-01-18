import json
import requests
from termcolor import colored

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
    pnl_colour = 'green' if ticker_data[2] > 0 else 'red'

    return "{:9} | {:6} | {:5}% | {} | {}".format(
        ticker_data[0], ticker_data[1],
        colored(ticker_data[2], pnl_colour),
        colored(ticker_data[3], 'blue'), ticker_data[4]
    )


def generate_url(tickers):
    return "https://query1.finance.yahoo.com/v7/finance/quote?lang=en-US&region=US&corsDomain=finance.yahoo.com&symbols={}&fields=regularMarketPrice,regularMarketChangePercent,regularMarketPreviousClose,regularMarketVolume,shortName,twoHundredDayAverage,twoHundredDayAverageChange,averageDailyVolume3Month".format(",".join(tickers))

tickers = ["MSFT", "TWTR", "NKE", "RBS.L", "FORTUM.HE"]
positions = {
    "MSFT" : {
        "size": 15,
        "open_price": 159.09,
        "open_date": "08-01-2020 15:38"
    },
    "TWTR": {
        "size": 15,
        "open_price": 32.15,
        "open_date": "07-01-2020 15:23"
    },
    "NKE": {
        "size": 15,
        "open_price": 101.78,
        "open_date": "13-01-2020 08:49"
    },
    "RBS.L": {
        "size": 1120,
        "open_price": 225.0,
        "open_date": "15-01-2020 12:41"
    },
    "FORTUM.HE": {
        "size": 136,
        "open_price": 21.59,
        "open_date": "13-01-2020 08:49"
    }
}

response = requests.request("GET", generate_url(tickers))
ticker_quotes = [t for t in json.loads(response.text)['quoteResponse']['result']]

total_pnl = 0.0
for t in ticker_quotes:
    info = get_ticker_info(t)
    print(format_ticker_info(info))
    if info[0] in positions:
        open_price = positions[info[0]]["open_price"]
        pnl = round(((info[1]/positions[info[0]]["open_price"])-1)*100, 2)
        total_pnl += pnl
        colour = 'green' if pnl > 0 else 'red'
        # TODO: enable shorts
        print("{}{:5} | {:6} | P&L: {} ({}) | {}".format(
            colored("Long", 'blue'), "", open_price,
            colored(str(round(pnl*5, 2))+"%", colour, attrs=['bold']),
            colored(str(pnl)+"%", colour), colored(positions[info[0]]["open_date"], 'yellow')
        ))
    print()

print("Total P&L: {}% ({}%)".format(round(total_pnl*5, 2), round(total_pnl, 2)))




