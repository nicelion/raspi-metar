import avwx
from avwx import Metar
# import setup
from airport import Airport
import time
from configparser import ConfigParser
# try:
#     kgsp = Metar("KSPn")
# except avwx.exceptions.BadStation:
#     print("there was an error")
# setup.start_wizard()

# kGSP = Metar("KGSP")
# kGSP.update()
# print(kGSP.data.raw)
# print(kGSP.data.wx_codes)
# print(kGSP.data.flight_rules)

# if kGSP.data.wx_codes[0].repr == '+TSRA':
#     print('Lightning!!')

# kGSP = Airport('KGSP', 12)
# kCEU = Airport('KCEU', 13)
# kAND = Airport('KAND', 14)
# kGMU = Airport('KGMU', 16)
# kCHS = Airport('KCHS', 19)

# airports = [kGSP, kCEU, kAND, kGMU, kCHS]

# def update():
#     print("Updating Airport Infromation")
#     for a in airports:
#         a.update_airport()


# while True:
#     update()
#     time.sleep(10)
        

# setup.start_wizard()
# airports = []
# with open('airports', 'r') as ap_file:
#     for line in ap_file:
#         airports.extend([str(a) for a in line.split()])


# ports = []
# x = 1
# for ap in airports:
#     ports.append(Airport(ap, x))
#     x += 1

# for p in ports:
#     p.update_airport()

config =  ConfigParser()
config.read('raspi-metar.conf')
config['colors'] = {
    "IFR": (255,212,122),
    "LIFR": (122,122,122),
    "VFR": (0, 255, 0)
}

with open('raspi-metar.conf', 'w') as configfile:
   config.write(configfile)