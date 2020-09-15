# setup.py
# raspi-metar

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
    config.set('settings', 'number_of_leds', str(led_index - 1))
    verify = input("Are you sure you want to save? (y/n) ")

    if verify == 'yes' or verify.lower() == 'y':
        with open('raspi-metar.conf', 'w') as configfile:
            config.write(configfile)
        
        print("[SUCCESS]: Saved airports to file.")
    else:
        print("Ok. Not saving recent configuration")

def suggest_airports(wrong_ident):
    print("Could not identift airport! Select an option below")
    

    for letter in wrong_ident[1:]:
        print(letter)

while run:
    try:
        ident = input("ICAO identifier for LED #%s: " % led_index)

        if ident == "":
            print("Skipping LED #%s" % led_index)
            led_index += 1
        else: 
            try: 
                m = Metar(ident.upper())    # attempts to see if avwx recognizes ICAO code
                config.update({led_index: ident.upper()})   # update dictionary with led index and uppercase identifier
                print('Assigning %s in %s, %s to LED #%s' % (m.station.name, m.station.city, m.station.state, led_index,))
                led_index += 1  # increment led_index
            except:
                if len(ident) < 4:
                    print('[ERROR] %s is not a valid ICAO identifier! Be sure to include county code!' % ident)
                    continue
                
                suggest_airports(ident)



    except KeyboardInterrupt:
        print("Keyboard")
        save_airports(config)
        run = False