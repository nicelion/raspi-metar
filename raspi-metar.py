# raspi-metar.py
#
# Created by Ian Thompson

from airport import Airport
import time, settings, requests
import xml.etree.cElementTree as ET
from itertools import zip_longest
import board
import neopixel
import re

pixels = neopixel.NeoPixel(board.D18, settings.number_of_leds, brightness=.05, auto_write=False)

airports = []

green = (255, 0, 0)
red = (0, 255, 0)
blue = (0, 0, 255)
off = (0, 0, 0)

def animation():

    pixels.fill(red)
    pixels.show()

    time.sleep(0.1)

    pixels.fill(blue)
    pixels.show()
    
    time.sleep(0.1)

    pixels.fill(green)
    pixels.show()
    
    time.sleep(0.1)

    pixels.fill(off)
    pixels.show()


def update_information():
    print('UPDATING METAR INFORMATION')

    airports.clear()

    # NOAA Weather Data URL
    url2 = 'https://www.aviationweather.gov/adds/dataserver_current/httpparam?dataSource=metars&requestType=retrieve&format=xml&hoursBeforeNow=5&mostRecentForEachStation=true&stationString=%s'

    identifiers = []
    for airport in settings.airports:
        ident = settings.airports[airport]
        
        identifiers.append(ident)
        airports.append(Airport(ident, airport))

    query_stirng = ','.join(identifiers)
    url2 = url2 % query_stirng
    
    dom = ET.fromstring(requests.get(url2).text)

    metars = dom.findall('./data/METAR')

    for m in metars:
        raw_metar = m.find('raw_text').text
        station_identifier = m.find("station_id").text

        for airport in airports:
            if airport.get_station_info().icao == station_identifier:
                airport.set_metar(raw_metar)

    # for m in metars:
    #     metar = m.find("raw_text").text
    #     station_id = m.find("station_id").text

    #     for airport in airports:
    #         if airport.get_station_info().icao == station_id:
    #             airport.set_metar(metar)


    
def set_leds():
    print('SETTING LEDS')

    for index, airport in enumerate(airports):
        try:
            led_color = airport.get_led_color()
            station = airport.get_station_info()
            flight_rules = airport.get_flight_rules()

            pixels[index] = tuple(int(v) for v in re.findall("[0-9]+", led_color))
            print('Setting %s to %s for %s conditions' % (station.name, str(led_color), flight_rules))
        except:
            print("No METAR found for %s! (%s)" % (airport.get_station_info().name, airport.get_station_info().icao))
            pixels[index] = (0, 0, 0)

    pixels.show() 




def show_animations():
    print('STARTING ANIMATIONS')

    ap_station_indexes = []

    for _ in airports:
        ap_station_indexes.append(0)

    animation_duration = settings.animation_duration / 2
    limit = settings.refresh_rate / (animation_duration * 2)

    count = 0
    while count < limit:

        animated_airports = []
        for index, airport in enumerate(airports):
            try:
                weather_codes = airport.get_animation_color()
                if len(weather_codes) > 0:
                    animated_airports.append(airport)
                    if len(weather_codes) - 1 >= 0:
                        print(weather_codes[ap_station_indexes[index]], airport.get_station_info().name)

                        pixels[index] = weather_codes[ap_station_indexes[index]]
                        if len(weather_codes) - 1 > ap_station_indexes[index]:
                            ap_station_indexes[index] += 1
                        else:
                            ap_station_indexes[index] = 0
            except:
                print("No METAR found for %s! (%s)" % (airport.get_station_info().name, airport.get_station_info().icao))
                pixels[index] = (0, 0, 0)

        pixels.show()
        time.sleep(animation_duration)

        set_leds()
        time.sleep(animation_duration * 3)

        count += 1

if __name__ == "__main__":

    animation()


    try:
        while True:

            update_information()
            set_leds()
            show_animations()

            print("\nRESTARTING\n")
    finally:
        print("cleaning up")

        pixels.fill((0,0,0))
        pixels.show()
