from termcolor import colored
import time
from datetime import datetime, timedelta

# TODO: weekends

## Forex Sessions

def tokyo_session(date):
    open = date.replace(hour=00, minute=0, second=0, microsecond=0)
    close = date.replace(hour=9, minute=0, second=0, microsecond=0)
    return (open, close)


def london_session(date):
    open = date.replace(hour=8, minute=0, second=0, microsecond=0)
    close = date.replace(hour=16, minute=0, second=0, microsecond=0)
    return (open, close)


def new_york_session(date):
    open = date.replace(hour=13, minute=0, second=0, microsecond=0)
    close = date.replace(hour=22, minute=0, second=0, microsecond=0)
    return (open, close)


def sydney_session(date):
    open = (date - timedelta(days=1)).replace(hour=20, minute=0, second=0, microsecond=0)
    close = date.replace(hour=5, minute=0, second=0, microsecond=0)
    return (open, close)

## Stock Markets

def london_stock_exchange(date):
    open = date.replace(hour=8, minute=0, second=0, microsecond=0)
    close = date.replace(hour=16, minute=30, second=0, microsecond=0)
    return (open, close)

def nasdaq_and_nyse(date):
    open = date.replace(hour=14, minute=30, second=0, microsecond=0)
    close = date.replace(hour=21, minute=00, second=0, microsecond=0)
    return (open, close)

## Utils

def clean_timedelta(delta):
    return str(delta).split(".")[0]


now = datetime.now()

london_open, london_close = london_session(now)
new_york_open, new_york_close = new_york_session(now)
tokyo = tokyo_session(now)

sydney = sydney_session(now)
next_sydney = sydney_session(now + timedelta(days=1))

# Time changer for testing
# now = now.replace(hour=15, minute=0, second=0, microsecond=0)

print("Today is", colored(now.strftime("%A, %d %B %Y"), 'yellow'))
print("The time is", colored(now.strftime("%-I:%M:%S %p"), 'yellow'), "\n")

print(colored('Forex', 'blue'), "\n")

## Sydney

print("Sydney Session (8 PM - 5 AM)")
if now < sydney[1]: # Before close
    time_to_close = sydney[1] - now
    msg = "Open, closes in {}".format(clean_timedelta(time_to_close))
    print(colored(msg, 'green'))
elif now >= sydney[1] and now <= next_sydney[0]: # Close
    time_to_close = next_sydney[0] - now
    msg = "Closed, opens in {}".format(clean_timedelta(time_to_close))
    print(colored(msg, 'red'))
else: # After close
    time_to_close = next_sydney[1] - now
    msg = "Open, closes in {}".format(clean_timedelta(time_to_close))
    print(colored(msg, 'green'))
print()

## Tokyo

print("Tokyo Session (12 AM - 9 AM)")
if now >= tokyo[0] and now <= tokyo[1]: # Open
    time_to_close = tokyo[1] - now
    msg = "Open, closes in {}".format(clean_timedelta(time_to_close))
    print(colored(msg, 'green'))
else: # After open
    next_tokyo = tokyo_session(now + timedelta(days=1))
    time_to_open = next_tokyo[0] - now
    msg = "Closed, opens in {}".format(clean_timedelta(time_to_open))
    print(colored(msg, 'red'))
print()

## London

print("London Session (8 AM - 4 PM)")
if now < london_open: # Before open
    time_to_open = london_open - now
    msg = "Closed, opens in {}".format(clean_timedelta(time_to_open))
    print(colored(msg, 'red'))
elif now >= london_open and now <= london_close: # Open
    time_to_close = london_close - now
    msg = "Open, closes in {}".format(clean_timedelta(time_to_close))
    print(colored(msg, 'green'))
else: # After open
    next_london_open, _ = london_session(now + timedelta(days=1))
    time_to_open = next_london_open - now
    msg = "Closed, opens in {}".format(clean_timedelta(time_to_open))
    print(colored(msg, 'red'))
print()

## New York

print("New York Session (1 PM - 10 PM)")
if now < new_york_open:
    time_to_open = new_york_open - now
    msg = "Closed, opens in {}".format(clean_timedelta(time_to_open))
    print(colored(msg, 'red'))
elif now >= new_york_open and now <= new_york_close:
    time_to_close = new_york_close - now
    msg = "Open, closes in {}".format(clean_timedelta(time_to_close))
    print(colored(msg, 'green'))
else:
    next_new_york = new_york_session(now + timedelta(days=1))
    time_to_open = next_new_york_open - now
    msg = "Closed, opens in {}".format(clean_timedelta(time_to_open))
    print(colored(msg, 'red'))

print()
print(colored('Stock Markets', 'blue'), "\n")

## LSE

lse = london_stock_exchange(now)

print("London Stock Exchange (8 AM - 4:30 PM)")
if now < lse[0]:
    time_to_open = lse[0] - now
    msg = "Closed, opens in {}".format(clean_timedelta(time_to_open))
    print(colored(msg, 'red'))
elif now >= lse[0] and now <= lse[1]:
    time_to_close = lse[1] - now
    msg = "Open, closes in {}".format(clean_timedelta(time_to_close))
    print(colored(msg, 'green'))
else:
    next_lse = london_stock_exchange(now + timedelta(days=1))
    time_to_open = next_lse[0] - now
    msg = "Closed, opens in {}".format(clean_timedelta(time_to_open))
    print(colored(msg, 'red'))

print()

## NASDAQ & NYSE

nasdaq_nyse = nasdaq_and_nyse(now)

print("NASDAQ & New York Stock Exchange (2:30 PM - 9 PM)")
if now < nasdaq_nyse[0]:
    time_to_open = nasdaq_nyse[0] - now
    msg = "Closed, opens in {}".format(clean_timedelta(time_to_open))
    print(colored(msg, 'red'))
elif now >= nasdaq_nyse[0] and now <= nasdaq_nyse[1]:
    time_to_close = nasdaq_nyse[1] - now
    msg = "Open, closes in {}".format(clean_timedelta(time_to_close))
    print(colored(msg, 'green'))
else:
    next_nasdaq_nyse = nasdaq_and_nyse(now + timedelta(days=1))
    time_to_open = next_new_york[0] - now
    msg = "Closed, opens in {}".format(clean_timedelta(time_to_open))
    print(colored(msg, 'red'))

