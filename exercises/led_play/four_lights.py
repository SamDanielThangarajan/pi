import RPi.GPIO as GPIO
import time
import signal
import sys

red = 21
blue = 20
green = 26
yellow = 19

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

###################################
## Controller Functions
###
def switch_on(color=None):
    if color is not None:
        GPIO.output(color, GPIO.HIGH)
        return
    for i in red, blue, green, yellow:
        GPIO.output(i, GPIO.HIGH)

    
def switch_off(color=None):
    if color is not None:
        GPIO.output(color, GPIO.LOW)
        return
    for i in red, blue, green, yellow:
        GPIO.output(i, GPIO.LOW)

def signal_handler(sig, frame):
    switch_off()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)    

for i in red, blue, green, yellow:
    GPIO.setup(i, GPIO.OUT)

####################################
## Formation functions
###

def police_lights():
    switch_on(red)
    time.sleep(0.2)
    switch_on(blue)
    switch_off(red)
    time.sleep(0.2)
    switch_off(blue)

def police_lights_ext():
    switch_on(red)
    switch_on(yellow)
    time.sleep(0.2)
    switch_on(blue)
    switch_on(green)
    switch_off(red)
    switch_off(yellow)
    time.sleep(0.2)
    switch_off(blue)
    switch_off(green)

def circle_formation():
    for i in red, blue, yellow, green:
        switch_on(i)
        time.sleep(0.2)
        switch_off(i)

def circle_formation_with_rev():
    ''' Forward '''
    for count in range(1,6):
        for i in red, blue, yellow, green:
            switch_on(i)
            time.sleep(0.2)
            switch_off(i)
    ''' Blink '''
    for count in range(1,4):
        switch_on()        
        time.sleep(0.2)
        switch_off()
        time.sleep(0.2)
    ''' Reverse '''
    for count in range(1,6):
        for i in green, yellow, blue, red:
            switch_on(i)
            time.sleep(0.2)
            switch_off(i)

while True:
    for count in range(1,10):
        police_lights()
    for count in range(1,10):
        police_lights_ext()
    for count in range(1,10):
        circle_formation_with_rev()
