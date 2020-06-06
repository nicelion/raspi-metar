from os import path, system
from avwx import Metar, exceptions, Station
from configparser import ConfigParser

done_keywords = ["done", "finished", "exit", "quit", "save"]

def start_wizard():
    # start the setup wizard
    system('clear')
    print('Welcome to Setup Wizard')

def get_command():
    # get the input from user and decide what to do with it. If command does not exist, function gets called again
    
    comm = input("Enter a command to get started: ")

    if comm == 'help':
        system('cat support/helpfile')
    elif comm == "add all":
        add_all()
    elif comm == 'add at':
        print('add at')
    elif comm in done_keywords:
        print('Goodbye.')
        return False
    else: 
        print('[ERROR]: Invalid command. Please try again. Pass help for all commands')
    
    return True
        

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
    print('Assign ICAO idents to LED position. For example, when asked you would pas \'KJFK\' and \'10\' if you wanted to assign John F. Kennedy International Airport to use LED 10.\nWhen finished, pass done\n')
    
    config = {}
    while True:

        airport = verify_airport_is_valid()

        if airport[0] == 'done':
            save_airports(config)
            break
        else:
            led = input("    LED position: ")

            config.update({led: airport[0]}) 

            print('[SUCCESS]: Assigned %s to LED at positon %s' % (airport[1], led))
            

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


if __name__ == "__main__":
    start_wizard()

    loop = True
    while loop:
        loop = get_command()
