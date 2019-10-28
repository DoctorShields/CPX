import time
import board
import pulseio
from adafruit_motor import servo
from adafruit_circuitplayground.express import cpx

pinArray = [board.A1, board.A2, board.A3]

pwmList = []
for pin in pinArray:
    pwmList.append(pulseio.PWMOut(pin, duty_cycle=2**15,frequency=50))

servoList = []
for pwm in pwmList:
    servoList.append(servo.Servo(pwm))

while True:
    print("moving")
    for s in servoList:
        s.angle = 0
    time.sleep(1)
    for s in servoList:
        s.angle = 180
    time.sleep(1)

print("success")
