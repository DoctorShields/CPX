# This program prints (and can plot) the x, y, and z acceleration values

# We're going to import these two modules in nearly every program
# Sleep allows us to, well, sleep.  The CPX will run a while loop WAY too fast without a pause of some sort.
# And when we import cpx, we get all kinds of cool functionality
from time import sleep
from adafruit_circuitplayground.express import cpx

# We don't always need a while True loop, but it's super common if we want to do stuff over and over.
while True:
    # Read the acceleration data from the CPX.  This will return a *tuple* of three elements
    accel = cpx.acceleration
    # accel is now a tuple of three things, x, y, and z.  You can access them by typing accel.x, accel.y, and accel.z
    # Open your serial monitor and you'll see a stream of three-element tuples.
    # THE FUN PART: open your serial *plotter* and you'll see a plot of these three values!
    # Notice the format to get the plotter to work is is print((a tuple, which has it's own parentheses))
    # So, even if I wanted to plot just accel.x, I'd type print((accel.x,)).  That comma means it's a tuple
    print((accel.x,accel.y,accel.z))
    # I don't want to print a bajillion times per second, so let's sleep for a tiny bit.
    sleep(.1)