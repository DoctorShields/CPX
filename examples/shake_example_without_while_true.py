# This program uses cpx.shake() to detect shaking.

# We're going to import these two modules in nearly every program
# Sleep allows us to, well, sleep.  The CPX will run a while loop WAY too fast without a pause of some sort.
# And when we import cpx, we get all kinds of cool functionality
from time import sleep
from adafruit_circuitplayground.express import cpx

phase = 1

# Hey, an exaple of some semi-forever loops.  These while loops run until the phase changes
while phase == 1:
    print("Phase 1")
    cpx.pixels.fill((10,0,0))
    if cpx.shake():
        phase = 2
    sleep(.1)

while phase == 2:
    print("Phase 2")
    cpx.pixels.fill((0,10,0))
    if cpx.shake():
        phase = 3
    sleep(.1)

print("done")