import os
import abc
import getpass
from dotenv import load_dotenv
from geopy.geocoders import Nominatim


class NormalUser(abc.ABC):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'initialize_user') and
                callable(subclass.initialize_user) and
                hasattr(subclass, 'get_location') and
                callable(subclass.get_location))


class LocalUser:
    @staticmethod
    def initialize_user():
        if os.path.exists(f'.{getpass.getuser()}_env'):
            load_dotenv(f'.{getpass.getuser()}_env')
        else:
            with open(f'.{getpass.getuser()}_env', mode='w+', newline='') as f:
                print(f'Hello {getpass.getuser()}! I understand this is your first time\n'
                      f'Let\'s setup your environment.\n')
                location = input('Please enter your location (e.g. Thessaloniki, Greece):')
                f.write(f'LOCATION={location}')
                os.environ['LOCATION'] = location

    @staticmethod
    def get_location():
        address = os.getenv('LOCATION')
        geo_locator = Nominatim(user_agent=getpass.getuser())
        return geo_locator.geocode(address)
