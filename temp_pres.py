from machine import I2C, Pin
import time
from bmp280 import *
import st7789
import tft_config
import vga1_bold_16x32 as font

bus = I2C(0, sda=Pin(43), scl=Pin(44))
bmp = BMP280(bus)

tft = tft_config.config(1)
tft.init()
tft.jpg(f'FondoBMP.jpg', 0, 0, st7789.SLOW)
while True:
    try:
        tft.text(font,"Temp:",50,50)
        tft.text(font, str(bmp.temperature),130,50)
        tft.text(font,"Pres:",50,80)
        tft.text(font, str(bmp.pressure/100),130,80)
        time.sleep(5)
    except:
        tft.deinit()
        
    
    
    