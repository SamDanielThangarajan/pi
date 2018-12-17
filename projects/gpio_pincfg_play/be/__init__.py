import RPi.GPIO as GPIO

gpio_mode_str = {
    GPIO.OUT : 'output',
    GPIO.IN : 'input' 
}

gpio_mode_str_rev = {
    'output' : GPIO.OUT,
    'input' : GPIO.IN
}

gpio_state_str = {
    GPIO.HIGH : 'on',
    GPIO.LOW : 'off'
}

gpio_state_str_rev = {
   'on' : GPIO.HIGH,
   'off' : GPIO.LOW
}

gpio_pins = frozenset([2,3,4,14,15,18,17,27,22,23,24,10,9,11,25,8,7,5,6,12,13,19,26,16,20,21])
gpio_pins_count = len(gpio_pins)

rgstd_gpio_pins = set()
