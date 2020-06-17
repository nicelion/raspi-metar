# raspi-metar.py
#
# Created by Ian Thompson

from airport import Airport, AirportTester
import time, settings, requests
from support.exceptions import *
import xml.etree.cElementTree as ET
from itertools import zip_longest


airports = []

def update_information():
    print('UPDATING METAR INFORMATION')

    airports.clear()

    # NOAA Weather Data URL
    url2 = 'https://www.aviationweather.gov/adds/dataserver_current/httpparam?dataSource=metars&requestType=retrieve&format=xml&hoursBeforeNow=2&mostRecentForEachStation=true&stationString=%s'

    identifiers = []
    for airport in settings.airports:
        ident = settings.airports[airport]
        
        identifiers.append(ident)
        airports.append(AirportTester(ident, airport))

    query_stirng = ','.join(identifiers)
    url2 = url2 % query_stirng
    
    dom = ET.fromstring(requests.get(url2).text)

    metars = dom.findall('./data/METAR')

    for m in metars:
        metar = m.find("raw_text").text
        station_id = m.find("station_id").text

        for airport in airports:
            if airport.get_station_info().icao == station_id:
                airport.set_metar(metar)

    # for airport in airports:
    #     print(airport.get_metar().data.raw)
    # for led in settings.airports:
    #     try:
    #         ident = settings.airports[led]
    #         airports.append(Airport(ident, led))
    #         print(led, ident)
    #     except NoMETARInformationError as err:
    #         print(err)
    
def set_leds():
    print('SETTING LEDS')
    # animated_airports.clear()

    for airport in airports:
        led_color = airport.get_led_color()
        station = airport.get_station_info()
        flight_rules = airport.get_flight_rules()

        print('Setting %s to %s for %s conditions' % (station.name, str(led_color), flight_rules))
        




def show_animations():
    print('STARTING ANIMATIONS')

    # i = 0
    # for a in animated_airports:
    #     l = len(a.get_animation_color())
    #     animation = a.get_animation_color()
        
    #     print(a.get_station_info().name, animation[i])
    # animate = True
    # ap_index = 0
    # wx_index = 0
    # limit = settings.refresh_rate / 2
    # count = 0
    # while count < limit:
    #     if ap_index == len(airports): 
    #         ap_index = 0
    #         wx_index += 1

    #     airport = airports[ap_index]

    #     print(airport.get_station_info().name)

    #     if wx_index < len(airport.get_animation_color()):
    #         print(airport.get_animation_color()[wx_index])


    #     # print(len(airport.get_animation_color()))
    #     ap_index += 1

    #     count += 2
    ap_index = 0
    ap_station_indexes = []

    for a in airports:
        ap_station_indexes.append(0)

    animation_duration = settings.animation_duration / 2
    limit = settings.refresh_rate / (animation_duration * 2)

    count = 0
    while count < limit:

        for index, airport in enumerate(airports):
            weather_codes = airport.get_animation_color()

            if len(weather_codes) - 1 >= 0:
                print(weather_codes[ap_station_indexes[index]], airport.get_station_info().name)

                # print(ap_station_indexes[index])

                if len(weather_codes) - 1 > ap_station_indexes[index]:
                    ap_station_indexes[index] += 1
                else:
                    ap_station_indexes[index] = 0

        time.sleep(animation_duration)

        set_leds()
        
        time.sleep(animation_duration)

        count += 1
        # for airport in airports:
        #     if wx_index < len(airport.get_animation_color()):
        #         print(airport.get_animation_color()[wx_index], airport.get_station_info().name)
        #     else:
        #         continue 
            # i += 1

        # for airport in airports:
        #     print(airport.get_led_color())
        
        # time.sleep(1)

        # ap_index += 1
        # wx_index += 1
        
        # if l == 0: continue

        # if i > l:
        #     print(a.get_station_info().name, animation[i])
        
        # i += 1



        # for m in a.get_animation_color():
        #     print(a.get_station_info().name, m)

    # limit = settings.refresh_rate / 2
    # count = 0
    # while count < limit:
    #     if settings.show_lightning:
    #         for airport in airports:
    #             if airport.is_lightning():
    #                 name = airport.get_station_info().name
    #                 print('setting %s to WHITE' % name)

    #     time.sleep(1)
        


    #     for airport in airports:
    #         if airport.is_lightning():
    #             name = airport.get_station_info().name
    #             print('setting %s to %s' % (name, airport.get_led_color()))
    #     time.sleep(1)

    #     count += 1

if __name__ == "__main__":

    try:
        while True:

            update_information()
            set_leds()
            show_animations()

            print("\nRESTARTING\n")
    except KeyboardInterrupt:
        print("cleaning up")
