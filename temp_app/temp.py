# bmp stuff
import time 
from breakout_bmp280 import BreakoutBMP280
from pimoroni_i2c import PimoroniI2C

PINS_BREAKOUT_GARDEN = {"sda": 4, "scl": 5}
PINS_PICO_EXPLORER = {"sda": 20, "scl": 21}

i2c = PimoroniI2C(**PINS_BREAKOUT_GARDEN)
bmp = BreakoutBMP280(i2c)
hold_temp = 0
# bmp stuff
import badger2040
from badger2040 import WIDTH

TEXT_SIZE = 0.45
LINE_HEIGHT = 20

display = badger2040.Badger2040()
display.thickness(2)
display.font("sans")
#display.text("Press button A" ,0, y, TEXT_SIZE)
### image
my_image = bytearray(int(296 * 128 / 8))
open("temp_background.bin", "r").readinto(my_image)
display.image(my_image)
### image
display.led(128)
display.pen(0)
display.rectangle(0, 0, WIDTH, 16)
display.thickness(1)
display.pen(15)
display.text("badgerOS", 3, 8, 0.4)
display.text("Temp", WIDTH - display.measure_text("temp", 0.4) - 4, 8, 0.4)
display.pen(0)
#TEXT_SIZE = 0.62
TEXT_SIZE = 1
y = 20 + int(LINE_HEIGHT / 2)
display.update()
while True:
    if display.pressed(badger2040.BUTTON_A):
        display.pen(15) # dark
#        display.pen(0) # light
        display.rectangle(10,50,150,30)
#        partial_update(x,y,w,h)
#        display.partial_update(0,40,150,20)
        reading = bmp.read()
#        display.pen(15) # dark 
        display.pen(0) # light
        display.thickness(2)
#        display.thickness(1)
        display.font("serif")
#        display.text("Temperature °C",3, 30, TEXT_SIZE)
        display.text(""+str(reading[0]) ,45, 65, TEXT_SIZE)
#        display.text("test"+str(hold_temp[0]), 1, 70, TEXT_SIZE)
#        y += LINE_HEIGHT
#        display.update_speed(badger2040.UPDATE_TURBO)
        display.update()
#        display.partial_update(2,40,150,20)
        display.halt()

#    if display.pressed(badger2040.BUTTON_B):
#        hold_temp = bmp.read()
#        display.pen(100)
#        display.rectangle(2,70,150,20)
#        display.pen(0)
#        display.thickness(2)
#        display.font("serif")
#        display.text("Hold "+str(hold_temp[0]), 1, 70, TEXT_SIZE)
#        display.update()
#        display.halt()
