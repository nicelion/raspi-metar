from os import path, system
from avwx import Metar, exceptions, Station
from configparser import ConfigParser

print("raspi-metar Setup Wizard")
play = True

led_index = 1
config = {}

def save_airports(configuration):
    config =  ConfigParser()
    config.read('raspi-metar.conf')
    config['airports'] = configuration
    
    verify = input("Are you sure you want to save?(y/n) ")

    if verify == 'yes' or verify.lower() == 'y':
        with open('raspi-metar.conf', 'w') as configfile:
            config.write(configfile)
        
        print("[SUCCESS]: Saved airports to file.")
    else:
        print("Ok. Not saving recent configuration")

while play:

    try:
        ident = input("ICAO identifier for LED #%s: " % led_index)

        try: 
            m = Metar(ident.upper())
            config.update({led_index: ident})
            print('Assigning %s to LED #%s' % (m.station.name, led_index))
            led_index += 1
        except:
            print('[ERROR] %s is not a valid ICAO identifier! Be sure to include county code!' % ident)



    except KeyboardInterrupt:
        print("Keyboard")
        save_airports(config)
        play = False