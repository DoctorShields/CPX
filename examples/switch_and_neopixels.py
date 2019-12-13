# This program lights 5 neopixels, based on the switch position

# We're going to import these two modules in nearly every program
# Sleep allows us to, well, sleep.  The CPX will run a while loop WAY too fast without a pause of some sort.
# And when we import cpx, we get all kinds of cool functionality
from time import sleep
from adafruit_circuitplayground.express import cpx

# We don't always need a while True loop, but it's super common if we want to do stuff over and over.
while True:
    # cpx.switch is true or false
    if(cpx.switch):
        # make the first 5 pixels green and the rest off
        for p in range(0,5):
            cpx.pixels[p] = (0,10,0)
        for p in range(6,10):
            cpx.pixels[p] = (0,0,0)
    else:
        # make the first 5 pixels off and the rest red
        for p in range(0,5):
            cpx.pixels[p] = (0,0,0)
        for p in range(6,10):
            cpx.pixels[p] = (10,0,0)
    # I don't want to run this a bajillion times per second, so let's sleep for a tiny bit.
    sleep(.1)