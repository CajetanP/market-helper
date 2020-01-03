from termcolor import colored
import time
from datetime import datetime, timedelta

# TODO: weekends

city = "Auckland"
# city = "Glasgow"

def session_info(session, open, close):
    open_hour = 12 if open.hour == 0 else open.hour
    close_hour = 12 if close.hour == 0 else close.hour

    starttime = "{} PM".format(open_hour-12) if open_hour > 12 else "{} AM".format(open_hour)
    endtime = "{} PM".format(close_hour-12) if close_hour > 12 else "{} AM".format(close_hour)

    return "{} Session ({} - {})".format(session, starttime, endtime)

## Forex Sessions

def tokyo_session(date, city="Glasgow"):
    open = date.replace(hour=00, minute=0, second=0, microsecond=0)
    close = date.replace(hour=9, minute=0, second=0, microsecond=0)

    if (city == "Auckland"):
        open = open + timedelta(hours=13)
        close = close + timedelta(hours=13)

    return (open, close)


def london_session(date, city="Glasgow"):
    open = date.replace(hour=8, minute=0, second=0, microsecond=0)
    close = date.replace(hour=16, minute=0, second=0, microsecond=0)

    if (city == "Auckland"):
        open = open + timedelta(hours=13)
        close = close + timedelta(hours=13)

    return (open, close)


def new_york_session(date, city="Glasgow"):
    open = date.replace(hour=13, minute=0, second=0, microsecond=0)
    close = date.replace(hour=22, minute=0, second=0, microsecond=0)

    if (city == "Auckland"):
        open = open + timedelta(hours=13)
        close = close + timedelta(hours=13)

    return (open, close)


def sydney_session(date, city="Glasgow"):
    open = (date - timedelta(days=1)).replace(hour=20, minute=0, second=0, microsecond=0)
    close = date.replace(hour=5, minute=0, second=0, microsecond=0)

    if (city == "Auckland"):
        open = open + timedelta(hours=13)
        close = close + timedelta(hours=13)

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

if (city == "Auckland"):
    now = now + timedelta(hours=13)

london_open, london_close = london_session(now, city)
new_york_open, new_york_close = new_york_session(now, city)
tokyo_open, tokyo_close = tokyo_session(now, city)

sydney_open, sydney_close = sydney_session(now, city)
next_sydney_open, next_sydney_close = sydney_session(now + timedelta(days=1), city)

# Time changer for testing
# now = now.replace(hour=15, minute=0, second=0, microsecond=0)

print("Today is", colored(now.strftime("%A, %d %B %Y"), 'yellow'))
print("The time is", colored(now.strftime("%-I:%M:%S %p"), 'yellow'), "\n")

print(colored('Forex', 'blue'), "\n")

## Sydney

if city == "Auckland":
    print("Sydney Session (9 AM - 6 PM)")
else:
    print("Sydney Session (8 PM - 5 AM)")

if now < sydney_close: # Before close
    time_to_close = sydney_close - now
    msg = "Open, closes in {}".format(clean_timedelta(time_to_close))
    print(colored(msg, 'green'))
elif now >= sydney_close and now <= next_sydney_open: # Close
    time_to_close = next_sydney_open - now
    msg = "Closed, opens in {}".format(clean_timedelta(time_to_close))
    print(colored(msg, 'red'))
else: # After close
    time_to_close = next_sydney_close - now
    msg = "Open, closes in {}".format(clean_timedelta(time_to_close))
    print(colored(msg, 'green'))
print()

## Tokyo

print(session_info("Tokyo", tokyo_open, tokyo_close))
if now >= tokyo_open and now <= tokyo_close: # Open
    time_to_close = tokyo_close - now
    msg = "Open, closes in {}".format(clean_timedelta(time_to_close))
    print(colored(msg, 'green'))
else: # After open
    next_tokyo_open, next_tokyo_close = tokyo_session(now + timedelta(days=1))
    time_to_open = next_tokyo_open - now
    msg = "Closed, opens in {}".format(clean_timedelta(time_to_open))
    print(colored(msg, 'red'))
print()

## London

if city == "Auckland":
    print("London Session (9 PM - 5 AM)")
else:
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

# print(new_york_open.hour)

if city == "Auckland":
    print("New York Session (2 AM - 11 AM)")
else:
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

lse_open, lse_close = london_stock_exchange(now)

print("London Stock Exchange (8 AM - 4:30 PM)")
if now < lse_open:
    time_to_open = lse_open - now
    msg = "Closed, opens in {}".format(clean_timedelta(time_to_open))
    print(colored(msg, 'red'))
elif now >= lse_open and now <= lse_close:
    time_to_close = lse_close - now
    msg = "Open, closes in {}".format(clean_timedelta(time_to_close))
    print(colored(msg, 'green'))
else:
    next_lse = london_stock_exchange(now + timedelta(days=1))
    time_to_open = next_lse[0] - now
    msg = "Closed, opens in {}".format(clean_timedelta(time_to_open))
    print(colored(msg, 'red'))

print()

## NASDAQ & NYSE

nasdaq_nyse_open, nasdaq_nyse_close = nasdaq_and_nyse(now)

print("NASDAQ & New York Stock Exchange (2:30 PM - 9 PM)")
if now < nasdaq_nyse_open:
    time_to_open = nasdaq_nyse_open - now
    msg = "Closed, opens in {}".format(clean_timedelta(time_to_open))
    print(colored(msg, 'red'))
elif now >= nasdaq_nyse_open and now <= nasdaq_nyse_close:
    time_to_close = nasdaq_nyse_close - now
    msg = "Open, closes in {}".format(clean_timedelta(time_to_close))
    print(colored(msg, 'green'))
else:
    next_nasdaq_nyse_open, _ = nasdaq_and_nyse(now + timedelta(days=1))
    time_to_open = next_nasdaq_nyse_open - now
    msg = "Closed, opens in {}".format(clean_timedelta(time_to_open))
    print(colored(msg, 'red'))

