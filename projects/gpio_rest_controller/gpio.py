import RPi.GPIO as GPIO

__initialized = False

def initialize():
    global __initialized
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(21,GPIO.OUT)
    GPIO.setup(21,GPIO.LOW)
    __initialized = True

def switch_on(no):
    if not __initialized:
        initialize()
    print ("Switching on : ", no)
    GPIO.output(21,GPIO.HIGH)

def switch_off(no):
    if not __initialized:
        initialize()
    print ("Switching off : ", no)
    GPIO.output(21,GPIO.LOW)
