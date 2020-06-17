from configparser import ConfigParser

config =  ConfigParser()
config.read('raspi-metar.conf')
config.sections()

airports = config['airports']
refresh_rate = config.getint('settings', 'refresh_rate')
animation_duration = config.getint('settings', 'animation_duration')
show_lightning = config.getboolean('settings', 'show_lightning')
brightness = config.getint('settings', 'brightness')
i2c_display_enabled = config.getboolean('settings', 'i2c_display_enabled')

vfr_color = config['colors']['vfr']
ifr_color = config['colors']['ifr']
mvfr_color = config['colors']['mvfr']
lifr_color = config['colors']['lifr']
snow_color = config['colors']['snow']
tornado_color = config['colors']['tornado']
fog_color = config['colors']['fog']