import RPi.GPIO as GPIO
from . import (gpio_mode_str,
               gpio_mode_str_rev,
               gpio_state_str,
               gpio_state_str_rev,
               gpio_pins,
               rgstd_gpio_pins)
from .gpio_exceptions import (dec_check_pin,
                              dec_check_pins,
                              dec_check_out_pins,
                              dec_check_pin_rgstd,
                              dec_check_pins_rgstd,
                              check_io_mode_arg,
                              NoSuchPinException,
                              InvalidIOMode,
                              PinNotRegisteredException)
from .logging import (info, debug, warning, error)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


@dec_check_pin
def get_gpio_function(pin):
    debug ('get_gpio_function called', {'pin':pin})
    return gpio_mode_str[GPIO.gpio_function(pin)]


@dec_check_pin
@dec_check_pin_rgstd
def get_gpio_state(pin):
    debug('get_gpio_state called', {'pin':pin})
    return gpio_state_str[GPIO.input(pin)]


@dec_check_pins
def set_gpio_function(pins, mode):
    debug('gpio_pin_setup called', {'pins':pins})
    check_io_mode_arg(mode)
    if type(mode) is str:
        mode = gpio_mode_str_rev[mode]
    [GPIO.setup(_, mode) for _ in pins]
    [rgstd_gpio_pins.add(_) for _ in pins]


@dec_check_pins
@dec_check_pins_rgstd
@dec_check_out_pins
def switch_on(pins):
    debug('switch_on called', {'pins':pins})
    [GPIO.output(_, GPIO.HIGH) for _ in pins]


@dec_check_pins
@dec_check_pins_rgstd
@dec_check_out_pins
def switch_off(pins):
    debug('switch_off called', {'pins':pins})
    [GPIO.output(_, GPIO.LOW) for _ in pins]


def get_gpio_info(pin=None):
    debug('get_gpio_info called', {'pin':pin})
    @dec_check_pin
    @dec_check_pin_rgstd
    def _get_info(_pin):
        return {
            _pin: {
                'mode' : get_gpio_function(_pin),
                'state' : get_gpio_state(_pin)
            }    
        }
    if pin:
        return _get_info(pin)
    return [_get_info(_) for _ in rgstd_gpio_pins]


if __name__ == '__main__':
    try:
        set_gpio_function([21,20], 'output')
        _ = get_gpio_info()
        info('----')
        info(_)
        info('----')
    except NoSuchPinException:
        error('NoSuchPinException Exception printed')
    except InvalidIOMode:
        error('InvalidIOMode Exception printed')
    except PinNotRegisteredException:
        error('PinNotRegisteredException Exception printed')
