# This program lights neopixels based on which button is pressed

# We're going to import these two modules in nearly every program
# Sleep allows us to, well, sleep.  The CPX will run a while loop WAY too fast without a pause of some sort.
# And when we import cpx, we get all kinds of cool functionality
from time import sleep
from adafruit_circuitplayground.express import cpx

# We don't always need a while True loop, but it's super common if we want to do stuff over and over.
while True:
    if cpx.button_a:
        # light the first 5
        for p in range(0,5):
            cpx.pixels[p] = (0,10,0)
    elif cpx.button_b:
        # light the last 5
        for p in range(6,10):
            cpx.pixels[p] = (0,10,0)
    else:
        #black
        cpx.pixels.fill((0,0,0))
    sleep(.1)