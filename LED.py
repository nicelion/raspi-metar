from avwx import Metar, Station

class LED:

    def __init__(self, index, current_metar: Metar, station: Station):
        self.index = index
        self.current_metar = current_metar
        self.station = station
    
    def __set_led(self):
        
        if self.current_metar.data.flight_rules == 'VFR':
            self.__set_color('GREEN')
        elif self.current_metar.data.flight_rules == 'IFR':
            self.__set_color('RED')
        elif self.current_metar.data.flight_rules == 'MVFR':
            self.__set_color('BLUE')
        elif self.current_metar.data.flight_rules == 'LIFR':
            self.__set_color('MAGENTA')

    def __set_color(self, color):
        print("Setting LED %s to %s for %s" % (self.index, color, self.station.name))

    def update(self):
        self.__set_led()
