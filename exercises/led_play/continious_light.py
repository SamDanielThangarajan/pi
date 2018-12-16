import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(21, GPIO.OUT)

def flick():
   GPIO.output(21, GPIO.HIGH)
   time.sleep(0.5)
   GPIO.output(21, GPIO.LOW)
   time.sleep(0.5)


if __name__ == '__main__':
   flick()
   flick()
   flick()
   flick()
   flick()
