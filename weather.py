import requests

from bs4 import BeautifulSoup
from enum import Enum


class Flag(Enum):
    HOURLY = 'hourly'
    CURRENTLY = 'currently'
    DAY_DETAILS = 'day_details'


def get_forecast(_lat, _long, _flag, _day=''):
    if _day:
        site = requests.get(f'https://darksky.net/details/{_lat},{_long}/{_day}/ca12/en')
    else:
        site = requests.get(f'https://darksky.net/forecast/{_lat},{_long}/ca12/en')

    soup = BeautifulSoup(site.content, features='html.parser')

    script = soup.findAll('script')[2].next.strip()

    if _flag is Flag.HOURLY:
        script = script.split('hours =')[1].split(']')[0] + ']'
    elif _flag is Flag.CURRENTLY:
        script = script.split('currently =')[1].split('}', 1)[0] + '}'
    elif _flag is Flag.DAY_DETAILS:
        script = soup.findAll('script')[1].next.split('=', 1)[-1].split(']')[0] + ']'
    forecast = eval(script)

    return forecast
