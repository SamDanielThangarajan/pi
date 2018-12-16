import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.OUT)

print "Led ON"
GPIO.output(21, GPIO.HIGH)
time.sleep(1)

print "Led OFF"
GPIO.output(21, GPIO.LOW)
