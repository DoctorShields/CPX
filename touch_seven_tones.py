from time import sleep
from adafruit_circuitplayground.express import cpx

while True:
    arr = [cpx.touch_A1, cpx.touch_A2, cpx.touch_A3, cpx.touch_A4, cpx.touch_A5, cpx.touch_A6, cpx.touch_A7]
    touched = False
    for i, pad in enumerate(arr):
        if pad:
            print(i+1)
            cpx.start_tone(220*(i+1))
            touched = True
    if not touched:
        cpx.stop_tone()
    sleep(0.05)