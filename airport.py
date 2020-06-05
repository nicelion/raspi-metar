from avwx import Metar, Station
from LED import *
class Airport:
    def __init__(self, ident, index):
        self.idnet = ident
        self.index = index

        self.station = Station.from_icao(ident)

        self.led = LED(self.index, self.__get_metar(), self.station)

    def __get_metar(self):
        m = Metar(self.idnet)
        m.update()
        return m
    
    def set_led(self, color):
        print("Setting LED %s to %s for %s" % (self.index, color, self.station.name))

    def update_airport(self):
        self.led.update()


