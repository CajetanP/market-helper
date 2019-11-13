from termcolor import colored
import time
from datetime import datetime, timedelta

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

def clean_timedelta(delta):
    return str(delta).split(".")[0]

now = datetime.now()
london = london_session(now)
new_york = new_york_session(now)
tokyo = tokyo_session(now)

# hour_ago = now - timedelta(hours=1)
# yesterday = now - timedelta(days=1)

# Time changer for testing
# now = now.replace(hour=23, minute=0, second=0, microsecond=0)

print("The time is:", colored(now.strftime("%H:%M:%S %p"), 'yellow'), "\n")

print(colored('Forex', 'blue'), "\n")

## Tokyo

if now >= tokyo[0] and now <= tokyo[1]: # Opened
    time_to_close = tokyo[1] - now
    print("Tokyo open, closes in {}".format(clean_timedelta(time_to_close)))
else: # After open
    next_tokyo = tokyo_session(now + timedelta(days=1))
    time_to_open = next_tokyo[0] - now
    print("Tokyo closed, opens in {}".format(clean_timedelta(time_to_open)))

## London

if now < london[0]: # Before open
    time_to_open = london[0] - now
    print("London closed, opens in {}".format(clean_timedelta(time_to_open)))
elif now >= london[0] and now <= london[1]: # Open
    time_to_close = london[1] - now
    print("London open, closes in {}".format(clean_timedelta(time_to_close)))
else: # After open
    next_london = london_session(now + timedelta(days=1))
    time_to_open = next_london[0] - now
    print("London closed, opens in {}".format(clean_timedelta(time_to_open)))

## New York

if now < new_york[0]:
    time_to_open = new_york[0] - now
    print("New York closed, opens in {}".format(clean_timedelta(time_to_open)))
elif now >= new_york[0] and now <= new_york[1]:
    time_to_close = new_york[1] - now
    print("New York open, closes in {}".format(clean_timedelta(time_to_close)))
else:
    next_new_york = new_york_session(now + timedelta(days=1))
    time_to_open = next_new_york[0] - now
    print("New York closed, opens in {}".format(clean_timedelta(time_to_open)))




