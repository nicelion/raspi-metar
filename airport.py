from avwx import Metar, Station
import settings
from support.exceptions import *

class Airport:
    def __init__(self, ident, index):
        self.idnet = ident
        self.index = index

        self.station = Station.from_icao(ident)

        self.metar = self.__get_metar()

        
    def __get_metar(self):

        try:
            m = Metar(self.idnet)
        except TimeoutError:
            self.__get_metar()
        else:
            if m.update():
                return m
            else:
                raise NoMETARInformationError('No METAR for %s found' % m.station.name)
    
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







class AirportTester:
    def __init__(self, ident, index):
        self.idnet = ident
        self.index = index

        self.station = Station.from_icao(ident)
        
    def set_metar(self, raw_metar):
        self.metar = Metar(self.idnet)
        self.metar.update(raw_metar)

    
    def get_metar(self):
        return self.metar

    def get_led_color(self):
        try:
            flight_rules = self.metar.data.flight_rules

        except AttributeError as err:
            print(err)
            return (0,0,0)
        else:
            if flight_rules == 'VFR':
                return settings.vfr_color
            elif flight_rules == 'MVFR':
                return settings.mvfr_color
            elif flight_rules == 'IFR':
                return settings.ifr_color
            elif flight_rules == 'LIFR':
                return settings.lifr_color


    # def update_airport(self):
    #     self.set_led("RED")
    
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

    def is_snowing(self):
        if 'rn' in self.metar.data.remarks.lower():
            return True
        for code in self.metar.data.wx_codes:
            if 'rn' in code.repr.lower() or 'rn' in self.metar.data.remarks.lower():
                return True
    def is_tornado():
        pass
        # if 'FC' in self.metar.data.raw
    def get_animation_color(self):
        wx = []
        snow_codes = ["IC", "PL", "SG", "SN", ]
        fog_codes = ["FG", "FU", "DS", "DU", "PO", "SS", "VA"]

        return (settings.snow_color, settings.fog_color)
        # for c in snow_codes:
        #     if 


        # if self.is_lightning(): wx.append("ltg")

        # return wx