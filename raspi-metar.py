import avwx
from avwx import Metar
import setup
from airport import Airport
import time
from configparser import ConfigParser
import settings

config =  ConfigParser()
config.read('raspi-metar.conf')
config.sections()

# ### CONFIGURATION
# refresh_rate = config.getint('settings', 'refresh_rate')
# show_lightning = config.getboolean('settings', 'show_lightning')
# brightness = config.getint('settings', 'brightness')
# i2c_display_enabled = config.getboolean('settings', 'i2c_display_enabled')

# vfr_color = config['colors']['vfr']
# ifr_color = config['colors']['ifr']
# mvfr_color = config['colors']['mvfr']
# lifr_color = config['colors']['lifr']



### END CONFIGURATION

airports = []
lightning = []

def update_information():
    airports.clear()
    for led in config['airports']:
        ident = config['airports'][led]
        airports.append(Airport(ident, led))
        print(led, ident)

def set_leds():
    for airport in airports:
        led_color = airport.get_led_color()
        station = airport.get_station_info()
        flight_rules = airport.get_flight_rules()
        lightning_status = airport.is_lightning()

        
        if lightning_status:
            lightning.append(airport)

        print('Setting %s to %s for %s conditions' % (airport.station.name, str(led_color), flight_rules))
        time.sleep(1)




def show_animations():
    limit = settings.refresh_rate / 2
    count = 0
    while count < limit:
        for airport in lightning:
            name = airport.get_station_info().name
            print('setting %s to WHITE' % name)

        time.sleep(1)
        for airport in lightning:
            name = airport.get_station_info().name
            print('setting %s to %s' % (name, airport.get_led_color()))
        time.sleep(1)

        count += 1

while True:
    update_information()

    set_leds()

    show_animations()

# airports = config['airports']

# print(airports.items())

# while True:
#     for key, value in airports.items():
#         print(key, value)
        
#         m = Metar(value)
#         m.update()

#         led_color = (0, 0, 0)
#         station = m.station.name
#         flight_rules = m.data.flight_rules

#         if flight_rules == 'VFR':
#             led_color = vfr_color
#         elif flight_rules == 'MVFR':
#             led_color = mvfr_color
#         elif flight_rules == 'IFR':
#             led_color = ifr_color
#         elif flight_rules == 'LIFR':
#             led_color = lifr_color
        
#         print('Setting %s for %s to %s for %s conditons' % (key, station, str(led_color), flight_rules))
#     break
# for led in config['airports']:
#     ident = config['airports'][led]

#     airports.append(Airport(ident, led))

# while True:
#     for airport in airports:

#         led_color = (0, 0, 0)
#         station = airport.get_station_info()
#         flight_rules = airport.get_flight_rules()
#         lightning_status = airport.is_lightning()

#         if flight_rules == 'vfr':
#             led_color = vfr_color
#         elif flight_rules == 'mvfr':
#             led_color = mvfr_color
#         elif flight_rules == 'ifr':
#             led_color = ifr_color
#         elif flight_rules == 'lifr':
#             led_color = lifr_color
        
#         if lightning_status:
#             pass

#         print('Setting %s to %s' % (airport.station.name, str(led_color)))

    
#     time.sleep(refresh_rate)

