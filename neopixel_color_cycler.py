from time import sleep
from adafruit_circuitplayground.express import cpx

brightness = 10

red = (brightness,0,0)
grn = (0,brightness,0)
blu = (0,0,brightness)
yel = (brightness,brightness,0)
cyn = (0,brightness,brightness)
mag = (brightness,0,brightness)

colorArray = [["red",red],["green",grn],["blue",blu],["yellow",yel],["cyan",cyn],["magenta",mag]]

while True:
    for col in colorArray:
        print(col[0])
        cpx.pixels.fill(col[1])
        sleep(0.5)
