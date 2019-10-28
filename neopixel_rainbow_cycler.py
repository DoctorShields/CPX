from time import sleep
from adafruit_circuitplayground.express import cpx

brightness = 10

red = (brightness,0,0)
grn = (0,brightness,0)
blu = (0,0,brightness)
yel = (brightness,brightness,0)
cyn = (0,brightness,brightness)
mag = (brightness,0,brightness)
org = (brightness,int(brightness/2),0)

colorArray = [["red",red],["orange",org],["yellow",yel],["green",grn],["cyan",cyn],["blue",blu],["magenta",mag]]

i = 0

while True:
    j = i%10
    for k in range(0,10):
        if(k-j >= 0 and k-j <= len(colorArray)-1):
            cpx.pixels[k] = colorArray[k-j][1]
    sleep(0.5)
    i += 1
