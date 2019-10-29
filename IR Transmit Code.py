import time
from adafruit_circuitplayground.express import cpx
import adafruit_irremote
import pulseio
import board

pwm = pulseio.PWMOut(board.IR_TX, frequency=38000, duty_cycle=2**15)
pulseout = pulseio.PulseOut(pwm)
encoder = adafruit_irremote.GenericTransmit(header=[9500,4500],one=[550,550],zero=[550,1700],trail=0)

print("Transmit is blue")

while True:
    cpx.pixels.fill((0,0,100))
    if cpx.button_a:
        print("Button A pressed. \n")
        cpx.red_led = True
        # I guess we always encode 4 bytes?
        encoder.transmit(pulseout, [255,2,255,0])
        cpx.red_led = False
        cpx.pixels.fill((100,0,0))
        time.sleep(.2)
    if cpx.button_b:
        print("Button B pressed. \n")
        cpx.red_led = True
        encoder.transmit(pulseout, [255,2,191,64])
        cpx.red_led = False
        cpx.pixels.fill((0,100,0))
        time.sleep(.2)
    time.sleep(0.05)