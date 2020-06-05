import os.path
from os import path
from avwx import Metar, exceptions, Station
from ColorIt import *

def start_wizard():
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
        print('help')
    elif comm == "add all":
        print('add all')
        add_all()
    elif comm == 'add at':
        print('add at')
    elif comm == 'exit' or comm == 'end':
        print('Goodbye.')
    else: 
        print('[ERROR]: Invalid command. Please try again. Pass help for all commands')
        get_command()

def verify_airport_is_valid() -> str:
    a = input("Enter ICAO ident (Kxxx): ")

    try:
        stat = Station.from_icao(a)
        print('Added %s' % stat.name)
        return a.upper()
    except exceptions.BadStation:
        print("[ERR] %s is not a valid identifier!" % a)
        verify_airport_is_valid()

def add_all():
    airports_file = open('airports', 'r')
    airports = airports_file.readlines()

    mod = []
    for airport in airports:
        print('called')
        ap = verify_airport_is_valid()
        mod.append(ap)

    save = input('Are you ready to save to file?(y/n): ')

    if save == 'y' or save == 'yes':
        print('save')
        save_file(mod)
    else: 
        print('Canceling')

def save_file(airports):
    with open('airports', "w") as fhandle:
        for airport in airports:
            fhandle.write(f'{airport}\n')
    
    print("[SUCCESS]: Saved airports to file.")

    get_command()


start_wizard()