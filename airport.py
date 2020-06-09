from avwx import Metar, Station
import settings

class Airport:
    def __init__(self, ident, index):
        self.idnet = ident
        self.index = index

        self.station = Station.from_icao(ident)

        self.metar = self.__get_metar()
    def __get_metar(self):
        m = Metar(self.idnet)
        m.update()
        return m
    
    def get_led_color(self):
        flight_rules = self.metar.data.flight_rules

        if flight_rules == 'VFR':
            return settings.vfr_color
        elif flight_rules == 'MVFR':
            return settings.mvfr_color
        elif flight_rules == 'IFR':
            return settings.ifr_color
        elif flight_rules == 'LIFR':
            return settings.lifr_color


    def update_airport(self):
        self.set_led("RED")
    
    def get_flight_rules(self):
        return self.metar.data.flight_rules.lower()

    def is_lightning(self):

        if 'ltg' in self.metar.data.remarks.lower():
            return True
        for code in self.metar.data.wx_codes:
            if 'ts' in code.repr.lower() or 'ltg' in self.metar.data.remarks.lower():
                return True
        

        return False

    def get_station_info(self):
        return self.station

