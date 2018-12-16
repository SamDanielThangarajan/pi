import RPi.GPIO as GPIO
import time
import signal
import sys

eye1 = 21
eye2 = 20

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

all_lights = [eye1, eye2]

###################################
## Controller Functions
###
def switch_on(id=None):
    if id is not None:
        GPIO.output(id, GPIO.HIGH)
        return
    for i in all_lights:
        GPIO.output(i, GPIO.HIGH)

    
def switch_off(id=None):
    if id is not None:
        GPIO.output(id, GPIO.LOW)
        return
    for i in all_lights:
        GPIO.output(i, GPIO.LOW)

def signal_handler(sig, frame):
    switch_off()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)    

for i in all_lights:
    GPIO.setup(i, GPIO.OUT)

def blink_eyes():
    switch_on()
    time.sleep(0.5)
    switch_off()
    time.sleep(0.5)

while True:
    blink_eyes()


#while True:
#    for count in range(1,10):
#        police_lights()
#    for count in range(1,10):
#        police_lights_ext()
#    for count in range(1,10):
#        circle_formation_with_rev()
