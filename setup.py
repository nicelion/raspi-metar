# setup.py
# raspi-metar

from os import path, system
from avwx import Metar, exceptions, Station
from configparser import ConfigParser
import json
import settings

system('clear')
print("\033[95mWelcome to the raspi-metar Setup Wizard!\033[0m\n")
run = True

global led_index
led_index = 1
config = {}

success = "\033[1m\033[92m[SUCCESS]:\033[0m "
warn = "\033[1m\033[93m[WARN]:\033[0m "
error = "\033[1m\033[91m[ERROR]:\033[0m "


with open('support/letter-suggestions.json') as f:
  data = json.load(f)


def save_airports(configuration):
    # save to config file

    config =  ConfigParser()
    config.read('raspi-metar.conf')
    config['airports'] = configuration
    config.set('settings', 'number_of_leds', str(led_index - 1))
    verify = input("\n" + warn + "Are you sure you want to save? (y/n) ")

    if verify == 'yes' or verify.lower() == 'y':
        with open('raspi-metar.conf', 'w') as configfile:
            config.write(configfile)
        
        print(success + "Saved airports to file.")
    else:
        print("Ok. Not saving recent configuration")
        print("Goodbye.")


def get_suggestion_index(length):
    
    try:
        u = input("Enter selection. Pass 'skip' or 'again' to skip or try again, repectivly: ")
        
        if u == "skip":
            return "skip"
        elif u == "again":
            return "again"
        else:
            if int(u) <= length and int(u) >= 0:
                return int(u)
            else:
                print(error + "Value is in valid. Please select a number 0-%i" % (length - 1))
                get_suggestion_index(length)


    except ValueError:
        print(error + "Input is not a valid number")
        get_suggestion_index(length)

def suggest_airports(led_ind, wrong_ident):
    global led_index
    print(error + "%s is not a valid ICAO identifier!" % wrong_ident)

    possible_airports = []

    letter_1_suggestions = data[wrong_ident[1].lower()]
    letter_2_suggestions = data[wrong_ident[2].lower()]
    letter_3_suggestions = data[wrong_ident[3].lower()]


    # find suggestions
    for l1 in letter_1_suggestions:
        for l2 in letter_2_suggestions:
            for l3 in letter_3_suggestions:
                suggestion = "k" + l1 + l2 + l3
                
                try:
                    m = Metar(suggestion.upper())

                    possible_airports.append(m)
                except:
                    pass
    
    print("Are of of these your airports?")

    index = 0 
    for airport in possible_airports:
        print("\033[1m%i.\033[0m %s | %s in %s, %s" % (index, airport.icao, airport.station.name, airport.station.city, airport.station.state))
        index += 1

    suggestion = get_suggestion_index(len(possible_airports))

    if suggestion == "again":
        pass
    elif suggestion == "skip":
        if input(warn + "Are you sure you want to skip? ") == "y":
            print("Skiping LED #%s" % led_ind)
            led_index += 1  # increment led_index
        else:
            suggest_airports(led_ind, wrong_ident)
    elif suggestion != "skip":
        selected_ap = possible_airports[suggestion]

        confirm = input(warn + "Are you sure you want to assign LED %i to %s in %s, %s? (y/n): " % (led_ind, selected_ap.station.name, selected_ap.station.city, selected_ap.station.state))

        if confirm.lower() == "y":
            config.update({led_ind: selected_ap.icao.upper()})
            print(success + 'Assigning %s in %s, %s to LED #%s' % (selected_ap.station.name, selected_ap.station.city, selected_ap.station.state, led_ind))
            led_index += 1
        else:
            suggest_airports(led_ind, wrong_ident)




    



while run:
    try:
        ident = input("\nICAO identifier for LED #%s: " % led_index)
        code = settings.default_country_code + ident

        if ident == "":
            print("Skipping LED #%s" % led_index)
            led_index += 1
        else: 
            try: 
                m = Metar(code.upper())    # attempts to see if avwx recognizes ICAO code
                config.update({led_index: code.upper()})   # update dictionary with led index and uppercase identifier
                print(success + 'Assigning %s in %s, %s to LED #%s' % (m.station.name, m.station.city, m.station.state, led_index))
                led_index += 1  # increment led_index
            except:
                if len(code) < 4:
                    # user did not provide a country code
                    print(error + '%s is not a valid ICAO identifier! Identifiers must be 3 to 4 characters in length' % code)
                    continue
                
                suggest_airports(led_index, code)
        




    except KeyboardInterrupt:
        save_airports(config)
        run = False