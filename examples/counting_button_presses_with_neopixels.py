# This program counts button presses and demonstrates how to only count once per click

# We're going to import these two modules in nearly every program
# Sleep allows us to, well, sleep.  The CPX will run a while loop WAY too fast without a pause of some sort.
# And when we import cpx, we get all kinds of cool functionality
from time import sleep
from adafruit_circuitplayground.express import cpx

count = 0
buttonA = False

# We don't always need a while True loop, but it's super common if we want to do stuff over and over.
while True:
    # we're using buttonA to track the *last* button state
    # so this statement is only true if button_a is pressed and it *wasn't* pressed last cycle
    if cpx.button_a and not buttonA:
        count += 1
    buttonA = cpx.button_a
    # if you get past 10, restart
    if count > 10:
        cpx.pixels.fill((0,0,0))
        count = 0
    # light the correct number of pixels
    for p in range(0,count):
        cpx.pixels[p] = (128,64,0)
    print(count)
    sleep(.1)