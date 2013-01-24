"""
Logging and other aspects.
"""
import logging
import sys

from logging import NullHandler
from subprocess import check_call, check_output, Popen


class ShellCommand(object):
    """
    Provides a simpler interface for calling shell commands.
    Wraps `subprocess`.
    """

    def __init__(self, cwd=None, cmd=None):
        self.cwd = cwd
        self.cmd = cmd

    def __process__(self, *args, **kwargs):

        if self.cmd and not kwargs.get('shell', False):
            new_args = [self.cmd]
            new_args.extend(args)
            args = new_args

        args = [arg for arg in args if arg]

        if self.cwd and 'cwd' not in kwargs:
            kwargs['cwd'] = self.cwd

        return (args, kwargs)

    def call(self, *args, **kwargs):
        args, kwargs = self.__process__(*args, **kwargs)
        return check_call(args, **kwargs)

    def get(self, *args, **kwargs):
        args, kwargs = self.__process__(*args, **kwargs)
        return check_output(args, **kwargs)

    def open(self, *args, **kwargs):
        args, kwargs = self.__process__(*args, **kwargs)
        return Popen(args, **kwargs)


def getLoggerWithConsoleHandler(logger_name=None):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        if sys.platform == 'win32':
            formatter = logging.Formatter(
                            fmt="%(asctime)s %(name)s %(message)s",
                            datefmt='%H:%M:%S')
        else:
            formatter = ColorFormatter(fmt="$RESET %(asctime)s "
                                      "$BOLD$COLOR%(name)s$RESET "
                                      "%(message)s", datefmt='%H:%M:%S')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger


def getLoggerWithNullHandler(logger_name):
    """
    Gets the logger initialized with the `logger_name`
    and a NullHandler.
    """
    logger = logging.getLogger(logger_name)
    if not logger.handlers:
        logger.addHandler(NullHandler())
    return logger


## Code stolen from :
## http://stackoverflow.com/q/384076
##
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

COLORS = {
    'WARNING': YELLOW,
    'INFO': WHITE,
    'DEBUG': BLUE,
    'CRITICAL': YELLOW,
    'ERROR': RED,
    'RED': RED,
    'GREEN': GREEN,
    'YELLOW': YELLOW,
    'BLUE': BLUE,
    'MAGENTA': MAGENTA,
    'CYAN': CYAN,
    'WHITE': WHITE,
}

RESET_SEQ = "\033[0m"
COLOR_SEQ = "\033[1;%dm"
BOLD_SEQ = "\033[1m"


class ColorFormatter(logging.Formatter):

    def __init__(self, *args, **kwargs):
        # can't do super(...) here because Formatter is an old school class
        logging.Formatter.__init__(self, *args, **kwargs)

    def format(self, record):
        levelname = record.levelname
        color = COLOR_SEQ % (30 + COLORS[levelname])
        message = logging.Formatter.format(self, record)
        message = message.replace("$RESET", RESET_SEQ)\
                           .replace("$BOLD",  BOLD_SEQ)\
                           .replace("$COLOR", color)

        for k, v in COLORS.items():
            message = message.replace("$" + k,    COLOR_SEQ % (v + 30))\
                             .replace("$BG" + k,  COLOR_SEQ % (v + 40))\
                             .replace("$BG-" + k, COLOR_SEQ % (v + 40))
        return message + RESET_SEQ

logging.ColorFormatter = ColorFormatter
