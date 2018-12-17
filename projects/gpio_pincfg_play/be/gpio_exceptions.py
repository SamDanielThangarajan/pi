from . import (gpio_pins,
               gpio_mode_str,
               gpio_mode_str_rev,
               rgstd_gpio_pins) 
import RPi.GPIO as GPIO


class NoSuchPinException(Exception):
    pass


class PinNotRegisteredException(Exception):
    pass


class InvalidPinException(Exception):
    pass


class InvalidIOMode(Exception):
    pass


def dec_check_pin(func):
    def inner(pin, *args, **kwargs):
        if pin not in gpio_pins:
            raise NoSuchPinException
        return func(pin, *args, **kwargs)
    return inner 


def dec_check_pins(func):
    def inner(pins, *args, **kwargs):
        if pins is None:
            raise NoSuchPinException
        for pin in pins:
            if pin not in gpio_pins:
                raise NoSuchPinException
        return func(pins, *args, **kwargs)
    return inner 


def dec_check_out_pins(func):
    def inner(pins, *args, **kwargs):
        if pins is None:
            raise NoSuchPinException
        for pin in pins:
            if GPIO.gpio_function(pin) != GPIO.OUT:
                raise InvalidIOMode
        return func(pins, *args, **kwargs)
    return inner


def dec_check_pins_rgstd(func):
    def inner(pins, *args, **kwargs):
        for pin in pins:
            if pin not in rgstd_gpio_pins:
                raise PinNotRegisteredException
        return func(pins, *args, **kwargs)
    return inner


def dec_check_pin_rgstd(func):
    def inner(pin, *args, **kwargs):
        if pin not in rgstd_gpio_pins:
            raise PinNotRegisteredException
        return func(pin, *args, **kwargs)
    return inner


def check_io_mode_arg(mode):
    if type(mode) is int and mode in gpio_mode_str:
        return
    if type(mode) is str and mode in gpio_mode_str_rev:
        return
    raise InvalidIOMode
