from flask import (Flask,
                   request)
from flask_restful import (Api,
                           Resource,
                           reqparse,
                           abort)
from .gpio import (switch_on,
                  switch_off,
                  get_gpio_info,
                  set_gpio_function)
from .logging import(debug,
                     info,
                     warning,
                     error)
from . import (gpio_pins,
               rgstd_gpio_pins)
import RPi.GPIO as GPIO

error_handling = {
    'NoSuchPinException' : {
        'message' : 'No Such pin exists in the Pi',
        'status' : 400
    },
    'PinNotRegisteredException' : {
        'message' : 'Pin is not registered yet',
        'status' : 400
    },
    'InvalidPinException' : {
        'message' : 'Invalid Pin',
        'status' : 400
    },
    'InvalidIOMode' : {
        'message' : 'Invalid IO mode value',
        'status' : 400
    }
}

application = Flask(__name__)
api = Api(application, errors=error_handling)

gpios_post_parser = reqparse.RequestParser(trim=True, bundle_errors=True)
gpios_post_parser.add_argument('pin',
                               type=int,
                               required=True,
                               help='GPIO pin(BCM) to configure')
gpios_post_parser.add_argument('mode',
                               type=str,
                               required=True,
                               help='Mode of pin, input|output')
gpios_post_parser.add_argument('switch',
                               type=str,
                               required=False,
                               help='Switch on|off the pin')

gpio_put_parser = reqparse.RequestParser(trim=True, bundle_errors=True)
gpio_put_parser.add_argument('switch',
                             type=str,
                             required=True,
                             help='Switch on|off the pin')


class InvalidValueForSwitchException(Exception):
    pass


def _switch_pin(pin, val):
    global error_handling
    if val is None:
        return
    if val.lower() == 'on':
        switch_on([pin])
    elif val.lower() == 'off':
        switch_off([pin])
    else:
        # Add the exception handler 
        if 'InvalidValueForSwitchException' not in error_handling:
            error_handling['InvalidValueForSwitchException'] = {
                'message' : 'Invalid value for Switch',
                'status' : 400
            }
        raise InvalidValueForSwitchException


class gpios(Resource):
    def get(self):
        debug('GET on <gpios>, args: ', request.args)
        if 'list' in request.args:
            if request.args['list'] == 'all':
                return {'gpios' : list(gpio_pins)}
            elif request.args['list'] != 'reg':
                abort(400, 'Invalid value for list, Supported values all|reg')
        return {'gpios' : get_gpio_info()}

    def post(self):
        debug('POST on <gpios>')
        args = gpios_post_parser.parse_args(strict=True)
        debug('Args : ' , {'args': args})
        set_gpio_function([args['pin']], args['mode'].lower())
        _switch_pin(args['pin'], args['switch'])
        return {'gpios': get_gpio_info(args['pin'])}, 201


class gpio(Resource):

    def get(self, pin):
        debug('GET on <gpio>', {'pin':pin})
        return {'gpios': get_gpio_info(pin)}

    def put(self, pin):
        debug('POST on <gpio>')
        args = gpio_put_parser.parse_args(strict=True)
        debug('Args : ' , {'args': args})
        _switch_pin(pin, args['switch'])
        return {'gpios': get_gpio_info(pin)}


api.add_resource(gpios, "/gpios")
api.add_resource(gpio, "/gpio/<int:pin>", endpoint = 'pin')


if __name__ == '__main__':
    application.run(debug=True)
