import board
import neopixel

from random import randrange

import time
print("Animating")

r = 650
pixels = neopixel.NeoPixel(board.D18, r, brightness=0.1, auto_write=False)

pixels.fill((0, 0, 0))
pixels.show()