import avwx
from avwx import Metar
import setup
from airport import Airport
import time
from configparser import ConfigParser

config =  ConfigParser()
config.read('raspi-metar.conf')
config.sections()

### CONFIGURATION
refresh_rate = config.getint('settings', 'refresh_rate')
show_lightning = config.getboolean('settings', 'show_lightning')
brightness = config.getint('settings', 'brightness')

vfr_color = config['colors']['vfr']
ifr_color = config['colors']['ifr']
mvfr_color = config['colors']['mvfr']
lifr_color = config['colors']['lifr']

### END CONFIGURATION

airports = []
for led in config['airports']:
    ident = config['airports'][led]

    airports.append(Airport(ident, led))

while True:
    for airport in airports:

        led_color = (0, 0, 0)
        station = airport.get_station_info()
        flight_rules = airport.get_flight_rules()
        lightning_status = airport.is_lightning()

        if flight_rules == 'vfr':
            led_color = vfr_color
        elif flight_rules == 'mvfr':
            led_color = mvfr_color
        elif flight_rules == 'ifr':
            led_color = ifr_color
        elif flight_rules == 'lifr':
            led_color = lifr_color
        
        if lightning_status:
            pass

        print('Setting %s to %s' % (airport.station.name, str(led_color)))

    
    time.sleep(refresh_rate)

