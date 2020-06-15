# raspi-metar.py
#
# Created by Ian Thompson

import avwx
from avwx import Metar
import setup
from airport import Airport
import time
import settings
from exceptions import *


airports = []

def update_information():
    print('UPDATING METAR INFORMATION')

    airports.clear()

    for led in settings.airports:
        try:
            ident = settings.airports[led]
            airports.append(Airport(ident, led))
            print(led, ident)
        except NoMETARInformationError as err:
            print(err)
    

def set_leds():
    print('SETTING LEDS')


    for airport in airports:
        led_color = airport.get_led_color()
        station = airport.get_station_info()
        flight_rules = airport.get_flight_rules()

        print('Setting %s to %s for %s conditions' % (station.name, str(led_color), flight_rules))
        




def show_animations():
    print('STARTING ANIMATIONS')

    limit = settings.refresh_rate / 2
    count = 0
    while count < limit:
        if settings.show_lightning:
            for airport in airports:
                if airport.is_lightning():
                    name = airport.get_station_info().name
                    print('setting %s to WHITE' % name)

        time.sleep(1)
        
        for airport in airports:
            if airport.is_lightning():
                name = airport.get_station_info().name
                print('setting %s to %s' % (name, airport.get_led_color()))
        time.sleep(1)

        count += 1

if __name__ == "__main__":

    try:
        while True:

            update_information()
            set_leds()
            show_animations()
            
    except KeyboardInterrupt:
        print("cleaning up")
