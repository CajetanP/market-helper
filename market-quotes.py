from alpha_vantage.timeseries import TimeSeries

import json
import requests
import math

def sma(quotes):
    return round(sum(quotes)/len(quotes), 4)

# TODO: refactoring here
def ema(s, n):
    s = s[::-1]
    ema = []
    j = 1

    sma = sum(s[:n]) / n
    multiplier = 2 / float(1 + n)
    ema.append(sma)

    #EMA(current) = ( (Price(current) - EMA(prev) ) x Multiplier) + EMA(prev)
    ema.append(( (s[n] - sma) * multiplier) + sma)

    for i in s[n+1:]:
        tmp = ( (i - ema[j]) * multiplier) + ema[j]
        j = j + 1
        ema.append(tmp)

    return round(ema[-1], 5)

def wma(quotes):
    n = len(quotes)
    divisor = n * (n+1) / 2

    result = 0
    for i, x in enumerate(quotes):
        result += (x * (n-i))

    return round(result/divisor, 5)

# def hma(quotes):
    # wma1 = wma(quotes[::len(quotes)/2]) * 2
    # wma1 = wma(quotes)


def get_quotes(ticker, interval="5min", length=200, api_key="QRSOBTILAOURK4N4"):
    ts = TimeSeries(key=api_key)
    data, meta_data = ts.get_intraday(ticker, interval=interval, outputsize='full')

    quotes = []
    for x in data:
        if len(quotes) >= length:
            break
        quotes.append(float(data[x]['4. close']))
    return quotes

def assess(ticker, key="QRSOBTILAOURK4N4"):
    quotes = get_quotes(ticker, api_key=key)


    last_price = quotes[0]
    averages = [ema(quotes, 12), ema(quotes, 26), sma(quotes[:50]), sma(quotes[:100]),
                sma(quotes), wma(quotes)
    ]

    if all(last_price < x for x in averages):
        print(ticker, "Below all")
    elif all(last_price > x for x in averages):
        print(ticker, "Above all")
    else:
        print(ticker, "Mixed")


assess("EURUSD")
assess("GBPUSD")
assess("AUDUSD")

assess("GOLD")
assess("SPY")

# assess("BTCUSD", key="AV89P4CT5WIULHJY")
# assess("MSFT", key=)
# assess("NFLX")


url = "https://www.alphavantage.co/query?function=WMA&symbol=USDCAD&interval=5min&time_period=200&series_type=close&apikey=AV89P4CT5WIULHJY"

response = requests.request("GET", url, verify='cacert.pem')
data = json.loads(response.text)
print(data)

# last_refreshed = data['Meta Data']["3: Last Refreshed"][:-3]
# value = data['Technical Analysis: WMA'][last_refreshed]

print()
print(value)
