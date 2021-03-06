from avwx import Metar, Station
import settings
from support.exceptions import *

class Airport:
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
    def get_animation_color(self):
        wx = []
        snow_codes = ["IC ", "PL ", "SG ", "SN ", "DS "]
        fog_codes = ["FG ", "FU ", "DS ", "DU ", "PO ", "SS ", "VA "]

        if self.is_lightning(): wx.append((255,255,255))

        for f in fog_codes:
            for c in self.metar.data.wx_codes:
                if c.repr in fog_codes:
                    wx.append((119,0,255))
                    break
            if f in self.metar.data.remarks: 
                wx.append((119,0,255))
                break
        for s in snow_codes:
            for c in self.metar.data.wx_codes:
                if c.repr in snow_codes:
                    wx.append((215,215,215))
                    break
            if s in self.metar.data.remarks:
                wx.append((215,215,215))
                break
        
        return wx

if __name__ == "__main__":
    
    spa = Airport('KSPA', 1)
    spa.set_metar('KSPA 170115Z AUTO 03007KT 10SM SCT012 BKN034 BKN042 15/12 A3017 RMK AO2')
    print(spa.get_animation_color())