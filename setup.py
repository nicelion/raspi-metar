from os import path, system
from avwx import Metar, exceptions, Station
from configparser import ConfigParser

print("raspi-metar Setup Wizard")
run = True

led_index = 1
config = {}

def save_airports(configuration):
    # save to config file

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

while run:
    try:
        ident = input("ICAO identifier for LED #%s: " % led_index)

        try: 
            m = Metar(ident.upper())    # attempts to see if avwx recognizes ICAO code
            config.update({led_index: ident.upper()})   # update dictionary with led index and uppercase identifier
            print('Assigning %s to LED #%s' % (m.station.name, led_index))
            led_index += 1  # increment led_index
        except:
            print('[ERROR] %s is not a valid ICAO identifier! Be sure to include county code!' % ident)



    except KeyboardInterrupt:
        print("Keyboard")
        save_airports(config)
        run = False