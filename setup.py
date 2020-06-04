import os.path
from os import path

def start_wizard():
    print('Welcome to Setup Wizard')

    check_to_create_airports()

def check_to_create_airports():
    # check if airports file exists

    if path.exists('airports'):
        print('true')
    else:
        print('[WARN] airports file was not found \nCreating one now!')
        count = input("How many data points are you displaying: ")

        ap = open('airports', 'x')

        for x in range(1, int(count)):
            ap.write('NULL\n')
        
        print('[SUCCESS] Successfully created airports file.')
