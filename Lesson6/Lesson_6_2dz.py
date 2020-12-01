import pyowm
import requests
from pyowm.utils import timestamps, formatting
from abc import ABC
import datetime

class wether(ABC):
    r = requests.get('https://api.ipdata.co?api-key=test').json()
    own_country = r['country_code']
    own_city = r['city']

    def __init__(self, city = None, code = None, date = None):
        self.city = city or self.own_city
        self.code = code or self.own_country
        self.date = date or '2020-11-30'

    def get_weather(self):
        owm = pyowm.OWM('d5c9bfe76822443c1b6986a3012c8f42')
        reg = owm.city_id_registry()
        list_of_locations = reg.locations_for(self.city, country=self.code)
        loc_list = list_of_locations[0]
        lat = loc_list.lat
        long = loc_list.lon
        mgr = owm.weather_manager()
        ts = formatting.to_UNIXtime(self.date)
        b = mgr.forecast_at_coords(lat=lat, lon=long, interval='3h')
        a = b.get_weather_at(ts)
        return a
# print(one_call.forecast_daily[0].temperature('celsius'))

# mgr = owm.weather_manager(list_of_locations['lat'],list_of_locations['lon'])

# a = wether('odessa','UA').get_weather()
# a = wether().get_weather()
# print(a)