import board
import neopixel

from random import randrange

import time
print("Animating")

r = 650
pixels = neopixel.NeoPixel(board.D18, r, brightness=0.1, auto_write=False)

# COLORS
green = (255, 0, 0)
red = (0, 255, 0)
blue = (0, 0, 255)
off = (0, 0, 0)


def blink():

    pixels.fill(red)
    pixels.show()

    time.sleep(0.1)

    pixels.fill(blue)
    pixels.show()
    
    time.sleep(0.1)

    pixels.fill(green)
    pixels.show()
    
    time.sleep(0.1)

    pixels.fill(off)
    pixels.show()


blink()