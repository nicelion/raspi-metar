import os
from os import path
from avwx import Metar, exceptions, Station
from ColorIt import *
from configparser import ConfigParser

done_keywords = ["done", "finished", "exit", "quit", "save"]

def start_wizard():
    os.system("clear")
    print('Welcome to Setup Wizard')

    check_to_create_airports()

def check_to_create_airports():
    # check if airports file exists

    if path.exists('airports'):
        get_command()
    else:
        print('[WARN] airports file was not found \nCreating one now!')
        count = input("How many data points are you displaying: ")

        ap = open('airports', 'x')

        for x in range(1, int(count)):
            ap.write('NULL\n')
        ap.write('NULL')
        
        print('[SUCCESS] Successfully created airports file.')

        ap.close()
        get_command()

def get_command():
    comm = input("Enter a command to get started: ")

    if comm == 'help':
        os.system('cat helpfile')
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
            # verify_airport_is_valid()

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
    
    with open('test.conf', 'w') as configfile:
        config.write(configfile)
    
    print("[SUCCESS]: Saved airports to file.")

    get_command()


start_wizard()
