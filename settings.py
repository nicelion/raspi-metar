from configparser import ConfigParser

config =  ConfigParser()
config.read('raspi-metar.conf')
config.sections()

airports = config['airports']
default_country_code = config['settings']["default_country_code"]
refresh_rate = config.getint('settings', 'refresh_rate')
animation_duration = config.getint('settings', 'animation_duration')
show_lightning = config.getboolean('settings', 'show_lightning')
brightness = config.getint('settings', 'brightness')
number_of_leds = config.getint('settings', 'number_of_leds')

vfr_color = config['colors']['vfr']
ifr_color = config['colors']['ifr']
mvfr_color = config['colors']['mvfr']
lifr_color = config['colors']['lifr']
snow_color = config['colors']['snow']
tornado_color = config['colors']['tornado']
fog_color = config['colors']['fog'] 