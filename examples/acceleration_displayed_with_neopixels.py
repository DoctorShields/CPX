# This program lights 0-10 pixels, based on the x acceleration.

# We're going to import these two modules in nearly every program
# Sleep allows us to, well, sleep.  The CPX will run a while loop WAY too fast without a pause of some sort.
# And when we import cpx, we get all kinds of cool functionality
from time import sleep
from adafruit_circuitplayground.express import cpx

# We don't always need a while True loop, but it's super common if we want to do stuff over and over.
while True:
    # Read the acceleration data from the CPX.  This will return a *tuple* of three elements
    accel = cpx.acceleration
    # extract just the x acceleration, round it to an integer, and take the absolute value
    x = abs(int(accel.x))
    # make sure it's never more than 10
    if x > 10:
        x = 10
    # light up pixels less than the x value
    for pix in range(0,10):
        if pix < x:
            cpx.pixels[pix] = (0,0,100)
        else:
            cpx.pixels[pix] = (0,0,0)
    print(x)
    # I don't want to print a bajillion times per second, so let's sleep for a tiny bit.
    sleep(.05)