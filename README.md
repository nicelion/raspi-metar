# raspi-metar (WORK IN PROGRESS)

Yet another python program to create a METAR map with your Raspberry Pi
## Table of Contents
- [About](#about)
- [Things You'll Need](#things-youll-need)
- [Setting Up Your Project](#seting-up-your-project)
- [setup.py](#setuppy)
	- [Assigning Airports to LEDs](#assigning-airports-to-leds)
- [Glossary](#glossary)
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

### Dependenies

There are a few python dependencies you need to install

  

-  `pip3 install avwx`

-  `pip3 install adafruit-circuitpython-neopixel`

  

### setup.py

`setup.py` is a tool that automates project configuration. You will need to run this BEFORE you begin your project. Here you will be able to assign LEDs to specific airports, change colors, refresh rates, etc.

### Manual Configuration
Inside the `raspi-metar` directory, you'll find a file named `raspi-metar.conf`. Use your favorite text editor to open it if you want to edit it manually.

Below is an example of what the file looks like:
```
[settings]
refresh_rate = 1800
show_lightning = yes
brightness = 10

[colors]
vfr = (0, 255, 0)
ifr = (255, 0, 0)
lifr = (255, 0, 255)
mvfr = (0, 0, 255)

[airports]
1 = KCEU
2 = KGMU
3 = KSPA
4 = KAND
```
  - SETTINGS
	  - refresh_rate
		  - A whole number greater than one which represents how often data will be updated in SECONDS.
	- show_lightning
		- yes/no if you want LEDs to flash when airport is reporting lighting in vicnity
	- brightness
		- A whole number 1-100 determining how bright you want your LEDs to shine
- COLORS
	- RGB values for the different flight conditions
- AIRPORTS
	- Set a whole number = to ICAO ident. The number represents LED index and obviously the ICAO index represents the airport its assigned to.
	- These do not need to be in order, but must follow this convention.

### Assigning Airports to LEDs

Once you have started `setup.py`, you will be asked to enter a command. To add airports all at once, type `add all`.

You will be asked for the [ICAO](#icao) identifier for the airport you want to add and the LED position you want to assign it to.

  

**Note:** Becuase [METAR](#metar) information is availible for airports in countries other than the US, you *must* add the country code prefix to the [ICAO](#icao) ident. For example, Los Angeles International Airport is commonly referred to in the US as LAX. However, you must enter KLAX for the program to recognize it.

  

#### Example:

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

## Glossary
Here is that glossary I was talking about. You can find definitions and explanations about some of the vocabulary used in this project.

#### ICAO
The ICAO, or [International Civil Aviation Organization](https://en.wikipedia.org/wiki/International_Civil_Aviation_Organization), is a United Nations agency tasked with controlling and creating international aviation regulations and guidelines.

#### METAR
What the heck is METAR? That is a great question! METAR stands for METerological Aerodome Report. Essentially, it a weather report in a very specific format that pilots use. Most "towered" airports, meaning one with an Air Traffic Control tower, will issue these METAR reports every hour, or when conditions change enough to warrant.

When a pilot decides they want to take off or land, it is crucial for them to get the latest METAR report so they can know what the runway conditions are going to be like. 

##### So what does a METAR look like?
Here is an example METAR report from a local airport:
`KGMU 052153Z 22009KT 10SM SCT032 29/21 A2990 RMK AO2 LTG DSNT N SLP113 T02890211`

Don't know whats going on? Yeah, I don't really either! If you want more info on METARs and how to read them, check out the [Wikipedia page](https://en.wikipedia.org/wiki/METAR)!