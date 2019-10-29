import time
from adafruit_circuitplayground.express import cpx
import adafruit_irremote
import pulseio
import board

# PulseIn reads microsecond times between high and low voltage
# This one will read up to 120 pulses
# Most IR receivers idle high (true)
# pulsein will be a list of microsecond durations
pulsein = pulseio.PulseIn(board.IR_RX, maxlen=120, idle_state=True)
# most IR remotes are similar enough, we can use a generic decoder
decoder = adafruit_irremote.GenericDecode()

print("Receive is orange")
cpx.pixels.fill((100,50,0))
time.sleep(2)

while True:
    #the read_pulses() function waits for something to be detected
    pulses = decoder.read_pulses(pulsein)
    try:
        # decode_bits() decodes into bits.  duh.
        # received_code = decoder.decode_bits(pulses, debug=False)
        received_code = decoder.decode_bits(pulses)
    except adafruit_irremote.IRNECRepeatException:
        print("repeat exception")
        continue
    except adafruit_irremote.IRDecodeException as e:
        print(e.args)
        continue
    print("code received: ", received_code)
    if received_code == [255,2,255,0]:
        print("button A received!")
        cpx.pixels.fill((100,0,0))
    if received_code == [255,2,191,64]:
        print("button B received!")
        cpx.pixels.fill((0,100,0))