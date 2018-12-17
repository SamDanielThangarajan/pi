import os

# Levels
_debug = 0
_info = 1
_warning = 2
_error = 3

#string to level map
_str_to_level = {
    'debug' : _debug,
    'info' : _info,
    'warning' : _warning,
    'error' : _error
}
try:
    _ = os.environ['LOG']
    level = _str_to_level[_]
except:
    print ('environment variable LOG is not set, setting debug mode')
    level = _debug


def log_write(level, msg, kwargs=None):
    message = str(msg)
    if kwargs:
        message += ', ' + str(kwargs)
    print(level + ': ' +  message)

def debug(msg, kwargs=None):
    if level <= _debug:
        log_write('DEBUG', msg, kwargs)

def info(msg, kwargs=None):
    if level <= _info:
        log_write('INFO', msg, kwargs)

def warning(msg, kwargs=None):
    if level <= _warning:
        log_write('WARN', msg, kwargs)

def error(msg, kwargs=None):
    if level <= _error:
        log_write('ERROR', msg, kwargs)
