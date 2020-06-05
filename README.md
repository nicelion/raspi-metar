# raspi-metar (WORK IN PROGRESS)

Yet another python program to create a METAR map with your Raspberry Pi

## About
In short, `raspi-metar` is a Raspberry Pi project that takes METAR data from various airports and displays it on a VFR sectional map using NEOPIXEL LEDs.

I know, there are other projects just like this on GitHub. However, I love learning. I wanted to expand my knowledge of python and see if I could create this myself! I wanted to look at this thing up on my wall and have the satisfaction that I made it myself.

I hope that you find this project interesting. I hope it can be used as a tool to learn about computers, weather, and aviation: some of my favorite things! (Huge nerd)

This project is not solely intended on you avgeeks, rather, anyone interested in computers, weather, or aviation. I feel like a lot of "beginner" Raspberry Pi projects tend to be weather tools that you'll never use or provide limited value or entertainment. This project is intended to be super beginner friendly and NOT limited to us avgeeks! Yes, you'll find a lot of aviation terms in this project, but think of it as a way to learn more about a new subject. Plus, I'll try to add a glossary at the end for some terms you may not know so if you see an unfamiliar word with a hyperlink, click on it!


## Things You'll Need
You're gonna need a couple of things to complete this project. Do note, for this project, I have elected to follow the policy of "go big or go home" so I am using a VFR sectional map of the ENTIRE United States measuring 3.5x5ft! You can easily use a smaller map, or even use regional maps!

- Raspberry Pi (any newish model should work)
- VFR Sectional Map
- Poster board
- WS2811 addressable LED modules (amount is up to you)
- Power supply for LEDs
- Spray adhesive
- Drill
- An internet connection
- A desire to learn
## Seting Up Your Project

#### Dependenies

There are a few python dependencies you need to install

  

-  `pip3 install avwx`

-  `pip3 install adafruit-circuitpython-neopixel`

  

## setup.py

`setup.py` is a tool that automates project configuration. You will need to run this BEFORE you begin your project. Here you will be able to assign LEDs to specific airports, change colors, refresh rates, etc.

  

### Assigning Airports to LEDs

Once you have started `setup.py`, you will be asked to enter a command. To add airports all at once, type `add all`.

You will be asked for the ICAO identifier for the airport you want to add and the LED position you want to assign it to.

  

**Note:** Becuase METAR information is availible for airports in countries other than the US, you *must* add the country code prefix to the ICAO ident. For example, Los Angeles International Airport is commonly referred to in the US as LAX. However, you must enter KLAX for the program to recognize it.

  

####Example:

Below is a terminal excerpt if you wantted to assign Greenville Spartanburg International Airport to LED 15:

  

```

Welcome to Setup Wizard

Enter a command to get started: add all

Assign ICAO idents to LED position. For example, when asked you would pas 'KJFK' and '10' if you wanted to assign John F. Kennedy International Airport to use LED 10.

When finished, pass done

Enter ICAO ident (Kxxx): KGSP

LED position: 15

[SUCCESS]: Assigned Greenville Spartanburg International Airport to LED at positon 15

Enter ICAO ident (Kxxx): done

[SUCCESS]: Saved airports to file.

```
