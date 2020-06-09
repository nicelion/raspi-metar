import avwx
from avwx import Metar
import setup
from airport import Airport
import time
import settings

airports = []
lightning = []

def update_information():
    print('UPDATING METAR INFORMATION')
    airports.clear()
    for led in settings.airports:
        ident = settings.airports[led]
        airports.append(Airport(ident, led))
        print(led, ident)

def set_leds():
    print('SETTING LEDS')
    for airport in airports:
        led_color = airport.get_led_color()
        station = airport.get_station_info()
        flight_rules = airport.get_flight_rules()
        lightning_status = airport.is_lightning()

        
        if lightning_status:
            lightning.append(airport)

        print('Setting %s to %s for %s conditions' % (airport.station.name, str(led_color), flight_rules))




def show_animations():
    print('STARTING ANIMATIONS')
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

try:
    while True:
        update_information()

        set_leds()

        show_animations()
except KeyboardInterrupt:
    print("cleaning up")
