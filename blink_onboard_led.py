from time import sleep
from adafruit_circuitplayground.express import cpx

while True:
    cpx.red_led = True
    print("on")
    sleep(0.5)
    cpx.red_led = False
    print("off")
    sleep(0.5)