from os import path, system
from avwx import Metar, exceptions, Station
from ColorIt import *
from configparser import ConfigParser

done_keywords = ["done", "finished", "exit", "quit", "save"]

def start_wizard():
    # start the setup wizard
    system('clear')
    print('Welcome to Setup Wizard')

    check_to_create_airports()

def check_to_create_airports():
    # check if airports file exists

    if path.exists('raspi-metar.conf'):
        # conf file does exist
        get_command()
    else:
        # file does not exist, so we will create one now.
        print('[WARN] airports file was not found \nCreating one now!')
        system('touch airports.conf')
        
        print('[SUCCESS] Successfully created airports.conf file.')
        get_command()

def get_command():
    # get the input from user and decide what to do with it. If command does not exist, function gets called again
    
    comm = input("Enter a command to get started: ")

    if comm == 'help':
        system('cat helpfile')
        get_command()
    elif comm == "add all":
        print('add all')
        add_all()
    elif comm == 'add at':
        print('add at')
    elif comm in done_keywords:
        print('Goodbye.')
    else: 
        print('[ERROR]: Invalid command. Please try again. Pass help for all commands')
        get_command()

def verify_airport_is_valid() -> (str, str):
    # verifies ICAO ident provided is a valid ident. If not, user will be asked to provide a valid one before going on.

    while True:
    
        a = input("    Enter ICAO ident (Kxxx): ")
        if a in done_keywords:
            return ('done', 'done')
            break
        try:
            stat = Station.from_icao(a)
            return (a.upper(), stat.name)
            break
        except exceptions.BadStation:
            print("[ERR] %s is not a valid identifier!" % a)

def add_all():
    print('Assign ICAO idents to LED position. For example, when asked you would pas \'KJFK\' and \'10\' if you wanted to assign John F. Kennedy International Airport to use LED 10.\nWhen finished, pass done')
    
    config = {}
    while True:

        airport = verify_airport_is_valid()

        if airport[0] == 'done':
            save_file(config)
            break
        else:
            led = input("    LED position: ")

            config.update({led: airport[0]}) 

            print('[SUCCESS]: Assigned %s to LED at positon %s' % (airport[1], led))
            

def save_file(configuration):
    config =  ConfigParser()
    config['leds'] = configuration
    
    with open('airports.conf', 'w') as configfile:
        config.write(configfile)
    
    print("[SUCCESS]: Saved airports to file.")

    get_command()


start_wizard()
