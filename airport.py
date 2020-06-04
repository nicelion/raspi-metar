from avwx import Metar, Station
from LED import *
class Airport:
    def __init__(self, ident, index):
        self.idnet = ident
        self.index = index

        self.station = Station.from_icao(ident)

    def __get_metar(self):
        m = Metar(self.idnet)
        m.update()
        return m
    
    def set_led(self, color):
        print("Setting LED %s to %s for %s" % (self.index, color, self.station.name))

    def update_airport(self):
        current_metar = self.__get_metar().data

        if current_metar.flight_rules == 'VFR':
            self.set_led('GREEN')
        elif current_metar.flight_rules == 'IFR':
            self.set_led('RED')
        elif current_metar.flight_rules == 'MVFR':
            self.set_led('BLUE')
        elif current_metar.flight_rule == 'LIFR':
            self.set_led('MAGENTA')


