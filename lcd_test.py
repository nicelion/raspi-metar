import lcddriver
import time
from avwx import Metar
import threading







display = lcddriver.lcd()



try:
    def long_string(display, text = '', num_line = 1, num_cols = 16):
        if (len(text) > num_cols):
            display.lcd_display_string(text[:num_cols], num_line)
            time.sleep(1)

            for i in range(len(text) - num_cols + 1):
                text_to_print = text[i:i+num_cols]
                display.lcd_display_string(text_to_print,num_line)
                time.sleep(0.5)
            time.sleep(1)
        else:
            display.lcd_display_string(text, num_line)
    
    def center_text(string):
        length = len(string)

        l = ""
        for _ in range(1, length - 16):
            pass


    m = Metar('KGMU')
    m.update()

    display.lcd_display_string('   Welcome To', 1)
    display.lcd_display_string('  raspi-metar!', 2)

    time.sleep(1)

    display.lcd_display_string('      Created by', 1)
    display.lcd_display_string('           Ian Thompson', 2)  
    display.lcd_clear()
    while True:
        display.lcd_display_string('   KGMU METAR', 1)
        display.lcd_display_string(m.data.flight_rules + ' Conditions', 2)
        time.sleep(1)
        long_string(display, m.data.raw, 2)
        display.lcd_clear()
        time.sleep(1)


except KeyboardInterrupt:
    display.lcd_clear()