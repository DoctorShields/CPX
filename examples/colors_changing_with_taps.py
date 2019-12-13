# This program cycles through the rainbow then tapped

# We're going to import these two modules in nearly every program
# Sleep allows us to, well, sleep.  The CPX will run a while loop WAY too fast without a pause of some sort.
# And when we import cpx, we get all kinds of cool functionality
from time import sleep
from adafruit_circuitplayground.express import cpx

# colors are tuples
red = (100,0,0)
org = (100,40,0)
yel = (100,100,0)
grn = (0,100,0)
blu = (0,0,100)
pur = (100,0,100)

# this is an array of colors
colors = [red, org, yel, grn, blu, pur]
count = 0

while True:
    # make all of the pixels a color in the color array
    cpx.pixels.fill(colors[count])
    # if tapped, go on to next color
    if cpx.tapped:
        count += 1
    # my array is only 6 elements
    if count >= 5:
        count = 0
