from termcolor import colored
import time
from datetime import datetime, timedelta

def today_london_session(date):
    open = date.replace(hour=8, minute=0, second=0, microsecond=0)
    close = date.replace(hour=16, minute=0, second=0, microsecond=0)
    return (open, close)

def today_new_york_session(date):
    open = date.replace(hour=13, minute=0, second=0, microsecond=0)
    close = date.replace(hour=22, minute=0, second=0, microsecond=0)
    return (open, close)

def clean_timedelta(delta):
    return str(delta).split(".")[0]

now = datetime.now()
london = today_london_session(now)
new_york = today_new_york_session(now)

# hour_ago = now - timedelta(hours=1)
# yesterday = now - timedelta(days=1)

# Time changer for testing
now = now.replace(hour=23, minute=0, second=0, microsecond=0)

print("The time is:", now.strftime("%H:%M:%S %p"), "\n")

if now >= london[0] and now <= london[1]:
    time_to_close = london[1] - now
    print("London open, closes in {}".format(clean_timedelta(time_to_close)))
else:
    # TODO: differentiate before close and after close
    time_to_open = london[0] - now
    print("London closed, opens in {}".format(clean_timedelta(time_to_open)))

if now >= new_york[0] and now <= new_york[1]:
    time_to_close = new_york[1] - now
    print("New York open, closes in {}".format(clean_timedelta(time_to_close)))
else:
    # TODO: differentiate before close and after close
    time_to_open = new_york[0] - now
    print("New York closed, opens in {}".format(clean_timedelta(time_to_open)))




