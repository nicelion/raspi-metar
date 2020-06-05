# raspi-metar (WORK IN PROGRESS)
Yet another python program to create a METAR map with your Raspberry Pi

## Seting Up Your Project
#### Dependenies
There are a few python dependencies you need to install

- `pip3 install avwx`
- `pip3 install adafruit-circuitpython-neopixel`

## setup.py
`setup.py` is a tool that automates project configuration. You will need to run this BEFORE you begin your project. Here you will be able to assign LEDs to specific airports, change colors, refresh rates, etc.

### Assigning Airports to LEDs
Once you have started `setup.py`, you will be asked to enter a command. To add airports all at once, type `add all`.
You will be asked for the ICAO identifier for the airport you want to add and the LED position you want to assign it to. 

**Note:** Becuase METAR information is availible for airports in countries other than the US, you *must* add the country code prefix to the ICAO ident. For example, Los Angeles International Airport is commonly referred to in the US as LAX. However, you must enter KLAX for the program to recognize it.

##### Example
Below is a terminal excerpt if you wantted to assign Greenville Spartanburg International Airport to LED 15:

```
Welcome to Setup Wizard
Enter a command to get started: add all
Assign ICAO idents to LED position. For example, when asked you would pas 'KJFK' and '10' if you wanted to assign John F. Kennedy International Airport to use LED 10.
When finished, pass done
    Enter ICAO ident (Kxxx): KGSP
    LED position: 15
[SUCCESS]: Assigned Greenville Spartanburg International Airport to LED at positon 15
    Enter ICAO ident (Kxxx): exit
[SUCCESS]: Saved airports to file.
```