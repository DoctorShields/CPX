# This program prints true or false based on the switch position.  That's it.

# We're going to import these two modules in nearly every program
# Sleep allows us to, well, sleep.  The CPX will run a while loop WAY too fast without a pause of some sort.
# And when we import cpx, we get all kinds of cool functionality
from time import sleep
from adafruit_circuitplayground.express import cpx

# We don't always need a while True loop, but it's super common if we want to do stuff over and over.
while True:
    print(cpx.switch)
    # I don't want to print a bajillion times per second, so let's sleep for a tiny bit.
    sleep(.25)